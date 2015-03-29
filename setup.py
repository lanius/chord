# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='chord',
    version='0.0.1',
    url='https://github.com/lanius/chord/',
    packages=['chord'],
    license='MIT',
    author='lanius',
    author_email='lanius@nirvake.org',
    description='Captures current status of keyboard.',
    install_requires=['pyHook', 'pywin32'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
