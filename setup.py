# -*- coding: utf-8 -*-
"""analytical solution for thermo-osmosis problem in 1D"""

from setuptools import setup, find_packages

setup(name="anasol.py",
      version=0.1,
      maintainer="Jörg Buchwald",
      maintainer_email="joerg_buchwald@ufz.de",
      author="Jörg Buchwald",
      author_email="joerg.buchwald@ufz.de",
      url="https://github.com/joergbuchwald/thermo-osmosis_analytical_solution",
      license="MIT -  see LICENSE.txt",
      platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
      include_package_data=True,
      install_requires=["numpy", "scipy"],
      py_modules=["heatsource"],
      packages=[])
