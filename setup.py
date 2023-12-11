# coding=utf-8
from psdash import __version__
from setuptools import setup

setup(
    name='psdash',
    version=__version__,
    classifiers=[
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Topic :: System :: Networking :: Monitoring',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ],
    keywords='linux web dashboard',
    license='CC0',
    packages=['psdash'],
    package_data={'psdash': ['templates/*', 'static/*']},
    install_requires=[
        'Flask==2.0.3',
        'psutil==5.9.6',
        'glob2==0.7',
        'gevent==22.10.2',
        'zerorpc==0.6.3',
        'netifaces==0.10.4',
        'argparse',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'psdash = psdash.run:main'
        ]
    }
)