#!/usr/bin/env python

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pyf',
    py_modules=['pyf'],
    version='0.1.0',
    author='Sérgio Rafael Siqueira',
    author_email='osergiosiqueira@gmail.com',
    url='https://github.com/sergiors/pyf',
    download_url='https://github.com/sergiors/pyf/tarball/master',
    long_description=readme,
    long_description_content_type='text/markdown; charset=UTF-8',
    license='MIT license',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pipe==1.5.0'
    ],
)
