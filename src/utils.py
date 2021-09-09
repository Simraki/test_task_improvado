"""
Shared utils
"""

import re


def str_to_int_optional(s: str):
    return int(s) if s.isdigit() else s


def sep_list(text):
    t = [str_to_int_optional(c) for c in re.split(r'(\d+)', text)]
    return t
