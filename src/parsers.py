"""
Provide parsers for different file types
"""

import csv
import json
import xml.etree.ElementTree as ET

from .interfaces import AbstractFileParser
from .utils import str_to_int_optional, is_have_extension


class CSVFile(AbstractFileParser):
    """Extract data from csv"""

    def _load_data(self, path: str):
        csv_reader = csv.reader(open(path))
        headers = next(csv_reader)
        l = []
        for i in csv_reader:
            i = [str_to_int_optional(v) for v in i]
            l.append(dict(zip(headers, i)))
        self.raw_headers = set(headers)
        self.raw_data = l


class JsonFile(AbstractFileParser):
    """Extract data from json"""

    def _load_data(self, path: str):
        t = json.load(open(path))
        headers = set(t['fields'][0].keys())
        self.raw_headers = headers
        self.raw_data = t['fields']


class XMLFile(AbstractFileParser):
    """Extract data from xml"""

    def _load_data(self, path: str):
        root = ET.parse(path).getroot()
        data = []
        headers = set()
        for el in root:
            t = dict()
            for sub_el in el:
                key = sub_el.attrib['name']
                headers.add(key)
                val = str_to_int_optional(sub_el[0].text)
                t[key] = val
            data.append(t)
        self.raw_headers = headers
        self.raw_data = data


_EXT_PARSERS = {
    '.csv': CSVFile,
    '.json': JsonFile,
    '.xml': XMLFile
}


def get_parser_by_ext(to_file: str) -> AbstractFileParser:
    """Return parser class by extension"""
    for ext, parser in _EXT_PARSERS.items():
        if is_have_extension(to_file, ext):
            return parser(to_file)
    raise RuntimeError(f'Unknown input file extension || Path: {to_file}')
