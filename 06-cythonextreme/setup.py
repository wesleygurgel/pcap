from distutils.core import setup
from Cython.Build import cythonize


setup(
    # ext_modules=cythonize(['cumprimentacython.pyx', 'computa.pyx])
    ext_modules=cythonize(['computa.pyx'])
)