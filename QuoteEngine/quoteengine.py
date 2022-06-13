from abc import ABC, abstractmethod
from typing import List
from quotemodel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for file ingestors."""

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @abstractmethod
    def parse_file(cls, file_path) -> List(QuoteModel):
        pass
