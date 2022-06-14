from quoteengine import IngestorInterface
from quotemodel import QuoteModel
import subprocess


class PdfIngestor(IngestorInterface):
    
    allowed_extensions = ['pdf']

    @classmethod
    def parse_file(cls, file_path):
        if not cls.can_ingest(file_path):
            raise Exception('cannot ingest exception')

        quotes = []

        p = subprocess.Popen(['pdftotext', '-simple', file_path, '-'], stdout=subprocess.PIPE, text=True)
        output, err = p.communicate()
        p_status = p.wait()
        txt_list = output.split('\n')

        print(txt_list)

        for quote in txt_list:
            try:
                
            if paragraph.text != "":
                quote_data = paragraph.text.split(' - ')
                quote_data[0] = quote_data[0].strip('"')
                quotes.append(QuoteModel(quote_data[0], quote_data[1]))

        # pdf_string   = pandas.read_csv(file_path, header=0)      
        # for index, quote_data in df.iterrows():
        #     quotes.append(QuoteModel(quote_data['body'], quote_data['author']))
        # print(quotes)
        #return quotes
    
    def __repr__(self):
        return f'PdfIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'
    
    def __str__(self):
        return f'PdfIngestor(IngestorInterface) : Allowed extensions = {allowed_extensions}'

if __name__ == '__main__':
    PdfIngestor.parse_file('./_data/DogQuotes/DogQuotesPDF.pdf')