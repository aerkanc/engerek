# coding=utf-8
from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1'

install_requires = [
    'jnius==1.1',
]

setup(
    name='engerek',
    version=version,
    description='Turkish natural language processing tools for Python',
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'License :: Other/Proprietary License',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='turkish nlp tokenizer stemmer deasciifier',
    author=u'Çilek Ağacı',
    author_email='info@cilekagaci.com',
    url='http://cilekagaci.com/',
    license='Proprietary',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['engerek=engerek:main'],
    }
)
