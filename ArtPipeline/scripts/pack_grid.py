"""Pack uniform RGBA PNG frames into a row-major atlas; outputs simple JSON frames.

Example:
 python3 ArtPipeline/scripts/pack_grid.py \
   --input ArtPipeline/renders/wudang_male_01/idle/SE \
   --output /tmp/idle_SE.png --cols 6
Requires: pip install Pillow
"""
import argparse
import json
from pathlib import Path
from PIL import Image


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--cols', type=int, default=8)
    args = p.parse_args()
    if args.cols <= 0:
        p.error('--cols must be positive')
    files = sorted(Path(args.input).glob('*.png'))
    if not files:
        p.error('No PNG frames found')
    with Image.open(files[0]) as first:
        size = first.size
    rows = (len(files) + args.cols - 1) // args.cols
    atlas = Image.new('RGBA', (size[0] * args.cols, size[1] * rows))
    frames = []
    for i, file in enumerate(files):
        with Image.open(file) as img:
            if img.size != size:
                raise ValueError(f'Frame size mismatch: {file}')
            x, y = i % args.cols * size[0], i // args.cols * size[1]
            atlas.paste(img.convert('RGBA'), (x, y))
        frames.append({'filename': file.name, 'x': x, 'y': y, 'w': size[0], 'h': size[1]})
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(out)
    out.with_suffix('.json').write_text(json.dumps({'image': out.name, 'frames': frames}, indent=2), encoding='utf-8')
    print(f'Packed {len(frames)} frames -> {out}')


if __name__ == '__main__':
    main()
