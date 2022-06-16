"""Class module for the PDF Ingestor.

It mainly consists of one method, for parsing the supported file type.
"""

from .quoteengine import IngestorInterface
from .quotemodel import QuoteModel
import subprocess


class PdfIngestor(IngestorInterface):
    """Processor for PDF files.

    Mainly a class method parse_file for processing data file.

    allowed_extensions is overridden here, so that parent class method
    Importer.get_file() refers to this class for this extension.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse_file(cls, file_path):
        """Take a PDF file as input, return a list of quote objects."""
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            p = subprocess.Popen(['pdftotext.exe', '-simple', file_path, '-'],
                                 stdout=subprocess.PIPE, text=True)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} reading pdf {file_path}')
        output, err = p.communicate()
        p_status = p.wait()
        txt_list = output.split('\n')

        for quote in txt_list:
            quote_data = quote.split(' - ')
            if len(quote_data) == 2:
                quote_data[0] = quote_data[0].strip('"')
                # print(QuoteModel(quote_data[0], quote_data[1]))
                quotes.append(QuoteModel(quote_data[0], quote_data[1]))

        # print(quotes)
        return quotes

    def __repr__(self):
        """Machine-friendly representation."""
        return f'PdfIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'

    def __str__(self):
        """User-friendly representation."""
        return f'PdfIngestor(IngestorInterface) : ' + \
            'Allowed extensions = {allowed_extensions}'


if __name__ == '__main__':
    """Used during module testing."""
    PdfIngestor.parse_file('./_data/SimpleLines/SimpleLinesNew.pdf')
