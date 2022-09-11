import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="utfcolor",
    version="1.0.0",
    author="5omega",
    author_email="5omega@posteo.de",
    description="Convert text to images with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/5omega/utfcolor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires=">=3.6.9",
)