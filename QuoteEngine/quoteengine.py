from abc import ABC, abstractmethod
from quotemodel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for file ingestors."""

    @classmethod
    def can_ingest(cls, file_path):
        ext = file_path.split('.')[-1]
        return ext in cls.allowed_extensions

    @abstractmethod
    def parse_file(cls, file_path):
        pass

    def __repr__():
        return f'IngestorInterface(ABC) : abstract base class for quote file ingestors.'

    def __str__():
        return f'IngestorInterface(ABC) : abstract base class for quote file ingestors.'