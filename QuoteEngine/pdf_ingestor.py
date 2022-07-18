"""A PDF ingestor to to extract quotes."""

from typing import List
import subprocess
import os
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    """PDFIngestor class to overides abstract methods.

    This PDFIngestor class overides the parse method
    of the IngestorInterface.
    """

    allowed_extension = ['.pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to read PDF files.

        This method converts pdf files to the txt files
        and return a list of quotes object.

        :param path: File path to the pdf file.
        :return: A collection of Quote object.
        """
        quotes = []

        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')

            tmp = os.path.splitext(path)
            tmp = f'{tmp[0]}Converted.txt'
            subprocess.call(['pdftotext', path, tmp])
            quotes = TextIngestor.parse(tmp)

        except Exception as error:
            print(f'Error occurred during converting pdf file.'
                  f' Details of error "{error}"')

        os.remove(tmp)
        return quotes
