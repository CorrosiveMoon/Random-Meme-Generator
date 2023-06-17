import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from memeengine.meme_generator import MemeGenerator
from meme import generate_meme 

os.makedirs('./static', exist_ok=True)


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
    """ Create a user-defined meme """

    # Get the form data
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    # Save the image from the image_url to a temporary file
    response = requests.get(image_url)
    temp_image_path = './temp/temp_image.jpg'

    os.makedirs('./temp/', exist_ok=True)  # Create the 'temp' directory if it doesn't exist

    with open(temp_image_path, 'wb') as f:
        f.write(response.content)

    try:
        # Generate the meme using the temporary image file and form data
        path = generate_meme(temp_image_path, body, author)

        # Remove the temporary image file
        os.remove(temp_image_path)

        return render_template('meme.html', path=path)
    except Exception as e:
        # Handle the exception and provide an error message
        error_message = f"Error generating meme: {str(e)}"
        return render_template('error.html', error_message=error_message)




if __name__ == "__main__":
    app.run()
