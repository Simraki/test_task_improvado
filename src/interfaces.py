"""
Provide abstractions for Parser classes
"""

from abc import abstractmethod, ABC
from typing import Set, List, Optional

from .aliases import DataList
from .utils import split_str


class AbstractFileParser(ABC):
    """Abstract parser class for several extensions"""

    def __init__(self, path: str):
        self._headers: Set[str] = set()
        self._sorted_headers: Optional[List[str]] = None
        self._data: DataList = []
        self._sorted_data: Optional[DataList] = None

        self._load_data(path)

    @abstractmethod
    def _load_data(self, path: str):
        """Load data"""
        raise NotImplementedError

    @property
    def raw_data(self) -> DataList:
        """Get raw data"""
        return self._data

    @raw_data.setter
    def raw_data(self, data):
        """Set raw data and null sorted data"""
        self._data = data
        self._sorted_data = None

    @property
    def raw_headers(self) -> Set[str]:
        """Get raw headers"""
        return self._headers

    @raw_headers.setter
    def raw_headers(self, headers):
        """Set raw headers and null sorted headers"""
        self._headers = headers
        self._sorted_headers = None

    @property
    def sorted_data(self) -> DataList:
        """Get sorted data if it exists OR create and return it"""
        if self._sorted_data:
            return self._sorted_data
        self._sorted_data = [dict(sorted(x.items(), key=lambda l: split_str(l[0])))
                             for x in self.raw_data]
        return self._sorted_data

    @property
    def sorted_headers(self) -> List[str]:
        """Get sorted headers if it exists OR create and return it"""
        if self._sorted_headers:
            return self._sorted_headers
        self._sorted_headers = sorted(self._headers, key=split_str)
        return self._sorted_headers

    def get_fields(self, headers: List) -> DataList:
        """Get sorted data with needed headers"""
        return [{k: v for k, v in x.items() if k in headers} for x in self.sorted_data]
