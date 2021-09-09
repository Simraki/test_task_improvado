"""
Solutions for tasks
"""

from typing import List

from .interfaces import AbstractFileParser
from .parsers import CSVFile, JsonFile, XMLFile
from .utils import sep_list
from .writers import TSVWriter


def basic_task(csv_paths: List[str], json_paths: List[str], xml_paths: List[str], out: str):
    parsers: List[AbstractFileParser] = []

    for p in csv_paths:
        parsers.append(CSVFile(p))
    for p in json_paths:
        parsers.append(JsonFile(p))
    for p in xml_paths:
        parsers.append(XMLFile(p))

    sorted_headers = parsers[0].raw_headers
    for v in parsers[1:]:
        sorted_headers = sorted_headers & v.raw_headers
    sorted_headers = sorted(sorted_headers, key=sep_list)

    dicts = []
    for parser in parsers:
        dicts += parser.get_fields(sorted_headers)
    dicts.sort(key=lambda k: k['D1'])

    tsv = TSVWriter()
    tsv.set_headers(sorted_headers)
    tsv.add_rows(*dicts)
    tsv.save(out)
