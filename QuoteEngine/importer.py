"""Unified file importer class.

Checks file extension against all known module extensions,
then call corresponding file parser.
"""

from .quoteengine import IngestorInterface
from .docxingestor import DocxIngestor
from .csvingestor import CsvIngestor
from .pdfingestor import PdfIngestor
from .textingestor import TextIngestor
import os


class Importer(IngestorInterface):
    """Importer class for loading quotes from data files.

    Takes a file path and checks the importers can_ingest method
    for an importer module capable of proessing it.
    """
    def __init__(self):
        self._quote_dirs = ['./_data/DogQuotes/', './_data/SimpleLines']
        self._importers = [DocxIngestor, CsvIngestor, PdfIngestor, TextIngestor]
        self._file_list = []

    def parse_all(self):
        self._all_quotes = []
        print('running')
        for dir in self._quote_dirs:
            print(dir)
            try:
                file_names = os.listdir(dir)
            except BaseException as err:
                print(f'Unexpected {err=}, {type(err)=} listing {dir}')
                raise
            for file_name in file_names:
                # print(file_name)
                try:
                    self._all_quotes.extend(
                        self.parse_file(dir + '/' + file_name))
                except BaseException as err:
                    print(f'Unexpected {err=}, {type(err)=} listing {dir}')
                    raise
        return self._all_quotes

    def parse_file(self, file_path):
        """Run can_ingest for each module against the filename to find a match.

        Calls the supporter importer parse_file function.

        Returns a collection of quote objects.
        """
        # print(file_path)
        for importer in self._importers:
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
    imp = Importer()
    imp.parse_all()
    # print(imp._all_quotes)
