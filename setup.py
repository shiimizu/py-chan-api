# https://github.com/pypa/sampleproject/blob/master/setup.py
from setuptools import setup, find_packages
from os import path
from io import open
from pychan import __version__ as current_version

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-chan-api',
    version=current_version,
    description='A Python wrapper for the 4chan API and other imageboards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shiimizu/py-chan-api',
    author='Shiimizu',
    author_email='shiimizu@protonmail.com',
    license='MIT',
    classifiers=[  # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Natural Language :: English'
    ],
    keywords='4chan api imageboard wrapper',
    packages=find_packages(exclude=['tests', 'test_json']),
    python_requires='>=3.0, <4',
    #install_requires=['bigjson'],
    package_data={
        '': ['README.md','LICENSE'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/shiimizu/py-chan-api/issues',
        'Source': 'https://github.com/shiimizu/py-chan-api',
    },
)