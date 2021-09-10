"""
Solutions for tasks
"""
from itertools import groupby
from typing import List, Tuple

from .aliases import DataList
from .interfaces import AbstractFileParser
from .parsers import get_parser_by_ext
from .utils import split_str
from .writers import TSVWriter


def _get_dicts_and_headers(paths: List[str]) -> Tuple[List, DataList]:
    parsers: List[AbstractFileParser] = []

    for p in paths:
        parsers.append(get_parser_by_ext(p))

    sorted_headers = parsers[0].raw_headers
    for v in parsers[1:]:
        sorted_headers = sorted_headers & v.raw_headers
    sorted_headers = sorted(sorted_headers, key=split_str)

    dicts: DataList = []
    for parser in parsers:
        dicts += parser.get_fields(sorted_headers)

    return sorted_headers, dicts


def basic_task(paths: List[str], out: str):
    """Script for basic task"""

    sorted_headers, dicts = _get_dicts_and_headers(paths)

    dicts.sort(key=lambda k: k['D1'])

    tsv = TSVWriter()
    tsv.set_headers(sorted_headers)
    tsv.add_rows(*dicts)
    tsv.save(out)


def advanced_task(paths: List[str], out: str):
    """Script for advanced task"""

    sorted_headers, dicts = _get_dicts_and_headers(paths)

    d_headers = [x for x in sorted_headers if x.startswith('D')]
    m_headers = [x for x in sorted_headers if x.startswith('M')]
    dicts.sort(key=lambda k: [k[x] for x in d_headers])

    t_dicts: DataList = []
    for k, v in groupby(dicts, key=lambda el: [el[x] for x in d_headers]):
        v = list(v)
        if len(v) == 1:
            t_dicts.append(v[0])
        else:
            new_d = v[0]
            for d in v[1:]:
                new_d.update({k: new_d[k] + d[k] for k in m_headers})
            t_dicts.append(new_d)
    dicts = t_dicts

    t_dicts = []
    for d in dicts:
        t_dicts.append({k if k.startswith('D') else f"MS{k[1:]}": v for k, v in d.items()})

    sorted_headers = [x if x.startswith('D') else f"MS{x[1:]}" for x in sorted_headers]

    tsv = TSVWriter()
    tsv.set_headers(sorted_headers)
    tsv.add_rows(*t_dicts)
    tsv.save(out)
