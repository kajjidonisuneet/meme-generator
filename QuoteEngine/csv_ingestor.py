"""A CSV ingestor to extract quotes."""

from typing import List
import pandas
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSVIngestor class.

    This CSVIngestor class overides the parse method of the IngestorInterface.
    """

    allowed_extension = ['.csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to read CSV files.

        This methods extract lines and return a list of quotes object.

        :param path: File path to the CSV file.
        :return: A collection of Quote object.
        """
        quote_list = []
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')

            data_frame = pandas.read_csv(path, header=0)
            for _, row in data_frame.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quote_list.append(new_quote)

        except Exception as error:
            print(f'Error occurred during processing of the CSV file.'
                  f' Details of error "{error}"')

        return quote_list
