"""A CSV ingestor to to extract quotes."""

from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """DocxIngestor class to overides abstract methods.

    This DocxIngestor class overides the parse method
    of the IngestorInterface.
    """

    allowed_extension = ['.docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to read Doxc files.

        This method extract lines and return a list of quotes object.

        :param path: File path to the Docx file.
        :return: A collection of Quote object.
        """
        if not cls.can_ingest(path):
            return Exception('cannot ingest exception')

        quote_list = []
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')

            doc = docx.Document(path)

            for para in doc.paragraphs:
                line = para.text
                text = line.split('-')
                if len(text) > 1:
                    quote = text[0].strip()
                    quote = quote.strip('"')
                    author = text[1].strip()
                    new_quote = QuoteModel(quote, author)
                    quote_list.append(new_quote)

        except Exception as error:
            print(f'Error occurred during processing of the Docx file.'
                  f' Details of error "{error}"')

        return quote_list
