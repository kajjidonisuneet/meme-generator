"""This module will set up the Flask server."""

import random
import os
import requests
from flask import Flask, render_template, request
from Meme import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

if not os.path.exists('./static'):
    os.mkdir('./static')

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['_data/DogQuotes/DogQuotesTXT.txt',
                   '_data/DogQuotes/DogQuotesDOCX.docx',
                   '_data/DogQuotes/DogQuotesPDF.pdf',
                   '_data/DogQuotes/DogQuotesCSV.csv']
    base_path = os.path.dirname(__file__)
    quote_files = [os.path.join(base_path, path) for path in quote_files] 
    quotes_list = []
    for files in quote_files:
        quotes_list.extend(Ingestor.parse(files))

    images_path = os.path.join(base_path, "_data/photos/dog/")

    imgs_list = []
    for root, _, files in os.walk(images_path):
        imgs_list = [os.path.join(root, name) for name in files]

    return quotes_list, imgs_list


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    body = request.form.get('body')
    author = request.form.get('author')
    image_url = request.form.get('image_url')
    base_path = os.path.dirname(__file__)
    img_tmp = os.path.join(base_path,'web_temp.png')
    try:
        responce = requests.get(image_url)      
        with open(img_tmp, 'wb') as image_file:
            image_file.write(responce.content)
    except Exception as error:
        print(f'invalid image_url "{error}"')
        return render_template('meme_url_missing.html')

    try:
        path = meme.make_meme(img_tmp, body, author)
        os.remove(img_tmp)
        return render_template('meme.html', path=path)

    except Exception as error:
        print(f'invalid image_url "{error}"')
        return render_template('meme_url_missing.html')


if __name__ == "__main__":
    app.run()
