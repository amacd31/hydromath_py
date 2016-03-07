import numpy as np
import os
import pkg_resources

from ctypes.util import find_library
from cffi import FFI

PKG_ROOT = os.path.dirname(__file__)

__ffi = FFI()
with open(os.path.join(PKG_ROOT, 'rust_lib', 'hydromath.h')) as header:
    __ffi.cdef(header.read())

__lib = __ffi.dlopen(os.path.join(PKG_ROOT, 'hydromath.so'))

mse_c = __lib.mse_c

def mse(obs, sim):
    assert len(obs) == len(sim)

    return mse_c(
        __ffi.cast('double *', obs.ctypes.data),
        __ffi.cast('double *', sim.ctypes.data),
        len(obs)
    )
