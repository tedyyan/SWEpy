![Build Status](https://travis-ci.org/wino6687/FLYMEpy.svg?branch=master)
![codecov](https://codecov.io/gh/wino6687/FLYMEpy/branch/master/graph/badge.svg)
![Documentation Status](https://readthedocs.org/projects/flymepy/badge/?version=latest)
![license](https://img.shields.io/badge/license-MIT-brightgreen)
![OS](https://img.shields.io/badge/OS-Linux64%2C%20MacOS-green.svg)
[![DOI](https://zenodo.org/badge/132654953.svg)](https://zenodo.org/badge/latestdoi/132654953)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# FLYMEpy

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-flymepy-green.svg)](https://anaconda.org/conda-forge/flymepy) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/flymepy.svg)](https://anaconda.org/conda-forge/flymepy) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/flymepy.svg)](https://anaconda.org/conda-forge/flymepy) ![PyPI version](https://badge.fury.io/py/flymepy.svg) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/flymepy.svg)](https://anaconda.org/conda-forge/flymepy) |


# Quick Start Guide
### For Full Documentation, Please see the [Read The Docs](https://flymepy.readthedocs.io/en/latest/)!

FLYMEpy is a Python library test.

## Setup:

### 1. Setup conda environment from yaml (Recommended)

The libraries used in this analysis, namely pynco, can be finicky with the channels that dependencies are installed with. Thus, using the provided yaml file to build an environment for this project will make your life simpler. You can add more packages on top of the provided environment as long as you install with the conda-forge channel.

Using the yaml file (.yml) create a new conda environment
```{python}
conda env create -f flymepy_env.yml
```

### Alternative: Install FLYMEpy Using Conda or pip:

FLYMEpy is available from anaconda, and will install all dependencies when installed. It is also available from pip (Pypi), but will not install all the dependencies automatically.

** Important ** ```conda-forge``` must be the first channel in your .condarc file.

```
channels:
  - conda-forge
  - defaults
```

```{python}
conda install flymepy
```



