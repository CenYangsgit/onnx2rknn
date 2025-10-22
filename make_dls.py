#!/usr/bin/env python3
"""从图片目录递归扫描生成 dataset.txt（每行一个图片绝对路径）。"""
import argparse
import os
from pathlib import Path

IMG_EXTS = {'.jpg', '.jpeg', '.png', '.bmp'}

# 用户可编辑默认配置（零参数运行时使用）
DEFAULT_IMG_DIR = './datasets/ccd'
DEFAULT_OUT = './datasets/ccd_01.txt'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('img_dir', type=str, nargs='?', default=DEFAULT_IMG_DIR, help='directory of images (recursively scanned)')
    ap.add_argument('--out', type=str, default=DEFAULT_OUT, help='output txt path')
    args = ap.parse_args()

    img_dir = Path(args.img_dir).resolve()
    if not img_dir.exists():
        raise SystemExit(f'not found: {img_dir}')

    files = []
    for root, _, names in os.walk(img_dir):
        for n in names:
            if Path(n).suffix.lower() in IMG_EXTS:
                files.append(str((Path(root) / n).resolve()))
    if not files:
        raise SystemExit(f'no images under: {img_dir}')

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(files))
    print(f'wrote {len(files)} lines to {out}')

if __name__ == '__main__':
    main()
