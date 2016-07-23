from cffi import FFI

ffi = FFI()

ffi.cdef(
"""
double mse_c(double * obs, double * sim, int n);
double rmse_c(double * obs, double * sim, int n);
double nse_c(double * obs, double * sim, int n);
double kge_c(double * obs, double * sim, int n);
void heaviside(double * input_data, double * output_data, int n);
"""
)

ffi.set_source(
    "hydromath._hydromath_cffi",
    """
    #include <hydromath.h>
    """,
    libraries = ['hydromath'],
)


if __name__ == '__main__':
    ffi.compile()
