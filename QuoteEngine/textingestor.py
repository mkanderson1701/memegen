from quoteengine import IngestorInterface
from quotemodel import QuoteModel


class TextIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse_file(cls, file_path):
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(file_path) as file:    
            for line in file:
                quote_data = line.strip('\n').split(' - ')
                quotes.append(QuoteModel(quote_data[0], quote_data[1]))
        # print(quotes)
        return quotes
    
    def __repr__(self):
        return f'TextIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'
    
    def __str__(self):
        return f'TextIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'

if __name__ == '__main__':
    TextIngestor.parse_file('./_data/DogQuotes/DogQuotesTXT.txt')
