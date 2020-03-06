from setuptools import setup, find_packages
import os
import sys

# Version
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
VERSION_FILE = os.path.join(BASE_DIR, 'data', '_version.py')
with open(VERSION_FILE) as fp:
    exec(fp.read())

with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name = "pylibjpeg-data",
    packages = find_packages(),
    include_package_data = True,
    version = __version__,
    zip_safe = False,
    description = (
        "Optional JPEG and DICOM data used for testing pylibjpeg"
    ),
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = "scaramallion",
    author_email = "scaramallion@users.noreply.github.com",
    url = "https://github.com/scaramallion/pylibjpeg-data",
    license = "MIT",
    keywords = (
        "dicom python medicalimaging radiotherapy oncology pydicom imaging "
        "jpg jpeg jpeg-ls pylibjpeg"
    ),
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires = ">=3.6",
    #install_requires = ["pylibjpeg"],
)
