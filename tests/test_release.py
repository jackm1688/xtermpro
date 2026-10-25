import argparse
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('release', Path(__file__).resolve().parents[1] / 'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_prepare_and_tamper_detection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'source'
            source.mkdir()
            for name in release.names('1.2.3'):
                path = source / name
                if path.suffix == '.zip':
                    with zipfile.ZipFile(path, 'w') as archive:
                        archive.writestr('app.exe', b'fixture')
                else:
                    path.write_bytes(b'fixture' + b'koly' + bytes(508))
            for name in release.DOCS:
                (source / name).write_text('document')
            notes = root / 'notes.md'
            notes.write_text('Release notes')
            args = argparse.Namespace(source=source, bundle=root / 'bundle',
                                      version='1.2.3', notes=notes)
            release.prepare(args)
            manifest = release.load_bundle(args)
            self.assertEqual(len(manifest['assets']), 8)
            with self.assertRaises(ValueError):
                release.prepare(args)
            (args.bundle / 'S3.html').write_text('tampered')
            with self.assertRaisesRegex(ValueError, 'Local asset changed'):
                release.load_bundle(args)

    def test_lfs_pointer_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'app.dmg'
            path.write_bytes(b'version https://git-lfs.github.com/spec/v1\n')
            with self.assertRaisesRegex(ValueError, 'LFS pointer'):
                release.validate_package(path)

    def test_remote_resume_and_mismatch(self):
        args = argparse.Namespace()
        manifest = {'assets': {'app.zip': {'size': 5, 'sha256': 'abc'}}}
        remote = {'assets': []}
        self.assertEqual(release.check_remote(args, manifest, remote, complete=False), {})
        with self.assertRaisesRegex(ValueError, 'Missing remote asset'):
            release.check_remote(args, manifest, remote)
        remote['assets'] = [{'name': 'app.zip', 'size': 5, 'state': 'uploaded', 'digest': 'sha256:abc'}]
        self.assertIn('app.zip', release.check_remote(args, manifest, remote, complete=False))
        remote['assets'][0]['digest'] = 'sha256:wrong'
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            release.check_remote(args, manifest, remote, complete=False)
        remote['assets'][0]['name'] = 'unexpected.zip'
        with self.assertRaisesRegex(ValueError, 'Unexpected'):
            release.check_remote(args, manifest, remote, complete=False)


if __name__ == '__main__':
    unittest.main()
