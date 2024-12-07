import numpy as np
from distutils.core import setup, Extension

rlsa_module = Extension("rlsa", sources=["rlsa/rlsa.c"], include_dirs=[np.get_include()])


setup(
    name="rlsa",
    version="0.0.5",
    description="Run Length Smoothing Algorithm",
    install_requires=["numpy"],
    ext_modules=[rlsa_module],
    packages=["rlsa"],
)
