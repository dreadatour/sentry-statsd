#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3',
    'statsd',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-statsd',
    version='0.0.2',
    author='Vladimir Rudnyh',
    author_email='dreadatour@gmail.com',
    url='http://github.com/dreadatour/sentry-statsd',
    description='A Sentry extension which send errors stats to StatsD',
    long_description=readme,
    license='WTFPL',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_statsd = sentry_statsd.plugin:StatsdPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
    keywords='sentry statsd',
)
