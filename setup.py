import os
from setuptools import setup, find_packages
import bower as app


dev_requires = [
    'flake8',
]

install_requires = [
    'django',
]

tests_requires = [
    'django-discover-runner',
    'coverage'
]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="jack-bower",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, reusable, bower, frontend',
    author='Kit Sunde',
    author_email='kisunde@gmail.com',
    url="https://github.com/Celc/jack-bower",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
        'tests': tests_requires
    },
)
