import argparse

from src.scripts import basic_task

parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument('--csv', type=str, required=True, nargs='+', help='path to 1st csv file')
parser.add_argument('--json', type=str, required=True, nargs='+', help='path to 1st csv file')
parser.add_argument('--xml', type=str, required=True, nargs='+', help='path to 1st csv file')
parser.add_argument('--out', type=str, default='out/resp_tsv.tsv', help='path to out tsv file')

args = parser.parse_args()

basic_task(args.csv, args.json, args.xml, args.out)

# python main.py -c1 data/csv_data_1.csv -c2 data/csv_data_2.csv -j data/json_data.json -x data/xml_data.xml
# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml
# python main.py --csv data/csv_data_1.csv data/csv_data_2.csv --json data/json_data.json --xml data/xml_data.xml --out out1/out.tsv
