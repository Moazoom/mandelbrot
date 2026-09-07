#include <pybind11/pybind11.h>
#include <pybind11/complex.h>

namespace py = pybind11;

int iterate(int max, std::complex<float> z, std::complex<float> c){
    int i = 0;
    for (; i < max; i++){
        float x = std::abs(z);
        if (x > 2.0) break;
        z = z * z + c;
    }
    return i;
}

PYBIND11_MODULE(main, m, py::mod_gil_not_used()) {
    m.def("iterate", &iterate, "A function that adds two numbers");
}