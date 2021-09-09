import csv
import os

from src.scripts import basic_task


def basic_tsv_test():
    to = 'out_test/'
    filename = 'basic.tsv'
    basic_task(csv_paths=['data/csv_data_1.csv', 'data/csv_data_2.csv'],
               json_paths=['data/json_data.json'],
               xml_paths=['data/xml_data.xml'],
               out=to + filename)

    f1 = open(to + filename)
    f2 = open('results/basic_results.tsv')

    def close():
        f1.close()
        f2.close()
        if os.path.isfile(to + filename):
            os.remove(to + filename)
        if os.path.isdir(to):
            os.rmdir(to)

    tsv1 = csv.reader(f1, delimiter='\t')
    tsv2 = csv.reader(f2, delimiter='\t')
    is_equal = True
    for i1 in tsv1:
        try:
            is_equal = is_equal and i1 == next(tsv2)
        except StopIteration:
            close()
            raise AssertionError("TSV files are not similar")
    try:
        next(tsv2)
        close()
        raise AssertionError("TSV files are not similar")
    except StopIteration:
        pass
    close()
    print("TSV files are similar")


basic_tsv_test()
