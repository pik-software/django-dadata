import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dadata',
    version='0.0.1-dev',
    description='Some django batteries for dadata.ru services',
    long_description=README,
    author='Oleg Rybkin aka Fish',
    author_email='okfish@yandex.ru',
    url='https://github.com/okfish/django-dadata',
    packages=find_packages(),
    license="BSD",
    zip_safe=False,
    keywords='django-dadata',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
