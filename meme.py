import os
import random
from argparse import ArgumentParser
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from memeengine import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs.extend([os.path.join(root, name) for name in files])

        img = random.choice(imgs)
    else:
        img = path

    if body is None and author is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv"
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        # Filter out existing quotes with the same body and different author
        filtered_quotes = [
            q for q in quotes if q.body != body or q.author == author
        ]

        if filtered_quotes:
            quote = random.choice(filtered_quotes)
        else:
            quote = random.choice(quotes)
    else:
        if body is None or author is None:
            raise Exception("Both quote body and author are required.")
        quote = QuoteModel(body, author)

    meme = MemeGenerator("./temp")
    
    # Adjust font size for long quotes
    if len(quote.body) > 50:
        meme.font_size = 20
    else:
        meme.font_size = 30
    
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = ArgumentParser(description="Meme Generator Command-Line Tool")
    parser.add_argument("--path", type=str, help="Path to an image file")
    parser.add_argument("--body", type=str, help="Quote body to add to the image")
    parser.add_argument("--author", type=str, help="Quote author to add to the image")
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
