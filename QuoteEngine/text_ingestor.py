"""A TXT ingestor to to extract quotes."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """TextIngestor class to overides abstract methods.

    This TextIngestor class overides the parse method
    of the IngestorInterface.
    """

    allowed_extension = ['.txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to read TXT files.

        This method extract lines and return a list of quotes object.

        :param path: File path to the TXT file.
        :return: A collection of Quote object.
        """
        quote_list = []

        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')

            with open(path) as infile:
                for line in infile.readlines():
                    text = line.split('-')
                    if len(text) > 1:
                        quote = text[0].strip()
                        quote = quote.strip('"')
                        author = text[1].strip()
                        new_quote = QuoteModel(quote, author)
                        quote_list.append(new_quote)

        except Exception as error:
            print(f'Error occurred during processing of the TXT file.'
                  f' Details of error "{error}"')

        return quote_list
