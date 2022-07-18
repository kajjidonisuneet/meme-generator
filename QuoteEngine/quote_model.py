"""Represents the model for quote.

The 'QuoteModel' class represents a quote object. Each quote object has a
body and author.
"""


class QuoteModel:
    """QuoteModel object.

    An QuoteModel encapsulates the body and author of the Quote.
    """

    def __init__(self, body: str, author: str) -> None:
        """Create a new 'QuoteModel'.

        :param body: The Body of the Quote.
        :param author: The author of the Quote.
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return `repr(self)`, a computer-readable string representation."""
        return f'"{self.body }" - {self.author}'
