import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('build', Path(__file__).resolve().parents[1] / 'scripts/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class PackagingTests(unittest.TestCase):
    def test_archive_rejects_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ('../secret', '/absolute', 'a/../../secret', 'a\\secret'):
                with self.assertRaises(ValueError):
                    build.write_zip(Path(tmp) / 'bad.zip', {name: b'no'})

    def test_archive_reproducible_and_preserves_resources(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / 'a.zip', Path(tmp) / 'b.zip'
            entries = {'skill/SKILL.md': b'instructions', 'skill/references/demo.md': b'evidence'}
            build.write_zip(a, entries)
            build.write_zip(b, dict(reversed(list(entries.items()))))
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with zipfile.ZipFile(a) as archive:
                self.assertEqual(archive.read('skill/references/demo.md'), b'evidence')

    def test_web_bundle_resolves_resource_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'demo'
            (folder / 'references').mkdir(parents=True)
            (folder / 'SKILL.md').write_text('---\nname: demo\ndescription: Test\n---\nRead [example](references/demo.md).')
            (folder / 'references/demo.md').write_text('Synthetic example.')
            result = build.chatgpt_bundle(folder)
            self.assertIn('(#resource-references-demo-md)', result)
            self.assertIn('<a id="resource-references-demo-md">', result)
            self.assertIn('Synthetic example.', result)

    def test_web_bundle_rejects_outside_or_missing_resource(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'demo'
            folder.mkdir()
            (Path(tmp) / 'secret.md').write_text('Private')
            for target in ('../secret.md', 'missing.md'):
                (folder / 'SKILL.md').write_text(f'Read [source]({target}).')
                with self.assertRaises(ValueError):
                    build.chatgpt_bundle(folder)

    def test_skill_resource_rejects_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'demo'
            folder.mkdir()
            secret = Path(tmp) / 'secret.md'
            secret.write_text('Private')
            (folder / 'source.md').symlink_to(secret)
            with self.assertRaises(ValueError):
                build.skill_files(folder)


if __name__ == '__main__':
    unittest.main()
