"""1.2.840.10008.1.2 - Little Endian Implicit VR"""

INDEX = {
    "rtdose.dcm": {
        "TransferSyntaxUID": ("UI", "1.2.840.10008.1.2"),
        "SamplesPerPixel": ("US", 1),
        "PhotometricInterpretation": ("CS", "MONOCHROME2"),
        "PlanarConfiguration": ("US", 0),
        "NumberOfFrames": ("IS", "15"),
        "Rows": ("US", 10),
        "Columns": ("US", 10),
        "BitsAllocated": ("US", 32),
        "BitsStored": ("US", 32),
        "HighBit": ("US", 31),
        "PixelRepresentation": ("US", 0),
    },
    "rtdose_1frame.dcm": {
        "TransferSyntaxUID": ("UI", "1.2.840.10008.1.2"),
        "SamplesPerPixel": ("US", 1),
        "PhotometricInterpretation": ("CS", "MONOCHROME2"),
        "PlanarConfiguration": ("US", 0),
        "NumberOfFrames": ("IS", "1"),
        "Rows": ("US", 10),
        "Columns": ("US", 10),
        "BitsAllocated": ("US", 32),
        "BitsStored": ("US", 32),
        "HighBit": ("US", 31),
        "PixelRepresentation": ("US", 0),
    },
}
