from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import pkg_resources

data_dir = pkg_resources.resource_filename("autowrap", "data_files/autowrap")

ext = Extension(
    "parser",
    sources=['parser.cpp'],
    language="c++",
    include_dirs=['.', data_dir],
    gdb_debug=True,
    compiler_directives=dict(
        # boundscheck=False,
        # wraparound=False,

        embedsignature=True,
        # profile=True,
        linetrace=True,
        language_level=3,
    ),
)

setup(cmdclass={'build_ext':build_ext},
      name="parser",
      # packages=['c_parser', 'parser'],
      version="0.0.1",
      ext_modules=[ext, ext]
     )
