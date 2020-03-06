"""1.2.840.10008.1.2.4.51 - JPEG Extended (Process 2 and 4)"""

INDEX = {
    'JPEGExtended_1s_1f_u_16_12.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.51'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1024),
        'Columns' : ('US', 256),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'ImageComments' : ('LT', 'Fixed version of JPEG-lossy.dcm'),
    },
    'JPEGExtended_3s_1f_u_08_08.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.51'),
        'SamplesPerPixel' : ('US', 3),
        'PhotometricInterpretation' : ('CS', 'YBR_FULL'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 576),
        'Columns' : ('US', 768),
        'BitsAllocated' : ('US', 8),
        'BitsStored' : ('US', 8),
        'HighBit' : ('US', 7),
        'PixelRepresentation' : ('US', 0),
    },
    'JPEG-lossy.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.51'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1024),
        'Columns' : ('US', 256),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'Status' : ('US', 0xC000),
        'ImageComments' : ('LT', 'SOS::Se invalid value 0 (should be 63)'),
    },
    'RG2_JPLY.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.51'),
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
        'Status' : ('US', 0xC000),
        'ImageComments' : ('LT', 'SOS::Se invalid value 0 (should be 63)'),
    },
    'RG2_JPLY_fixed.dcm' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.51'),
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
        'ImageComments' : ('LT', 'Fixed version of RG2_JPLY'),
    },
}
