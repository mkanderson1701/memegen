"""Class module for the DocX Ingestor.

It mainly consists of one method, for parsing the supported file type.
"""

from quoteengine import IngestorInterface
from quotemodel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Processor for DocX files.

    Mainly a class method parse_file for processing data file.

    allowed_extensions is overridden here, so that parent class method
    Importer.get_file() refers to this class for this extension.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse_file(cls, file_path):
        """Take a DocX file as input, return a list of quote objects."""
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            docx_obj = docx.Document(file_path)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} reading docx {file_path}')
        for paragraph in docx_obj.paragraphs:
            if paragraph.text != "":
                quote_data = paragraph.text.split(' - ')
                quote_data[0] = quote_data[0].strip('"')
                quotes.append(QuoteModel(quote_data[0], quote_data[1]))
        # print(quotes)
        return quotes

    def __repr__(self):
        """Machine-friendly representation."""
        return f'DocxIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'

    def __str__(self):
        """User-friendly representation."""
        return f'DocxIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'


if __name__ == '__main__':
    """Used during module testing."""
    DocxIngestor.parse_file('./_data/DogQuotes/DogQuotesDOCX.docx')
