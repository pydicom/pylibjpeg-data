"""Package shortcuts and variables."""

import os

from ._version import __version__
from .manager import get_indexed_datasets


DATA_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
DICOM_DIRECTORY = os.path.join(DATA_DIRECTORY, 'ds')
JPEG_DIRECTORY = os.path.join(DATA_DIRECTORY, 'jpg')
