import csv
import os

from src.scripts import basic_task, advanced_task


def _compare_two_tsv(to_tsv1: str, to_tsv2: str, tag: str = ''):
    f1 = open(to_tsv1)
    f2 = open(to_tsv2)

    def close():
        f1.close()
        f2.close()
        if os.path.isfile(to_tsv1):
            os.remove(to_tsv1)
        if os.path.isdir(os.path.split(to_tsv1)[0]):
            os.rmdir(os.path.split(to_tsv1)[0])

    tsv1 = csv.reader(f1, delimiter='\t')
    tsv2 = csv.reader(f2, delimiter='\t')
    is_equal = True
    for i1 in tsv1:
        try:
            is_equal = is_equal and i1 == next(tsv2)
        except StopIteration:
            close()
            raise AssertionError(f"{tag} || TSV files are not similar")
    try:
        next(tsv2)
        close()
        raise AssertionError(f"{tag} || TSV files are not similar")
    except StopIteration:
        pass
    close()
    print(f"{tag} || TSV files are similar")


def basic_tsv_test():
    to_tsv = 'out_test/basic.tsv'
    basic_task(csv_paths=['data/csv_data_1.csv', 'data/csv_data_2.csv'],
               json_paths=['data/json_data.json'],
               xml_paths=['data/xml_data.xml'],
               out=to_tsv)

    _compare_two_tsv(to_tsv, 'results/basic_results.tsv', tag='basic')


def advanced_tsv_test():
    to_tsv = 'out_test/advanced.tsv'
    advanced_task(csv_paths=['data/csv_data_1.csv', 'data/csv_data_2.csv'],
                  json_paths=['data/json_data.json'],
                  xml_paths=['data/xml_data.xml'],
                  out=to_tsv)

    _compare_two_tsv(to_tsv, 'results/advanced_results.tsv', tag='advanced')


basic_tsv_test()
advanced_tsv_test()
