#!/usr/bin/env python
from setuptools import setup

setup(
    name='ArcherySec',
    version='0.1',
    author='Anand Tiwari',
    description="Tool for managing and scanning vulnerability",
    install_requires=[
        'asn1crypto==0.23.0',
        'certifi==2017.11.5',
        'cffi==1.11.2',
        'chardet==3.0.4',
        'cryptography==3.2',
        'Django==1.11.8',
        'django-appconf==1.0.2',
        'django-cryptography==0.2',
        'django-fernet-fields==0.5',
        'django-stronghold==0.2.9',
        'djangorestframework==3.7.3',
        'enum34==1.1.6',
        'idna==2.6',
        'ipaddress==1.0.18',
        'openvas-lib==1.1.3',
        'pycparser==2.18',
        'python-owasp-zap-v2.4==0.0.13',
        'pytz==2017.3',
        'requests==2.18.4',
        'selenium==3.8.0',
        'six==1.11.0',
        'urllib3==1.22',
    ],
    url='https://github.com/anandtiwarics/archerysec/'
)
