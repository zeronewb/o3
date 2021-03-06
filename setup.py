#  -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='o3',
    packages=find_packages(include=('o3',)),
    url='https://github.com/mblomdahl/o3',
    license='The Unlicense',
    description='Hadoop-Airflow analytics',
    # https://pypi.python.org/pypi?:action=list_classifiers
    install_requires=[
        'psycopg2',
        'hdfs3',
        'apache-airflow[password,ssh]',
        'ansible',
        'netaddr',
        'ipython',
        'pandas',
        'fastavro',
        'pyhive'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6'
    ],
    platforms=['POSIX']
)
