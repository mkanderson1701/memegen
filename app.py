"""Main flask web server."""

import random
import os
import requests
import datetime
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, abort, request
from QuoteEngine.importer import Importer
from QuoteEngine.quotemodel import QuoteModel
from MemeEngine.memeengine import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')
images_path = "./_data/photos/dog/"


def setup():
    """Load all resources."""
    if not os.path.isdir('./static'):
        os.makedirs('/static')

    imp = Importer()
    quotes = imp.parse_all()

    imgs = os.listdir(images_path)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = images_path + random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    try:
        r = requests.get(image_url)
        r.raise_for_status()
    except (requests.HTTPError,
            requests.RequestException,
            requests.ConnectionError,
            requests.URLRequired) as e:
        print('Could not load image file, ' +
              'please check the URL and try again.' +
              f'{e}')
        return render_template('meme_error.html')

    temp_img = './static/tmp_' + \
               datetime.datetime.now().strftime("%y%m%d_%H%M%S") + \
               f'.jpg'

    # opening and saving the response stream with pillow
    # adds additional insurance response is a valid image
    try:
        im = Image.open(BytesIO(r.content))
    except OSError:
        print('The remote server did not return a valid image, ' +
              'please check the URL and try again.' +
              f'{e}')
        return render_template('meme_error.html')
    try:
        im.save(temp_img)
    except OSError:
        print('Unable to save image from this URL, ' +
              'please try another address.' +
              f'{e}')
        return render_template('meme_error.html')

    if not body or not author:
        imp = Importer()
        quote_list = imp.parse_all()
        quote = random.choice(quote_list)
    else:
        quote = QuoteModel(body, author)

    path = meme.make_meme(temp_img, quote.body, quote.author)

    try:
        os.remove(temp_img)
    except BaseException as err:
        print(f'Unexpected {err=}, {type(err)=} removing temp {temp_img}')
        raise

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
