"""
Some tests for tasks
"""

import csv
import os

from src.scripts import basic_task, advanced_task


def _compare_two_tsv(to_tsv1: str, to_tsv2: str) -> bool:
    file_1 = open(to_tsv1)
    file_2 = open(to_tsv2)

    def close():
        file_1.close()
        file_2.close()
        if os.path.isfile(to_tsv1):
            os.remove(to_tsv1)
        if os.path.isdir(os.path.split(to_tsv1)[0]):
            os.rmdir(os.path.split(to_tsv1)[0])

    tsv1 = csv.reader(file_1, delimiter='\t')
    tsv2 = csv.reader(file_2, delimiter='\t')
    is_equal = True
    for i in tsv1:
        try:
            is_equal = is_equal and i == next(tsv2)
        except StopIteration:
            close()
            return False
    try:
        next(tsv2)
        close()
        return False
    except StopIteration:
        pass
    close()
    return True


def basic_tsv_test():
    """Test for basic task"""

    to_tsv = 'out_test/basic.tsv'
    to_files = ['data/csv_data_1.csv', 'data/csv_data_2.csv', 'data/json_data.json', 'data/xml_data.xml']
    basic_task(paths=to_files,
               out=to_tsv)

    assert _compare_two_tsv(to_tsv, 'results/basic_results.tsv'), 'TSV are not similar'
    print('Done || Basic Test')


def advanced_tsv_test():
    """Test for advanced task"""

    to_tsv = 'out_test/advanced.tsv'
    to_files = ['data/csv_data_1.csv', 'data/csv_data_2.csv', 'data/json_data.json', 'data/xml_data.xml']
    advanced_task(paths=to_files,
                  out=to_tsv)

    assert _compare_two_tsv(to_tsv, 'results/advanced_results.tsv'), 'TSV are not similar'
    print('Done || Advanced Test')


basic_tsv_test()
advanced_tsv_test()
