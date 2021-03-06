"""1.2.840.10008.1.2.4.70 - JPEG Lossless, Non-Hierarchical, First-Order
Prediction (Process 14 [Selection Value 1])
"""

INDEX = {
    '532_JPEGLossless_VOI.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 2021),
        'Columns' : ('US', 2021),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 14),
        'HighBit' : ('US', 13),
        'PixelRepresentation' : ('US', 0),
        'RescaleIntercept' : ('DS', '0'),
        'RescaleSlope' : ('DS', '1'),
        'WindowCenter' : ('DS', ['5339', '5339', '5339']),
        'WindowWidth' : ('DS', ['3368', '2526', '5052']),
        'ImageComments' : ('LT', 'Contains icon and 3 VOI LUTs'),
        'RetrieveURI' : ('UR', 'https://github.com/pydicom/pydicom/issues/532'),
    },
    'JPEG-LL.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1024),
        'Columns' : ('US', 256),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 1),
    },
    'JPEGLosslessP14SV1_1s_1f_u_08_08.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 768),
        'Columns' : ('US', 1024),
        'BitsAllocated' : ('US', 8),
        'BitsStored' : ('US', 8),
        'HighBit' : ('US', 7),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '127'),
        'WindowWidth' : ('DS', '254'),
    },
    'JPEGLosslessP14SV1_1s_1f_u_16_16.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 535),
        'Columns' : ('US', 800),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 0),
    },
    'JPEGLosslessP14SV1_3s_2f_u_08_08.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 3),
        'PhotometricInterpretation' : ('CS', 'RGB'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '2'),
        'Rows' : ('US', 768),
        'Columns' : ('US', 1027),
        'BitsAllocated' : ('US', 8),
        'BitsStored' : ('US', 8),
        'HighBit' : ('US', 7),
        'PixelRepresentation' : ('US', 0),
    },
    'MG1_JPLL.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 4664),
        'Columns' : ('US', 3064),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '2047'),
        'WindowWidth' : ('DS', '4095'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'RG1_JPLL.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1955),
        'Columns' : ('US', 1841),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 15),
        'HighBit' : ('US', 14),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '15000'),
        'WindowWidth' : ('DS', '30000'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'RG2_JPLL.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 2140),
        'Columns' : ('US', 1760),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 10),
        'HighBit' : ('US', 9),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '511'),
        'WindowWidth' : ('DS', '1024'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'SC_rgb_jpeg_gdcm.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.70'),
        'SamplesPerPixel' : ('US', 3),
        'PhotometricInterpretation' : ('CS', 'RGB'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 100),
        'Columns' : ('US', 100),
        'BitsAllocated' : ('US', 8),
        'BitsStored' : ('US', 8),
        'HighBit' : ('US', 7),
        'PixelRepresentation' : ('US', 0),
    },
}
