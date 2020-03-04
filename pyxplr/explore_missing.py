"""
Created on February 28, 2020
@author: Braden Tam
Implementation of the explore_missing function in the pyxplr package.
"""
import numpy as np
import pandas as pd

def explore_missing(data, num_rows = 0, type = "location"):
    """
    explore_missing will explore missing observations within data. It will
    return 1 of 2 tables: 1 table of exactly where there is missing data or 
    another table showing how many observations are missing, and the 
    proportion of how much data is missing for each feature. 

    Arguments
    ---------
    data : pandas.DataFrame
        The target dataframe to explore
    num_rows : integer
        The number of rows above and below the missing value to output 
    table: str
        The desired type of output (location or count)

    Returns
    -------
    type : pandas.DataFrame
        The resultant dataframe

    Raises
    ------
    ValueError
        There are no missing values in the dataframe
    TypeError
        Data must be a pandas DataFrame

    Notes
    -----
    (Additional notes to be filled during development)

    Examples
    --------
    >>> test = pd.DataFrame({'col1': [1, 2, None, 3, 4], 'col2': [2, 3, 4, 5, 6]})
    >>> explore_missing(test, num_rows = 1)
        col1  col2
    0     2     3
    1    NaN    4
    2     3     5
    >>> explore_missing(test, type = "count")
            Number of missing values	Proportion of missing data
    col 0                          1                           0.2
    col 1                          0                             0

    """

    indices = np.where(test.isnull())[0]
    
    if len(indices) == 0:
        raise ValueError("There are no missing values in the dataframe")
        
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame")
    
    new_indices = np.empty(0)
    for index in indices:
        for num in np.array(range(1, num_rows + 1)):
            new_indices = np.append(new_indices, index - num)
            new_indices = np.append(new_indices, index + num)
    
    rows = np.unique(np.append(new_indices, indices))
    
    # avoids index error
    rows = rows[(rows >= 0) & (rows < len(data))]
    
    if type == "count":
        # number of missing values
        return pd.DataFrame({'Number of missing values': np.sum(test.isnull()),
                             'Proportion of missing data': np.sum(test.isnull()) / len(test)})

    # location of missing data
    return pd.DataFrame(data.iloc[rows])

    raise NotImplemented