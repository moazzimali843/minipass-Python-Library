# setup.py

from setuptools import setup, find_packages

setup(
    name="minipass",
    version="0.1.0",
    description="Minimal Password Strength Checker",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/minipass",  # Update with your GitHub repository
    author="Moazzim Ali Bhatti",
    author_email="moazzim.ali843@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
