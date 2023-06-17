# Meme Generator

Meme generator created by me and as a project for the Udacity Intermediate Python Nanodegree.

## About the Project

This project is a simple meme generator written in Python. It was created as part of Udacity's Python Nanodegree program. The meme generator includes a Flask-based web interface and a command-line interface (CLI). The CLI interface allows you to generate memes and save them to disk.

### Built With:

The Simple Meme Generator is built using the following libraries:

1. Flask: A simple web server interface for the web-based meme generator.
2. Pandas: Used for easy processing of meme text from CSV files.
3. Pillow: Enables image processing to add text to the generated memes.

## Features
The Simple Meme Generator offers the following features:

1. Web Interface: The Flask-based web interface allows users to input text and select an image to generate a meme.
2. Command-Line Interface: The CLI interface allows users to generate memes by providing input via the command line.
3. CSV File Support: The generator can process meme text from CSV files, making it easy to batch generate memes using pre-defined text.
4. Image Processing: The generator uses the Pillow library to process images and add text to the generated memes.
5. Save to Disk: The CLI interface enables users to save the generated memes directly to their local disk.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Sub-Modules

The Simple Meme Generator includes the following sub-modules:

### Flask Web Interface

The Flask web interface allows users to input text and select an image to generate a meme. The web interface is built using the Flask library and includes the following files:

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `static/*`: Static files (CSS, JS, images) used by the web interface.

To run the Flask web interface, execute the following command: python app.py


### Command-Line Interface (CLI)

The CLI interface allows users to generate memes by providing input via the command line. The CLI interface is built using the following files:

- `meme.py`: The main CLI application file.
- `QuoteEngine/*`: Sub-module for processing quote files.
- `MemeGenerator/*`: Sub-module for generating memes.

To generate a meme using the CLI interface, execute the following command: python meme.py --path --body --author


### Quote Engine

The Quote Engine sub-module is responsible for processing quote files. It includes the following files:

- `QuoteEngine/IngestorInterface.py`: Defines the `IngestorInterface` abstract base class.
- `QuoteEngine/CSVIngestor.py`: Sub-class of `IngestorInterface` for processing CSV files.
- `QuoteEngine/DocxIngestor.py`: Sub-class of `IngestorInterface` for processing DOCX files.
- `QuoteEngine/PDFIngestor.py`: Sub-class of `IngestorInterface` for processing PDF files.
- `QuoteEngine/TXTIngestor.py`: Sub-class of `IngestorInterface` for processing TXT files.
- `QuoteEngine/QuoteModel.py`: Defines the `QuoteModel` class.

### Meme Generator
The Meme Generator sub-module is responsible for generating memes. It includes the following files:

MemeGenerator/MemeEngine.py: Defines the MemeEngine class for generating memes.
MemeGenerator/QuoteEngine.py: Defines the QuoteEngine class for processing quote files.
MemeGenerator/__init__.py: Initializes the Meme Generator sub-module.


## Usage

To use the Simple Meme Generator, follow these steps:

1. Run the Flask web interface using the command: python app.py
2. Open the web interface in your browser at http://
3. Enter the desired text and select an image to generate a meme.

To use the CLI interface, follow these steps:

1. Run the CLI interface using the command: python meme.py --path --body --author
2. The generated meme will be saved to the output folder.



## Contact
N/A