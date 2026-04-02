from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "stack_stl",
        ["STL.cpp"],
        cxx_std=17,
    ),
]

setup(
    name="stack_stl",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)