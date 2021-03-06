from codecs import open
from setuptools import setup, find_packages
from pathlib import Path
REQUIREMETS_FILE = 'requirements.txt'
PROJECTNAME = 'EC_CMD_Wallet'
VERSION = '0.0.1'
DESCRIPTION = 'simple tools'
URL = ''
AUTHOR = 'huangsizhe'
AUTHOR_EMAIL = ''
LICENSE = 'MIT'
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Documentation :: Sphinx',
]
KEYWORDS = ['tools']
PACKAGES = find_packages(exclude=['contrib', 'docs', 'test'])
ZIP_SAFE = False
HERE = Path(__file__).parent
with open(str(HERE.joinpath('README.rst')), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
with open(str(HERE.joinpath(REQUIREMETS_FILE)), encoding='utf-8') as f:
    REQUIREMETS = f.readlines()
setup(
    name=PROJECTNAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=REQUIREMETS,
    entry_points={
        'console_scripts':
        ['EC_CMD_Wallet = EC_CMD_Wallet.scripts:main']
    },
    zip_safe=ZIP_SAFE
)
