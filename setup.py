import os
from setuptools import setup, find_packages

scripts = [os.path.join("bin", script) for script in os.listdir("bin")]

setup(
    name="tdqd-tools",
    version="0.0.1",
    packages=find_packages(),
    scripts=scripts,
)
