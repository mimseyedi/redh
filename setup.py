from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

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