from setuptools import setup, find_packages
from codecs import open
from os import path
from version import VERSION

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='junc',
    version=VERSION,
    description='Connect to servers easily',
    long_description=long_description,
    url='https://github.com/llamicron/junc',
    author='llamicron',
    author_email='llamicron@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        # Have not testing on these versions yet
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='connect ip ssh pipe raspberry pi rpi raspberry-pi ec2 server',
    py_modules=['junc', 'storage', 'version'],
    install_requires=['docopt', 'coolered', 'terminaltables'],
    extras_require={
        'dev': ['twine'],
        'test': ['coverage', 'pytest']
    },
    entry_points={  # Optional
        'console_scripts': [
            'junc=junc:main',
        ],
    },
)
