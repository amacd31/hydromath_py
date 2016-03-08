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

def __map_func(c_func_name, obs, sim):
    """
        Map to a Rust function via the C interface.

        Since all the skill score functions take two arrays (and a length) we
        can avoid repeating code by following the required pattern in one
        place. This function looks up the c/rust function name based on the
        passed argument then passes the converted data into the function. Later
        versions can also handle ensuring the passed arrays are numpy arrays of
        the correct data type.
    """
    assert len(obs) == len(sim)
    return __lib.__getattr__(c_func_name)(
        __ffi.cast('double *', obs.ctypes.data),
        __ffi.cast('double *', sim.ctypes.data),
        len(obs)
    )

def mse(obs, sim):
    return __map_func('mse_c', obs, sim)

def rmse(obs, sim):
    return __map_func('rmse_c', obs, sim)

def nse(obs, sim):
    return __map_func('nse_c', obs, sim)
