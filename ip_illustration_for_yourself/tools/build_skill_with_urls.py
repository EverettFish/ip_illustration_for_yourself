#!/usr/bin/env python3
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Resolve YOUR_PUBLIC_BASE_URL for ip_illustration_for_yourself RedSkill publishing.')
parser.add_argument('--base-url', required=True, help='Public root URL, e.g. https://cdn.example.com/ip_illustration_for_yourself')
parser.add_argument('--input', default='SKILL.md')
parser.add_argument('--output', default='SKILL.redskill.md')
args = parser.parse_args()

base = args.base_url.rstrip('/').replace('\\', '/')
source = Path(args.input).read_text(encoding='utf-8')
source = source.replace('YOUR_PUBLIC_BASE_URL', base)
Path(args.output).write_text(source, encoding='utf-8')

ref = Path('REFERENCE_URLS.md')
if ref.exists():
    text = ref.read_text(encoding='utf-8').replace('YOUR_PUBLIC_BASE_URL', base)
    Path('REFERENCE_URLS.resolved.md').write_text(text, encoding='utf-8')

print(f'Wrote {args.output}')
