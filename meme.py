import argparse
import random
import os
from QuoteEngine.importer import Importer
from QuoteEngine.quotemodel import QuoteModel
from MemeEngine.memeengine import MemeEngine


def quote_args(args):
    if not args.q or not args.a:

        imp = Importer()
        quote_list = imp.parse_all()
        return random.choice(quote_list)
    else:
        if len(args.q) < 1 or len(args.a) < 1:
            print('Quote and author must be at least 1 character.')
            quit()
        elif len(args.q) > 40 or len(args.a) > 25:
            print('Quote should be under 40 characters, author less than 25.')
            quit()
        return QuoteModel(args.q, args.a)

def make_img(quote, args):
    me = MemeEngine('./images')
    if args.f:
        if os.path.exists(args.f):
            return me.make_meme(args.f, quote._body, quote._author)
        else:
            print(f'file {args.f} not found.')
            quit()
    else:
        return me.make_meme('./_data/photos/dog/', quote._body, quote._author)

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
    quote = quote_args(args)
    file_name = make_img(quote, args)

    print(f'Meme-like image generated: {file_name}')