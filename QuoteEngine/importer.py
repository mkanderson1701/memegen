"""Unified file importer class.

Checks file extension against all known module extensions,
then call corresponding file parser.
"""

from quoteengine import IngestorInterface
from docxingestor import DocxIngestor
from csvingestor import CsvIngestor
from pdfingestor import PdfIngestor
from textingestor import TextIngestor


class Importer(IngestorInterface):
    """Importer class with a single get_file method.

    Takes a file path and checks the importers can_ingest method
    for an importer module capable of proessing it.
    """

    importers = [DocxIngestor, CsvIngestor, PdfIngestor, TextIngestor]

    @classmethod
    def parse_file(cls, file_path):
        """Run can_ingest for each module against the filename to find a match.

        Calls the supporter importer parse_file function.

        Returns a collection of quote objects.
        """
        for importer in cls.importers:
            if importer.can_ingest(file_path):
                return importer.parse_file(file_path)

    def __repr__():
        """Machine-friendly representation."""
        return f'Importer object. parse_file() : call available importer.'

    def __str__():
        """Machine-friendly representation."""
        return f'Importer object. parse_file() : call available importer.'


if __name__ == '__main__':
    """Used for testing module."""
    print(Importer.parse_file('./_data/DogQuotes/DogQuotesDOCX.docx'))
    print(Importer.parse_file('./_data/DogQuotes/DogQuotesCSV.csv'))
    print(Importer.parse_file('./_data/DogQuotes/DogQuotesTXT.txt'))
    print(Importer.parse_file('./_data/DogQuotes/DogQuotesPDF.pdf'))
