
import os
import sys
import platform
import subprocess
import re
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_version():
    version_file = read("openeye_client_python/version.py")
    version_re = r"__version__ = \"(?P<version>.+)\""
    version = re.match(version_re, version_file).group("version")
    return version

setuptools.setup(
    name="openeye_client_python",
    version=find_version(),
    author="Jaap Oosterbroek",
    author_email="jaapoosterbroek@kexxu.com",
    description="A Library for statistics under Homomorphic Encryption",
    license="Apache-2.0",
    keywords="mouse control openeye eyetracker",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/kexxu-robotics/openeye_client_python",
    packages=setuptools.find_packages(include=["openeye_client_python", "openeye_client_python.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
    ],
    ext_modules=[],
    #cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)