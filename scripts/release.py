#!/usr/bin/env python3
"""Prepare and publish XTermPro distribution assets using GitHub CLI."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DOCS = {'xtermpro-user-manual.html': 'xtermpro-user-manual.html',
        'S3配置指南.html': 'S3.html', 'S3配置指南.docx': 'S3.docx'}


def run(*args):
    return subprocess.check_output(args, text=True).strip()


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def names(version):
    return [f'xtermpro-{version}-{suffix}' for suffix in (
        'arm64.dmg', 'amd64.dmg', 'windows-x64-installer.zip', 'windows-x64.zip')]


def validate_package(path):
    with path.open('rb') as stream:
        if stream.read(128).startswith(b'version https://git-lfs.github.com/spec/'):
            raise ValueError(f'Git LFS pointer is not a package: {path}')
    if path.stat().st_size == 0:
        raise ValueError(f'Empty package: {path}')
    if path.suffix == '.zip':
        with zipfile.ZipFile(path) as archive:
            if not archive.namelist() or archive.testzip() is not None:
                raise ValueError(f'Invalid ZIP: {path}')
    else:
        with path.open('rb') as stream:
            stream.seek(-512, 2)
            if stream.read(4) != b'koly':
                raise ValueError(f'Missing UDIF DMG trailer: {path}')


def prepare(args):
    source = args.source.resolve()
    output = args.bundle.resolve()
    if output.exists():
        raise ValueError(f'Output already exists: {output}; choose a new directory')
    packages = names(args.version)
    for name in packages:
        validate_package(source / name)
    for name in DOCS:
        if not (source / name).is_file():
            raise ValueError(f'Missing document: {name}')
    notes = args.notes.read_text(encoding='utf-8')
    if not notes.strip():
        raise ValueError('Release notes are empty')
    output.parent.mkdir(parents=True, exist_ok=True)
    # Stage beside destination; a failed copy never leaves an apparently complete bundle.
    with tempfile.TemporaryDirectory(dir=output.parent) as temporary:
        stage = Path(temporary) / 'bundle'
        stage.mkdir()
        for src, dst in [(n, n) for n in packages] + list(DOCS.items()):
            shutil.copyfile(source / src, stage / dst)
        (stage / 'SHA256SUMS').write_text(''.join(
            f'{digest(stage / n)}  {n}\n' for n in packages), encoding='utf-8')
        (stage / 'release-notes.md').write_text(notes, encoding='utf-8')
        manifest = {'version': args.version, 'assets': {
            n: {'size': (stage / n).stat().st_size, 'sha256': digest(stage / n)}
            for n in packages + list(DOCS.values()) + ['SHA256SUMS']}}
        (stage / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        stage.rename(output)
    print(f'Prepared: {output}')


def load_bundle(args):
    manifest = json.loads((args.bundle / 'manifest.json').read_text())
    expected = set(names(args.version) + list(DOCS.values()) + ['SHA256SUMS'])
    if manifest['version'] != args.version or set(manifest['assets']) != expected:
        raise ValueError('Bundle version or asset names do not match')
    for name, info in manifest['assets'].items():
        path = args.bundle / name
        if path.stat().st_size != info['size'] or digest(path) != info['sha256']:
            raise ValueError(f'Local asset changed: {name}')
    return manifest


def remote(args):
    # The tag endpoint can return 404 for an unpublished draft without a tag.
    pages = json.loads(run('gh', 'api', '--paginate', '--slurp',
                           f'repos/{args.repo}/releases?per_page=100'))
    matches = [r for page in pages for r in page
               if r['tag_name'] == f'v{args.version}']
    if len(matches) != 1:
        raise ValueError('Expected exactly one matching release')
    return matches[0]


def check_remote(args, manifest, release, complete=True):
    assets = {a['name']: a for a in release['assets']}
    if set(assets) - set(manifest['assets']):
        raise ValueError('Unexpected remote assets; inspect release manually')
    for name, info in manifest['assets'].items():
        asset = assets.get(name)
        if asset is None:
            if complete:
                raise ValueError(f'Missing remote asset: {name}')
            continue
        if (asset['state'] != 'uploaded' or asset['size'] != info['size'] or
                asset.get('digest') != 'sha256:' + info['sha256']):
            raise ValueError(f'Remote size/digest/state mismatch: {name}')
    if complete and release['body'].strip() != (args.bundle / 'release-notes.md').read_text().strip():
        raise ValueError('Remote release notes differ from local notes')
    return assets


def execute(args):
    manifest = load_bundle(args)
    run('gh', 'auth', 'status', '--hostname', 'github.com')
    if args.command == 'draft':
        if not args.target or not re.fullmatch(r'[0-9a-fA-F]{40}', args.target):
            raise ValueError('draft requires --target with a full 40-character commit SHA')
        commit = json.loads(run('gh', 'api', f'repos/{args.repo}/commits/{args.target}'))
        if commit['sha'].lower() != args.target.lower():
            raise ValueError('Remote commit does not match target')
        refs = json.loads(run('gh', 'api',
                              f'repos/{args.repo}/git/matching-refs/tags/v{args.version}'))
        if any(r['ref'] == f'refs/tags/v{args.version}' for r in refs):
            tagged = json.loads(run('gh', 'api', f'repos/{args.repo}/commits/v{args.version}'))
            if tagged['sha'].lower() != args.target.lower():
                raise ValueError('Remote tag does not point to --target')
        releases = json.loads(run('gh', 'api', '--paginate', '--slurp',
                                  f'repos/{args.repo}/releases?per_page=100'))
        existing = [r for page in releases for r in page if r['tag_name'] == f'v{args.version}']
        if not existing:
            run('gh', 'release', 'create', f'v{args.version}', '--repo', args.repo,
                '--draft', '--target', args.target, '--title', f'XTermPro v{args.version}',
                '--notes-file', str(args.bundle / 'release-notes.md'))
        release = remote(args)
        if not release['draft']:
            raise ValueError('Release is already public; refusing to change it')
        if release['target_commitish'].lower() != args.target.lower():
            raise ValueError('Draft target differs from --target; inspect it manually')
        assets = check_remote(args, manifest, release, complete=False)
        for name in manifest['assets']:
            if name not in assets:
                run('gh', 'release', 'upload', f'v{args.version}',
                    str((args.bundle / name).resolve()), '--repo', args.repo)
        check_remote(args, manifest, remote(args))
        print('Draft uploaded and verified; inspect it before publishing.')
    else:
        release = remote(args)
        check_remote(args, manifest, release)
        if args.command == 'publish':
            run('gh', 'release', 'edit', f'v{args.version}', '--repo', args.repo,
                '--draft=false', '--prerelease=false', '--latest')
            release = remote(args)
            check_remote(args, manifest, release)
        if not release['draft']:
            if release['prerelease']:
                raise ValueError('Release is marked prerelease')
            latest = json.loads(run('gh', 'api', f'repos/{args.repo}/releases/latest'))
            if latest['id'] != release['id']:
                raise ValueError('Release is not Latest')
            for asset in release['assets']:
                run('curl', '--fail', '--location', '--silent', '--show-error',
                    '--head', '--retry', '3', '--connect-timeout', '20', '--max-time', '120',
                    asset['browser_download_url'])
        print(('Draft verified: ' if release['draft'] else 'Public release verified: ') + release['html_url'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'draft', 'publish', 'verify'])
    parser.add_argument('--version', required=True, help='Numeric version, for example 3.2.18')
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--repo', default='jackm1688/xtermpro')
    parser.add_argument('--source', type=Path, default=ROOT)
    parser.add_argument('--notes', type=Path)
    parser.add_argument('--target')
    args = parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+', args.version):
        parser.error('--version must be X.Y.Z without v')
    if not re.fullmatch(r'[\w.-]+/[\w.-]+', args.repo):
        parser.error('--repo must be OWNER/REPO on github.com')
    if args.command == 'prepare' and args.notes is None:
        parser.error('prepare requires --notes')
    try:
        prepare(args) if args.command == 'prepare' else execute(args)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, subprocess.CalledProcessError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
