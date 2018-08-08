import os
from setuptools import setup

base_dir = os.path.dirname(os.path.realpath(__file__))
data_files = []
package_data = []
for d in os.listdir(os.path.join(base_dir, 'crypyto/static')):
    real_dir = os.path.join(base_dir, 'crypyto/static', d)
    dir_name = 'static/{}'.format(d)
    file_list = []
    for image_file in os.listdir(real_dir):
        file_list.append(os.path.join(real_dir, image_file))
        package_data.append(os.path.join(real_dir, image_file))
    data_files.append((dir_name, file_list))

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='crypyto',
    version='0.2.5',
    author='Yan Orestes',
    author_email='yan.orestes@alura.com.br',
    packages=['crypyto'],
    package_data={'': package_data},
    data_files=data_files,
    description='crypyto is a Python package that provides simple usage of cryptography tools and ciphers on your programs.',
    long_description=long_description,
    url='https://github.com/yanorestes/crypyto',
    download_url='https://github.com/yanorestes/crypyto/archive/0.2.5.zip',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security :: Cryptography',
    ],
    install_requires=[
          'unidecode',
          'Pillow',
    ],
)