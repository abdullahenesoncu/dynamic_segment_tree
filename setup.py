# setup.py
from setuptools import setup, Extension
import pybind11
import sys

ext_modules = [
    Extension(
        "dynamic_segment_tree._dseg",
        ["dynamic_segment_tree/_dseg.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-O3", "-std=c++17"]
    )
]

setup(
    name="dynamic-segment-tree",
    version="0.1.0",
    description="Dynamic segment tree (C++) with sparse per-node category counts",
    packages=["dynamic_segment_tree"],
    ext_modules=ext_modules,
    install_requires=["pybind11"],
)
