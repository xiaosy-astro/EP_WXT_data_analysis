import os
import re
def write_ds9_annulus_region(ra, dec, output_dir='.', filename='bkg.reg',
                              inner_radius='1080.000"', outer_radius='2160.000"',comment='bkg'):
    """
    写入 DS9 annulus region 文件

    参数:
    - ra, dec: 坐标（浮点型，单位为度）
    - output_dir: 输出目录（默认为当前目录）
    - filename: 文件名（默认为 bkg.reg）
    - inner_radius, outer_radius: 环形区域的内/外半径（字符串，带单位，如 "1080.000"）

    返回:
    - 文件的完整路径
    """
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)

    with open(full_path, 'w') as f:
        f.write('# Region file format: DS9 version 4.1\n')
        f.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" '
                'select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n')
        f.write('icrs\n')
        comment_str = f' # text={{ {comment} }}' if comment else ''
        f.write(f'annulus({ra},{dec},{inner_radius},{outer_radius}){comment_str}\n')

    return full_path

import os

def write_ds9_circle_region(ra, dec, output_dir='.', filename='bkg.reg',
                              radius='543.243"',comment='src'):
    """
    写入 DS9 annulus region 文件

    参数:
    - ra, dec: 坐标（浮点型，单位为度）
    - output_dir: 输出目录（默认为当前目录）
    - filename: 文件名（默认为 bkg.reg）
    - radius: 源区域的半径（字符串，带单位，如 "540.000"）

    返回:
    - 文件的完整路径
    """
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)

    with open(full_path, 'w') as f:
        f.write('# Region file format: DS9 version 4.1\n')
        f.write('global color=red dashlist=8 3 width=1 font="helvetica 10 normal roman" '
                'select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n')
        f.write('icrs\n')
        comment_str = f' # text={{ {comment} }}' if comment else ''
        f.write(f'circle({ra},{dec},{radius}){comment_str}\n')

    return full_path

from typing import Tuple

def parse_filename(filename: str) -> Tuple[str, str, str]:
    """
    从标准文件名中解析 obsid, cmos_num, 和 src_num。
    """
    pattern = r'ep(\d+)wxtCMOS(\d+)s(\d+)v\d+'
    match = re.match(pattern, filename)
    if not match:
        raise ValueError(f"文件名 '{filename}' 格式不符合 'ep...wxtCMOS...s...v...' 的预期格式！")
    obsid, cmos_num, src_num = match.group(1), match.group(2), match.group(3)
    return obsid, cmos_num, src_num