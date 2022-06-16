import argparse
import random
import os
from QuoteEngine.importer import Importer
from QuoteEngine.quotemodel import QuoteModel
from MemeEngine.memeengine import MemeEngine

def quote_args(args):
    if not args.q and not args.a:
        imp = Importer()
        quote_list = imp.parse_all()
        # print(quote_list)
        return random.choice(quote_list)
    else:
        return QuoteModel(args.q, args.a)

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

    # if not args.q and not args.a:
    #     imp = Importer()
    #     quote_list = imp.parse_all()
    #     # print(quote_list)
    #     quote = random.choice(quote_list)
    # else:
    #     quote = QuoteModel(args.q, args.a)

    me = MemeEngine('./images')
    if args.f:
        if os.path.exists(args.f):
            if str(args.f)[::-1] != '/':
                img_path = args.f + '/'
            me.make_meme(img_path, quote._body, quote._author)
        else:
            print(f'file {args.f} not found.')
            raise
    else:
        # img = me.choose_image('./_data/photos/dog')
        out_file = me.make_meme('./_data/photos/dog/', quote._body, quote._author)
    
    print(f'Meme-like image generated: {out_file}')

    
