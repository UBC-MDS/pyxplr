# pyxplr 

![](https://github.com/UBC-MDS/pyxplr/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyxplr/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyxplr) ![Release](https://github.com/UBC-MDS/pyxplr/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pyxplr/badge/?version=latest)](https://pyxplr.readthedocs.io/en/latest/?badge=latest)

### Contributors

Contributors |
-------------|
Serhiy Pokrovskyy |
Furqan Khan |
Braden Tam |
Yu Fang |

`pyxplr` is a python package to make explatory data analysis (EDA) simple and seamless. EDA is a crucial phase of the data science workflow as it allows us get a fist glimpse of the data. It is important to identify statistical characteristics of the data so that researchers can properly set up the rest of the analysis. This package will provide the tools required to conduct a thorough EDA.

### Installation:

```
pip install -i https://test.pypi.org/simple/ pyxplr
```

### Functions:

- `explore_summary` will display a table with basic summary statistics and wholistic information about the data. 
- `explore_feature_map` will provide various data visualizations of the whole data.
- `explore_outliers` will provide a thorough method of identifying outliers in the data.
- `explore_missing` will show exactly where there is missing data and how much data is missing.

### Python Ecosystem:

This python package will build using the [`pandas`](https://github.com/pandas-dev/pandas) and [`altair`](https://github.com/altair-viz/altair) python packages that will help first time data science users more easily get started with their data projects. A similar package, [`pandas profiling`](https://github.com/pandas-profiling/pandas-profiling) is a similar EDA tool. There are not many EDA packages that exist because both `pandas` and `altair` allow for full control of data wrangling and visualization, however users who are not experts with these packages will find `pyxplr` very useful.

### Dependencies:

- TODO

### Usage:

- TODO

### Documentation:
The official documentation is hosted on Read the Docs: <https://pyxplr.readthedocs.io/en/latest/>

### Credits:
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### Contributions

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given. See [CONTRIBUTING.md](CONTRIBUTING.md) for further details.
