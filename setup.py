from setuptools import setup
from rust_ext import build_rust_cmdclass, install_lib_including_rust

setup(name='hydromath',
    version='0.0.1',
    cmdclass={
        # This enables 'setup.py build_rust', and makes it run
        # 'cargo extensions/cargo.toml' before building your package.
        'build_rust': build_rust_cmdclass('hydromath/rust_lib/Cargo.toml'),
        # This causes your rust binary to be automatically installed
        # with the package when install_lib runs (including when you
        # run 'setup.py install'.
        'install_lib': install_lib_including_rust
    },
    packages=['hydromath'],
    package_data={'hydromath': ['rust_lib/hydromath.h']},
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False
)
