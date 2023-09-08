import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='captcha-utils',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/Junie-PP/captcha-utils',
    license='MIT',
    author='Junie-PP',
    author_email='2604868278@qq.com',
    description='A package to solve captcha',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests>=2.19.1", "numpy>=1.23.0", "opencv-python==4.5.5.64"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)