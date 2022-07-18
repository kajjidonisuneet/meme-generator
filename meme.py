"""To genrate meme from the command line tool."""

import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from Meme import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme from the given path quote and text.

    If any of the parameter are not provided then a
    random selection is carried out.

    :param path: The path of the image file to be used for creating meme.
    :param body: The quote that will be added in the meme image.
    :param author: The author of the quote that will be added in
    the meme image.
    :return: The path of meme file.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A meme generator')
    parser.add_argument('-p', '--path', type=str,
                        help='path to an input image files')
    parser.add_argument('-b', '--body', type=str,
                        help='quote body to add to the image')
    parser.add_argument('-a', '--author', type=str,
                        help='quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
