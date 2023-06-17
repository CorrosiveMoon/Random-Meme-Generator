class QuoteModel:
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        """Retun a string representation of the quote."""
        return f'"{self.body}" - {self.author}'
