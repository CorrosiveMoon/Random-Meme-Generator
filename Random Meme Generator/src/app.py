import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources"""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, image) for image in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information"""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme"""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    response = requests.get(image_url)
    if response.status_code != 200:
        abort(400, 'Image URL not valid')

    temp_image_path = './temp/temp_image.jpg'
    with open(temp_image_path, 'wb') as f:
        f.write(response.content)

    path = meme.make_meme(temp_image_path, body, author)
    os.remove(temp_image_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
