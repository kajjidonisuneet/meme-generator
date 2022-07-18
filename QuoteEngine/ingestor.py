"""An Ingestor to select the correct Ingestor.

This Ingestor is intended to select the correct Ingestor for a given file type
and to process that file.
"""

from typing import List
from .quote_model import QuoteModel
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor
from .ingestor_interface import IngestorInterface


class Ingestor(IngestorInterface):
    """A Subclass of IngestorInterface to realize the parse method."""

    allowed_ext = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method selects the appropriate ingestor.

        This parse method selects the appropriate ingestor
        is for the given file path.

        :param path: The file path for which the ingestor has to be selected.
        :return: A appropriate ingestor for the given file path.
        """
        for ingestor in cls.allowed_ext:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
