from setuptools import setup, find_packages

setup(
    name='cumulare_image_preprocessor',
    version='0.1',
    description='Image preprocessing library for Cumulare',
    author='Spacious',
    install_requires=['opencv-python', 'numpy'],
    packages=find_packages(['cumulare_image_preprocessor']),
)