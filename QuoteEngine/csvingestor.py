"""Class module for the CSV Ingestor.

It mainly consists of one method, for parsing the supported file type.
"""

from .quoteengine import IngestorInterface
from .quotemodel import QuoteModel
import pandas


class CsvIngestor(IngestorInterface):
    """Processor for CSV files.

    Mainly a class method parse_file for processing data file.

    allowed_extensions is overridden here, so that parent class method
    Importer.get_file() refers to this class for this extension.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse_file(cls, file_path):
        """Take a CSV file as input, return a list of quote objects."""
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            df = pandas.read_csv(file_path, header=0)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} reading csv {file_path}')
        for index, quote_data in df.iterrows():
            quotes.append(QuoteModel(quote_data['body'], quote_data['author']))
        # print(quotes)
        return quotes

    def __repr__(self):
        """Machine-friendly representation."""
        return f'CsvIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'

    def __str__(self):
        """User-friendly representation."""
        return f'CsvIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'


if __name__ == '__main__':
    """Used during module testing."""
    CsvIngestor.parse_file('./_data/DogQuotes/DogQuotesCSV.csv')
