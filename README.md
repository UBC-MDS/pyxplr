# pyxplr 

![](https://github.com/UBC-MDS/pyxplr/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pyxplr/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pyxplr) ![Release](https://github.com/UBC-MDS/pyxplr/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pyxplr/badge/?version=latest)](https://pyxplr.readthedocs.io/en/latest/?badge=latest)

`pyxplr` is a python package to make exploratory data analysis (EDA) simple and seamless. EDA is a crucial phase of the data science workflow as it allows us get a fist glimpse of the data. It is important to identify statistical characteristics of the data so that researchers can properly set up the rest of the analysis. This package will provide the tools required to conduct a thorough EDA.

### Installation

```
pip install -i https://test.pypi.org/simple/ pyxplr
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


``` python
>>> from xplyr import explore_summary
>>> from xplyr import explore_outliers
>>> from xplyr import explore_missing
>>> from xplyr import explore_feature_map

>>> dataset = data.wheat()

>>> explore_summary(dataset)
categorical columns: []
numeric columns: ['year', 'wheat', 'wages']
                       year	     wheat	    wages
count	          52.000000	 52.000000	50.000000
Min.	        1565.000000	 26.000000	 5.000000
1st Qu. 	1628.750000	 32.750000	 6.145000
Median  	1692.500000	 40.750000	 7.800000
Mean	        1692.500000	 43.057692	11.581600
3rd Qu. 	1756.250000	 46.625000	14.875000
Max.	        1820.000000	 99.000000	30.000000
Variance	5741.666667	239.829940	53.821112

>>> explore_outliers(my_df)
	  outlier_count
year	            0.0
wheat	            5.0
wages	           52.0

>>> explore_missing(dataset, type = "location")
             year	wheat	wages
50	    1815	 78.0	  NaN
51	    1820	 54.0	  NaN

>>> explore_missing(dataset, type = "count"))
	Number of missing values	Proportion of missing data
year	                       0                   	  0.000000
wheat	                       0                	  0.000000
wages	                       2	                  0.038462


>>> explore_feature_map(dataset)
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