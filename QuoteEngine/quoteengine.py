"""Abstract parent class for all importer objects.

Implements the can_ingest method, which is called from a child
with a defined list of allowed_extensions.
"""

from abc import ABC, abstractmethod
from quotemodel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class for file ingestors."""

    @classmethod
    def can_ingest(cls, file_path):
        """Compare allowed extensions to a given file extension.

        This is always called from child object methods which have a
        defined list of allowed_extensions.
        """
        ext = file_path.split('.')[-1]
        return ext in cls.allowed_extensions

    @abstractmethod
    def parse_file(cls, file_path):
        """All child objects should implement this abstract class."""
        pass

    def __repr__():
        """Machine-friendly representation."""
        return f'IngestorInterface(ABC) : abstract base class for quote file ingestors.'

    def __str__():
        """User-friendly representation."""
        return f'IngestorInterface(ABC) : abstract base class for quote file ingestors.'