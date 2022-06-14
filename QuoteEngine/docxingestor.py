import docx
from quoteengine import IngestorInterface
from quotemodel import QuoteModel
import re

class DocxIngestor(IngestorInterface):

    allowed_extensions = ['docx']

    @classmethod
    def parse_file(cls, file_path):
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []
        
        docx_obj = docx.Document(file_path)
        for paragraph in docx_obj.paragraphs:
            if paragraph.text != "":
                quote_data = paragraph.text.split(' - ')
                quote_data[0] = quote_data[0].strip('"')
                quotes.append(QuoteModel(quote_data[0], quote_data[1]))
        # print(quotes)
        return quotes
    
    def __repr__(self):
        return f'DocxIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'
    
    def __str__(self):
        return f'DocxIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'

if __name__ == '__main__':
    DocxIngestor.parse_file('./_data/DogQuotes/DogQuotesDOCX.docx')
