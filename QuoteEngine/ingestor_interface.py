"""An interface to select the correct methods.

This interface is meant for selecting the correct ingestor for processing the
given file.
"""

import os
from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Interface for all other ingestor.

    A subclass of Abstract Base Class used as an interface for a all other
    ingestor.
    """

    allowed_extension = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Class method to check if the file extension is supported or not.

        :param path: The file path for which the extension needs to be checked.
        :return: True or False if the given extension is allowed or not.
        """
        extension = os.path.splitext(path)[1]
        return extension in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse is an abstract class method.

        This method will be defined in the inferred class.
        """
        pass
