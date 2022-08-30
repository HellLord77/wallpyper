__version__ = '0.0.1'

import distutils.ccompiler
import distutils.command.build_ext
import distutils.core
import os
import sys
from typing import Optional


def compile_c(source: str, output: Optional[str] = None):
    if output is None:
        output = os.path.splitext(source)[0]
    build = distutils.command.build_ext.build_ext(distutils.core.Distribution())
    build.finalize_options()
    compiler = distutils.ccompiler.new_compiler()
    compiler.link_executable(compiler.compile([source], include_dirs=build.include_dirs), output, libraries=[
        f'python{sys.version_info.major}{sys.version_info.minor}'], library_dirs=build.library_dirs)
