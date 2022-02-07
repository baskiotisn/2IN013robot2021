#!/usr/bin/env python
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md

try:
	with open('package_description.rst', 'r') as file_description:
		description = file_description.read()

except IOError:
	description = "Librairie 2I013-Robot"

from setuptools import setup, find_packages

setup(
    name = "robot2I013",
    version = "1.0.0",

    description = "Librairie pour le controleur du Robot GoPiGo3 pour le cours 2I013-Robot",
    long_description = description,

    author = "N. Baskiotis",
    author_email = "nicolas.baskiotis@lip6.fr",

    license = 'MIT',
    url = "https://github.com/baskiotisn/2I013robot2018",


    packages=find_packages(),
    py_modules = ['robot2I013'],
)
