"""
Main file - entry point
"""

import argparse

from src.scripts import basic_task, advanced_task

parser = argparse.ArgumentParser(description='Script for your tasks')
parser.add_argument('--paths', type=str, required=True, nargs='+', help='Path to input files')
parser.add_argument('--out', type=str, help='Path to out tsv file. Default = out/{mode}_tsv.tsv')
parser.add_argument('-adv', '--advanced', type=bool, const=True, default=False, nargs='?',
                    help='Enabled advanced mode')

args = parser.parse_args()

advanced = args.advanced
if not args.out:
    args.out = f'out/{"advanced" if advanced else "basic"}_tsv.tsv'

if advanced:
    advanced_task(args.paths, args.out)
else:
    basic_task(args.paths, args.out)
