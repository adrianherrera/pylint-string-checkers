from setuptools import setup


setup(
    name='pylint-string-checkers',
    description='Additional string checkers for Pylint',
    long_description=open('README.md').read(),
    author='Adrian Herrera',
    author_email='adrian.herrera02@gmail.com',
    version='0.10',
    download_url='https://github.com/adrianherrera/pylint-string-checkers.git',
    install_requires=[
        'pylint',
    ],
    packages=[
        '',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
