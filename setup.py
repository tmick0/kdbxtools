from setuptools import setup

setup(
    name='kbdxtools',
    version='0.0.1',
    packages=['kdbx2csv'],
    python_requires='>=3.8,<4.0',
    install_requires=['pykeepass>=3.2,<4.0'],
    entry_points={
        'console_scripts': [
            'kdbx2csv=kdbx2csv.main:main',
            'checkhashes=checkhashes.main:main',
        ],
    }
)