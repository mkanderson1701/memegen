from quoteengine import IngestorInterface
from docxingestor import DocxIngestor
from csvingestor import CsvIngestor
from pdfingestor import PdfIngestor
from textingestor import TextIngestor


class Importer(IngestorInterface):
    importers = [DocxIngestor, CsvIngestor, PdfIngestor, TextIngestor]

    @classmethod
    def get_file(cls, path):
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse_file(path)

if __name__ == '__main__':
    print(Importer.get_file('./_data/DogQuotes/DogQuotesDOCX.docx'))
    print(Importer.get_file('./_data/DogQuotes/DogQuotesCSV.csv'))
    print(Importer.get_file('./_data/DogQuotes/DogQuotesTXT.txt'))
    # print(Importer.get_file('./_data/DogQuotes/DogQuotesPDF.pdf'))