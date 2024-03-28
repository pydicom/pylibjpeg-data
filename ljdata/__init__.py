"""Package shortcuts and variables."""

from pathlib import Path

from ._version import __version__
from .manager import get_indexed_datasets


DATA_DIRECTORY = Path(__file__).resolve().parent
DICOM_DIRECTORY = DATA_DIRECTORY / "ds"
JPEG_DIRECTORY = DATA_DIRECTORY / "jpg"
