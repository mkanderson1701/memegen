import pandas
from quoteengine import IngestorInterface
from quotemodel import QuoteModel


class CsvIngestor(IngestorInterface):

    allowed_extensions = ['csv']

    @classmethod
    def parse_file(cls, file_path):
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []

        df = pandas.read_csv(file_path, header=0)      
        for index, quote_data in df.iterrows():
            quotes.append(QuoteModel(quote_data['body'], quote_data['author']))
        # print(quotes)
        return quotes
    
    def __repr__(self):
        return f'CsvIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'
    
    def __str__(self):
        return f'CsvIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'

if __name__ == '__main__':
    CsvIngestor.parse_file('./_data/DogQuotes/DogQuotesCSV.csv')