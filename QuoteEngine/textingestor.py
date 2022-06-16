"""Class module for the plaintext Ingestor.

It mainly consists of one method, for parsing the supported file type.
"""

from .quoteengine import IngestorInterface
from .quotemodel import QuoteModel


class TextIngestor(IngestorInterface):
    """Processor for plaintext files.

    Mainly a class method parse_file for processing data file.

    allowed_extensions is overridden here, so that parent class method
    Importer.get_file() refers to this class for this extension.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse_file(cls, file_path):
        """Take a txt file as input, return a list of quote objects."""
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(file_path) as file:    
            for line in file:
                # print(line)
                quote_data = line.strip('\n').split(' - ')
                if len(quote_data) == 2:
                    quotes.append(QuoteModel(quote_data[0], quote_data[1]))
        # print(quotes)
        return quotes

    def __repr__(self):
        """Machine-friendly representation."""
        return f'TextIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'

    def __str__(self):
        """User-friendly representation."""
        return f'TextIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'


if __name__ == '__main__':
    """Used during module testing."""
    TextIngestor.parse_file('./_data/DogQuotes/DogQuotesTXT.txt')
