"""
Main file - entry point
"""

import argparse

from src.scripts import basic_task, advanced_task

parser = argparse.ArgumentParser(description='Script for your tasks')
parser.add_argument('--csv', type=str, required=True, nargs='+', help='Path to 1st csv file')
parser.add_argument('--json', type=str, required=True, nargs='+', help='Path to 1st csv file')
parser.add_argument('--xml', type=str, required=True, nargs='+', help='Path to 1st csv file')
parser.add_argument('--out', type=str, help='Path to out tsv file. Default = out/{mode}_tsv.tsv')
parser.add_argument('-adv', '--advanced', type=bool, const=True, default=False, nargs='?',
                    help='Enabled advanced mode')

args = parser.parse_args()

advanced = args.advanced
if not args.out:
    args.out = f'out/{"advanced" if advanced else "basic"}_tsv.tsv'
args = [args.csv, args.json, args.xml, args.out]

if advanced:
    advanced_task(*args)
else:
    basic_task(*args)

# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml
# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml --out out1/out.tsv
# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml -adv
# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml --out out1/out.tsv -adv
