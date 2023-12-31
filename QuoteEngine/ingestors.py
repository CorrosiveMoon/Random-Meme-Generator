from abc import ABC, abstractmethod
import os
import subprocess
from typing import List
import pandas as pd
from docx import Document
from QuoteEngine import QuoteModel

class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the class can ingest a file based on its file type.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the class can ingest the file, False otherwise.
        """
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances representing the quotes found in the file.
        """
        pass


class CSVIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the class can ingest a CSV file.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the class can ingest the CSV file, False otherwise.
        """
        return path.endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the CSV file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances representing the quotes found in the CSV file.
        """
        df = pd.read_csv(path)
        quotes = []
        for _, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes


class DocxIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the class can ingest a DOCX file.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the class can ingest the DOCX file, False otherwise.
        """
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the DOCX file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the DOCX file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances representing the quotes found in the DOCX file.
        """
        quotes = []
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                quote = QuoteModel(paragraph.text, paragraph.style.name)
                quotes.append(quote)
        return quotes


class PDFIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        # Check if the class can ingest a PDF file
        return path.endswith('.pdf')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Parse the PDF file and return a list of QuoteModel instances
        quotes = []
        temp_file = 'temp.txt'
        try:
            # Call pdftotext to convert PDF to text
            subprocess.run(['pdftotext', path, temp_file], check=True)

            with open(temp_file, 'r') as f:
                for line in f:
                    if line.strip():
                        quote = QuoteModel(line.strip(), '')
                        quotes.append(quote)
        finally:
            os.remove(temp_file)
        return quotes



class TXTIngestor(IngestorInterface):
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the class can ingest a TXT file.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the class can ingest the TXT file, False otherwise.
        """
        return path.endswith('.txt')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the TXT file and return a list of QuoteModel instances.

        Args:
            path (str): The path to the TXT file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances representing the quotes found in the TXT file.
        """
        quotes = []
        # Logic to parse TXT file and extract quotes
        # Append QuoteModel instances to the quotes list
        return quotes


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file using the appropriate ingestor and return a list of QuoteModel instances.

        Args:
            path (str): The path to the file.

        Returns:
            List[quote_model]: A list of QuoteModel instances representing the quotes found in the file.

        Raises:
            ValueError: If the file type is not supported by any ingestor.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError('Unsupported file type')
