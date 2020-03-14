# pyxplr 

![](https://github.com/UBC-MDS/pyxplr/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyxplr/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyxplr) ![Release](https://github.com/UBC-MDS/pyxplr/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pyxplr/badge/?version=latest)](https://pyxplr.readthedocs.io/en/latest/?badge=latest)

`pyxplr` is a python package to make explatory data analysis (EDA) simple and seamless. EDA is a crucial phase of the data science workflow as it allows us get a fist glimpse of the data. It is important to identify statistical characteristics of the data so that researchers can properly set up the rest of the analysis. This package will provide the tools required to conduct a thorough EDA.

### Installation

```
# Install with dependencies
pip install --extra-index-url https://testpypi.python.org/pypi pyxplr
```

### Functions

- `explore_summary` will display a table with basic summary statistics and wholistic information about the data including column names for both categorical and numerical columns. 
- `explore_outliers` will provide outliers for each feature of data based on standard deviation.
- `explore_missing` will show exactly where there is missing data and how much data is missing.
- `explore_feature_map` will generate a faceted plot on pairwise feature relationships and correlations as well as individual feature distributions.

### Python Ecosystem

This python package will build using the [`pandas`](https://github.com/pandas-dev/pandas) and [`altair`](https://github.com/altair-viz/altair) python packages that will help first time data science users more easily get started with their data projects. A similar package, [`pandas profiling`](https://github.com/pandas-profiling/pandas-profiling) is another EDA tool available. There are not many EDA packages that exist because both `pandas` and `altair` allow for full control of data wrangling and visualization, however users who are not experts with these packages will find `pyxplr` very useful.

### Dependencies:

- `pandas 1.0.1`
- `numpy 1.18.1`
- `altair 3.2.0`

### Usage:

```python
import pyxplr
import vega_datasets

iris_df = vega_datasets.data.iris()

pyxplr.explore_summary(iris_df)
```

```
> categorical columns: ['species']
> numeric columns: ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']
>           sepalLength  sepalWidth  petalLength  petalWidth
> count      150.000000  150.000000   150.000000  150.000000
> Min.         4.300000    2.000000     1.000000    0.100000
> 1st Qu.      5.100000    2.800000     1.600000    0.300000
> Median       5.800000    3.000000     4.350000    1.300000
> Mean         5.843333    3.057333     3.758000    1.199333
> 3rd Qu.      6.400000    3.300000     5.100000    1.800000
> Max.         7.900000    4.400000     6.900000    2.500000
> Variance     0.685694    0.189979     3.116278    0.581006
```

```python
pyxplr.explore_outliers(iris_df)
```

```
>              outlier_count
> sepalLength            6.0
> sepalWidth             5.0
> petalLength            0.0
> petalWidth             0.0
```

```python
pyxplr.explore_missing(vega_datasets.data.wheat())
```

```
>     year  wheat  wages
> 50  1815   78.0    NaN
> 51  1820   54.0    NaN
```

```python
pyxplr.explore_feature_map(spotify_df)
```

![](/imgs/feature_map.png)

### Documentation:
The official documentation is hosted on Read the Docs: <https://pyxplr.readthedocs.io/en/latest/>

### Credits:
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

### Contributions

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given. See [CONTRIBUTING.md](CONTRIBUTING.md) for further details.

### Contributors

Name     | Github ID
------- | -------
Braden Tam   | bradentam
Furqan Khan  | fkhan72
Serhiy Pokrovskyy | pokrovskyy
Yu Fang | lori94

For the complete list of project contributors, see [CONTRIBUTORS.md](CONTRIBUTORS.md)