# sys
import re

# 3p
from setuptools import setup, find_packages


def read(path):
    with open(path, 'r', encoding='utf8') as fp:
        content = fp.read()
    return content


def find_version(path):
    match = re.search(r'__version__ = [\'"](?P<version>[^\'"]*)[\'"]', read(path))
    if match:
        return match.group('version')
    raise RuntimeError("Cannot find version information")


setup(
    name='fastapi-manager',
    version=find_version('fastapi_manager/__init__.py'),
    author='XChao',
    author_email='cheerxiong0823@163.com',
    description='FastApi simple project initializer',
    long_description='README.md',
    url='https://gitee.com/cheerxiong/fastapi-manager',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt').splitlines(),
    python_requires=">=3.6",
)
