#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name = 'svg2rlg',
    py_modules = ['svg2rlg'],
    version = '0.4.0',
    author='Runar Tenfjord',
    author_email = 'runar.tenfjord@gmail.com',
    maintainer = 'Steve Arnold',
    maintainer_email = 'nerdboy@gentoo.org',
    license = 'BSD',
    url = 'https://github.com/sarnold/svg2rlg',
    download_url = 'http://pypi.python.org/pypi/svg2rlg/',
    requires = ['reportlab'],
    entry_points = {
                'console_scripts': ['svg2rlg = svg2rlg:main']},

    classifiers=[
          'Environment :: Console',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],

    description = 'Convert SVG to Reportlab drawing',
    long_description_content_type='text/x-rst',
    long_description = '''**svg2rlg** is a small utility to convert SVG to reportlab graphics.

The authors motivation was to have a more robust handling of
SVG files in the **rst2pdf** tool. Specific to be able to handle
the quirks needed to include SVG export from matplotlib.
'''
)
