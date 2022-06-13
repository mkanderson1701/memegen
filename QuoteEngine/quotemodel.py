class QuoteModel():

    def __init__(self, body, author):
        self._body = body
        self._author = author

    def __repr__(self):
        return f'QuoteModel("{self._body}", "{self._author}")'

    def __str__(self):
        return f'"{self._body}" - {self._author}'
