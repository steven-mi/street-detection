#!/usr/bin/env python3

import os
from setuptools import setup

about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'street_detection', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['street_detection'],
    include_package_data=True,
    python_requires=">=3.5.*",
    install_requires=['tensorflow', 'requests', 'pillow'],
    license=about['__license__'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['is_street=street_detection.is_street:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='street detection'
)
