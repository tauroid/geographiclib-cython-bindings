import sys
from distutils.core import setup, Extension

extensions = [Extension(
    "geographiclib_cython",
    ["geographiclib_cython.pyx"],
    libraries=["GeographicLib"]
)]

from Cython.Build import cythonize
extensions = cythonize(extensions)

setup(
    name="geographiclib-cython-bindings",
    description="""Cython extension module for C++ geographiclib functions""",
    version="0.2.0",
    author="Sergey Serebryakov",
    author_email="sergey@serebryakov.info",
    url="https://github.com/megaserg/geographiclib-cython-bindings",
    license="MIT",
    ext_modules=extensions
)
