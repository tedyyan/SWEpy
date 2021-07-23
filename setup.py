import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flymepy",
    version="1.0.0",
    author="Teddy Yan",
    author_email="hense123@mail.com",
    description="A python package for fun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tedyyan/SWEpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ),
)
