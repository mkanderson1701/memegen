import argparse
from QuoteEngine.importer import Importer
from QuoteEngine.quotemodel import QuoteModel

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a meme-ish image.',
                                     argument_default=None)
    parser.add_argument('-q', type=str,
                        help='text body of the quote.', required=False)
    parser.add_argument('-a', type=str,
                        help='the quote author.', required=False)
    parser.add_argument('-f', type=str,
                        help='path to a custom image file.', required=False)

    args = parser.parse_args()

    if not args.a and not args.b:
        imp = Importer()
        quote_list = imp.parse_all()
        print(quote_list)

    print(args.a)
