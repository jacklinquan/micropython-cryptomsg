import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(
    name="micropython-cryptomsg",
    version="0.1.0",
    description="A MicroPython module to encrypt and decrypt messages " \
        + "with AES CBC mode.",
    long_description="https://github.com/jacklinquan/micropython-cryptomsg",
    long_description_content_type="text/markdown",
    url="https://github.com/jacklinquan/micropython-cryptomsg",
    author="Quan Lin",
    author_email="jacklinquan@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: MicroPython"
    ],
    cmdclass={"sdist": sdist_upip.sdist},
    py_modules=["cryptomsg"],
)
