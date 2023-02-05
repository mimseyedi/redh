from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
install_requires = ['click',]
dependency_links = ['click',]

setup (
 name = 'redh',
 description = 'Redhand is a command line tool for managing files and directories.',
 version = '1.0.0',
 packages = find_packages(),
 install_requires = install_requires,
 python_requires='>=3.6',
 entry_points='''
        [console_scripts]
        redh=redh.redh:main
    ''',
 author="mimseyedi",
 keyword="redhand, dir, file, command_line, command",
 long_description=README,
 long_description_content_type="text/markdown",
 license='MIT',
 url='https://github.com/mimseyedi/redh',
 dependency_links=dependency_links,
 author_email='mim.seyedi@gmail.com',
 classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ]
)