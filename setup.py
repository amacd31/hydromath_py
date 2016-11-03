from setuptools import setup
import versioneer

setup(name='hydromath',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['hydromath'],
    install_requires=['cffi>=1.0.0'],
    cffi_modules=["hydromath/_build.py:ffi"],
)
