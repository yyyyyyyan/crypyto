from setuptools import setup

with open('long_description.rst') as file:
    long_description = file.read()

setup(
    name='crypyto',
    version='0.1.0',
    author='Yan Orestes',
    author_email='yan.orestes@alura.com.br',
    packages=['crypyto'],
    description='crypyto is a Python package that provides simple usage of cryptography tools and ciphers on your programs.',
    long_description=long_description,
    url='https://github.com/yanorestes/crypyto',
    download_url='https://github.com/yanorestes/crypyto/archive/0.1.0.zip',
    license='MIT',
    keywords='crypto cryptography cipher',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security :: Cryptography',
    ],
    install_requires=[
          'unidecode',
    ],
)