# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='random_useragent',
    version='1.0',
    author='Drinor Selmanaj',
    author_email='drinorselmanaj@gmail.com',
    packages=['random_useragent'],
    url='https://github.com/drinorselmanaj/random_useragent',
    license='MIT',
    description='A python library for generating random user-agent strings',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.md']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
