"""Command line version of meme creator."""

import argparse
import random
import os
from QuoteEngine.importer import Importer
from QuoteEngine.quotemodel import QuoteModel
from MemeEngine.memeengine import MemeEngine


def quote_args(args):
    """Process body and author args passed in command line.

    If either body or author is missing, load all the datafiles and
    choose a full quote at random.
    """
    if not args.body or not args.author:
        imp = Importer()
        quote_list = imp.parse_all()
        return random.choice(quote_list)
    else:
        if len(args.body) < 1 or len(args.author) < 1:
            print('Quote and author must be at least 1 character.')
            quit()
        elif len(args.body) > 40 or len(args.author) > 25:
            print('Quote should be under 40 characters, author less than 25.')
            quit()
        return QuoteModel(args.body, args.author)


def make_img(quote, args):
    """Build a meme with an image file.

    If args inclued a file and that file exists, use it.
    If not choose one at random.
    """
    me = MemeEngine('./images')
    if args.path:
        if os.path.exists(args.path):
            return me.make_meme(args.path, quote.body, quote.author)
        else:
            print(f'file {args.path} not found.')
            quit()
    else:
        return me.make_meme('./_data/photos/dog/', quote.body, quote.author)


if __name__ == "__main__":
    """Initialize the meme creator."""
    parser = argparse.ArgumentParser(description='Create a meme-ish image.',
                                     argument_default=None)
    parser.add_argument('--body', type=str,
                        help='text body of the quote.', required=False)
    parser.add_argument('--author', type=str,
                        help='the quote author.', required=False)
    parser.add_argument('--path', type=str,
                        help='path to a custom image file.', required=False)

    args = parser.parse_args()
    quote = quote_args(args)
    file_name = make_img(quote, args)

    print(f'{file_name}')
