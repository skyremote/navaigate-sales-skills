#!/usr/bin/env python3
"""Validate published paths, generated bundles and the allowlisted archive contents."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
from build import ROOT, SELLING_SLUGS, SLUGS, VERSION, chatgpt_bundle, skill_files


def validate():
    all_skills = ROOT / 'skills'
    assert {p.name for p in all_skills.iterdir() if p.is_dir()} == set(SLUGS), 'Unexpected skill set'
    for slug in SLUGS:
        folder = all_skills / slug
        text = (folder / 'SKILL.md').read_text()
        assert text.startswith('---\n') and '\n---\n' in text[4:], f'Missing frontmatter: {slug}'
        front = text[4:].split('\n---\n', 1)[0]
        assert f'name: {slug}\n' in front + '\n', f'Wrong skill name: {slug}'
        assert re.search(r'^description: .+', front, re.M), f'Missing description: {slug}'
        assert (ROOT / 'chatgpt' / f'{slug}.md').read_text() == chatgpt_bundle(folder), f'Stale web bundle: {slug}'
        with zipfile.ZipFile(ROOT / 'dist' / f'{slug}-v{VERSION}.zip') as archive:
            wanted = {f'{slug}/{p.relative_to(folder)}': p.read_bytes() for p in skill_files(folder)}
            assert set(archive.namelist()) == set(wanted), f'Unexpected ZIP content: {slug}'
            assert all(archive.read(n) == b for n, b in wanted.items()), f'ZIP drift: {slug}'
    manifest = json.loads((ROOT / 'dist/source-manifest.json').read_text())
    for name, digest in manifest.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, f'Source drift: {name}'
    for archive_path in (ROOT / 'dist').glob('*.zip'):
        with zipfile.ZipFile(archive_path) as archive:
            assert not archive.testzip(), f'Corrupt archive: {archive_path.name}'
            for name in archive.namelist():
                assert not name.startswith('/') and '..' not in Path(name).parts and '\\' not in name
                assert not any(part in ('private', 'outputs', '.git', 'node_modules') for part in Path(name).parts)
            if '-plugin-' in archive_path.name:
                import posixpath
                names = set(archive.namelist())
                for name in names:
                    if not name.endswith('.md'):
                        continue
                    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', archive.read(name).decode()):
                        if re.match(r'^(?:https?://|mailto:|#)', target):
                            continue
                        destination = posixpath.normpath(posixpath.join(posixpath.dirname(name), target.split('#')[0]))
                        assert destination in names or any(p.startswith(destination.rstrip('/') + '/') for p in names), f'Broken packaged link: {name} -> {target}'
            if archive_path.name.startswith('selling-at-ai-speed-plugin-'):
                assert json.loads(archive.read('.claude-plugin/plugin.json'))['name'] == 'selling-at-ai-speed'
                actual = {name.split('/')[1] for name in archive.namelist() if name.startswith('skills/')}
                assert actual == set(SELLING_SLUGS), 'Standalone plugin must contain exactly four original workflows'
                for slug in SELLING_SLUGS:
                    for path in skill_files(ROOT / 'skills' / slug):
                        name = f'skills/{slug}/{path.relative_to(ROOT / "skills" / slug)}'
                        assert archive.read(name) == path.read_bytes(), f'Standalone plugin drift: {name}'
    # Check local Markdown links in source docs; generated web bundles use in-file anchors.
    for directory in ('skills', 'docs'):
        for path in (ROOT / directory).rglob('*.md'):
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
                if re.match(r'^(?:https?://|mailto:|#)', target):
                    continue
                assert (path.parent / target.split('#')[0]).exists(), f'Broken link: {path.name} -> {target}'
    for line in (ROOT / 'dist/SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert hashlib.sha256((ROOT / 'dist' / name).read_bytes()).hexdigest() == digest, f'Checksum drift: {name}'
    print(f'PASS: {len(SLUGS)} skills; four-skill standalone plugin; fresh web bundles; exact ZIP resources; links; checksums; safe paths.')


if __name__ == '__main__':
    validate()
