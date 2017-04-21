# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as BaseBuildPy
from distutils.errors import DistutilsSetupError
from distutils.dep_util import newer

VERSION_FILE = "VERSION"
PY_VERSION_FILE = "dpkg/version.py"


def get_version_string():
    try:
        with open(VERSION_FILE) as f:
            return f.read().strip()
    except IOError:
        raise DistutilsSetupError("failed to read version info")


def write_version():
    if newer(VERSION_FILE, PY_VERSION_FILE):
        with open(PY_VERSION_FILE, "w") as f:
            f.write("# GENERATED BY setup.py\n")
            f.write("version = '%s'\n" % (get_version_string()))


class BuildPy(BaseBuildPy):

    def run(self):
        write_version()
        BaseBuildPy.run(self)


with open('README.rst') as f:
    readme = f.read()


setup(
    name='cell_track_dpkg',
    version=get_version_string(),
    description='Data package representation for cell migration tracking data',
    long_description=readme,
    author='paola masuzzo',
    author_email='paola.masuzzo@ugent.be',
    url='https://github.com/pcmasuzzo/cell_track_dpkg',
    license="BSD",
    cmdclass={"build_py": BuildPy},
    packages=find_packages(exclude=('tests', 'docs'))
)
