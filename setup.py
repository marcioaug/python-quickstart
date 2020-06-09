# _*_ coding: UTF-8 _*_

import os
from setuptools import setup, find_packages

_all__ = ['setup']


install_requires = [

]


def read_file(filename):
    try:
        path = os.path.abspath(os.path.dirname(__file__))
        return open(os.path.join(path, filename)).read()
    except IOError:
        return ''


def readme():
    for readme_file in ['README', 'README.rst', 'README.md']:
        if os.path.exists(readme_file):
            return read_file(readme_file)
    return ''


setup(
    name='python-quickstart',
    version='0.0.0',
    description='A simple quickstart for python projects.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    entry_points={},
    test_suite='nose.collector',
    url='https://github.com/marcioaug/python-quickstart',
    author='Marcio Augusto Guimarães',
    author_email='marcio.guimaraes@edge.ufal.br',
    install_requires=install_requires,
    zip_safe=False,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License ',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning'
    ]
)
