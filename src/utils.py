"""
Shared utils
"""

import re
from typing import Union, List


def str_to_int_optional(s: str) -> Union[str, int]:
    """Convert string to integer if string only contains digits"""

    return int(s) if s.isdigit() else s


def split_str(text) -> List[Union[str, int]]:
    """Split a string into a list of characters"""

    return [str_to_int_optional(c) for c in re.split(r'(\d+)', text)]


def is_have_extension(path: str, ext: str) -> bool:
    """Check if file by path have extension"""

    if path.endswith('/'):
        path = path[:-1]
    return path.endswith(ext)
