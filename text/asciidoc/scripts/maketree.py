#!/usr/bin/env python3
from pathlib import Path

lines = [
    '<div id="tree">',
    '  <ul>',
    *[f'    <li><a href="{path}">{path}</a></li>'
      for path in sorted(Path().iterdir())],
    '  </ul>',
    '</div>',
]
print(*lines, sep='\n')
