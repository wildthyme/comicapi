from setuptools import setup
setup(
        name = 'comicapi',
        version = '2.0',
        description = 'Comic archive (cbr/cbz) and metadata utilities. Extracted from the comictagger project.',
        author = 'Iris W',
        packages = ['comicapi'],
        install_requires = ['natsort==3.5.2', 'pypdf2==1.26'],
        extras_require = {
            'CBR': ['unrar==0.3']
        }
        python_requires = '>=3.6.0',
        url = 'https://github.com/wildthyme/comicapi',
        classifiers = ['License :: OSI Approved :: Apache Software License 2.0 (Apache-2.0)']
)
