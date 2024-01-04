
from pathlib import Path

try:
    from pydicom import dcmread
    HAS_PYDICOM = True
except ImportError:
    HAS_PYDICOM = False

from ljdata.ds import (
    JPEG2000_IDX,
    JPEG2000Lossless_IDX,
    JPEGBaseline_IDX,
    JPEGExtended_IDX,
    JPEGLossless_IDX,
    JPEGLosslessSV1_IDX,
    JPEGLS_IDX,
    JPEGLSLossless_IDX,
    LittleEndianExplicit_IDX,
    LittleEndianImplicit_IDX,
    RLELossless_IDX,
)

DATA_DIRECTORY = Path(__file__).resolve().parent
DS_DIR = DATA_DIRECTORY / 'ds'
JPG_DIR = DATA_DIRECTORY / 'jpg'


UIDS = {
    '1.2.840.10008.1.2':       'LittleEndianImplicit',
    '1.2.840.10008.1.2.1':     'LittleEndianExplicit',
    '1.2.840.10008.1.2.4.50':  'JPEGBaseline',
    '1.2.840.10008.1.2.4.51':  'JPEGExtended',
    '1.2.840.10008.1.2.4.57':  'JPEGLossless',
    '1.2.840.10008.1.2.4.70':  'JPEGLosslessSV1',
    '1.2.840.10008.1.2.4.80':  'JPEGLSLossless',
    '1.2.840.10008.1.2.4.81':  'JPEGLS',
    '1.2.840.10008.1.2.4.90':  'JPEG2000Lossless',
    '1.2.840.10008.1.2.4.91':  'JPEG2000',
    '1.2.840.10008.1.2.4.201': 'HTJ2KLossless',
    '1.2.840.10008.1.2.4.203': 'HTJ2K',
    '1.2.840.10008.1.2.5':     'RLELossless',
}


def get_datasets(uid, as_dataset=False):
    """Return a list of Path to matching DICOM datasets.

    Parameters
    ----------
    uid : str
        The transfer syntax UID of the DICOM datasets.
    as_dataset : bool, optional
        If ``True`` return the dataset as a pydicom Dataset object (requires
        pydicom to be installed), default ``False``.

    Returns
    -------
    Union[List[Path], List[Dataset]]
    """
    subdir = UIDS[uid]
    fnames = get_indices('ds')[subdir].keys()
    fpaths = [DS_DIR / subdir / fname for fname in fnames]
    if as_dataset:
        if not HAS_PYDICOM:
            raise RuntimeError("'as_dataset=True' requires pydicom")

        return [dcmread(fpath) for fpath in fpaths]

    return fpaths


def get_indexed_datasets(uid):
    subdir = UIDS[uid]
    index = get_indices('ds')[subdir]
    fnames = index.keys()
    for fname in fnames:
        fpath = DS_DIR / subdir / fname
        index[fname]['ds'] = dcmread(fpath)

    return index


def get_from_parameter(index, keyword, value):
    matches = []
    for kk, vv in index.items():
        if keyword in vv and vv[keyword] == value:
            matches.append(index[kk]['ds'])

    return matches


def get_indices(index_type='ds'):
    """Return a :class:`dict` containing all the indices for `index_type`.

    Parameters
    ----------
    index_type : str
        The index type to get, one of ``'ds'``.
    """
    if index_type == 'ds':
        return {
            'LittleEndianImplicit' : LittleEndianImplicit_IDX,
            'LittleEndianExplicit' : LittleEndianExplicit_IDX,
            'JPEGBaseline' : JPEGBaseline_IDX,
            'JPEGExtended' : JPEGExtended_IDX,
            'JPEGLossless' : JPEGLossless_IDX,
            'JPEGLosslessSV1' : JPEGLosslessSV1_IDX,
            'JPEGLSLossless' : JPEGLSLossless_IDX,
            'JPEGLS' : JPEGLS_IDX,
            'JPEG2000Lossless' : JPEG2000Lossless_IDX,
            'JPEG2000' : JPEG2000_IDX,
            'RLELossless' : RLELossless_IDX,
        }
