"""
Provide writers for different file types
"""

import csv
import os

from .aliases import DataRow, DataList


class TSVWriter:
    """Provide methods for recording TSV"""

    def __init__(self):
        self._list_dicts: DataList = []
        self._headers = None

    def set_headers(self, headers):
        """Set headers to TSV"""
        self._headers = headers

    def add_row(self, row: DataRow):
        """Add row to TSV data"""
        if not self._headers:
            raise RuntimeError("Headers is None in TSV Writer")
        self._list_dicts.append(row)

    def add_rows(self, *rows: DataRow):
        """Add some rows to TSV data"""
        for row in rows:
            self.add_row(row)

    def save(self, out: str):
        """Save TSV with contained headers and data"""

        (to_file, _) = os.path.split(out)
        if not os.path.exists(to_file):
            os.makedirs(to_file)
        with open(out, 'w', newline='') as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=self._headers)
            writer.writeheader()
            for d in self._list_dicts:
                writer.writerow(d)
            file.close()
