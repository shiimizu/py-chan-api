# https://github.com/pypa/sampleproject/blob/master/setup.py
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-chan-api',
    version='0.1.1',
    description='A Python wrapper for the 4chan API and other imageboards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shiimizu/py-chan-api',
    author='Shiimizu',
    author_email='shiimizu@protonmail.com',
    classifiers=[  # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='4chan api imageboard',
    packages=find_packages(exclude=['tests', 'test_json']),
    python_requires='>=3.7, <4',
    install_requires=['bigjson','psutil'],
    package_data={
        '': ['README.md','LICENSE'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/shiimizu/py-chan-api/issues',
        'Source': 'https://github.com/shiimizu/py-chan-api',
    },
)