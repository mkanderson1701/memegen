"""Basic module for holding quote data."""


class QuoteModel():
    """Represent a quote."""

    def __init__(self, body, author):
        """Create a new quote object."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Machine-friendly representation."""
        return f'QuoteModel("{self._body}", "{self._author}")'

    def __str__(self):
        """User-friendly representation."""
        return f'"{self._body}" - {self._author}'
