import numpy as np

from cffi import FFI
from hydromath import _hydromath_cffi

__ffi = FFI()
__lib = _hydromath_cffi.lib

def __map_func(c_func_name, obs, sim):
    """
        Map to function via the C interface.

        Since all the skill score functions take two arrays (and a length) we
        can avoid repeating code by following the required pattern in one
        place. This function looks up the c function name based on the
        passed argument then passes the converted data into the function. Later
        versions can also handle ensuring the passed arrays are numpy arrays of
        the correct data type.
    """
    assert len(obs) == len(sim)
    return getattr(__lib, c_func_name)(
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

def kge(obs, sim):
    return __map_func('kge_c', obs, sim)
