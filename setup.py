from setuptools import setup

setup(name='hydromath',
    version='0.0.1',
    packages=['hydromath'],
    install_requires=['cffi>=1.0.0'],
    cffi_modules=["hydromath/_build.py:ffi"],
)
