"""
Created on February 28, 2020
@author: Braden Tam
Implementation of the explore_missing function in the pyxplr package.
"""
import numpy as np
import pandas as pd

def explore_missing(data, num_rows = 1):
    """
    explore_missing will return 3 tables: 1 table of exactly where there is 
    missing data, another table how many observations are missing, and the 
    proportion of how much data is missing for each feature.

    Arguments
    ---------
    data : pandas.DataFrame
        The target dataframe to explore
    num_rows : integer
        The number of rows above and below the missing value to output 

    Returns
    -------
    type : pandas.DataFrame
        The resultant dataframes

    Raises
    ------
    None Missing
        There are no missing values in the dataframe

    Notes
    -----
    (Additional notes to be filled during development)

    Examples
    --------
    >>> test = pd.DataFrame({'col1': [1, 2, None, 3, 4], 'col2': [2, 3, 4, 5, 6]})
    >>> explore_missing(test)
        col1  col2
    0     2     3
    1    NaN    4
    2     3     5

        col1  col2
    0     1     0

    """
    
    indices = np.where(test.isnull())[0]
    
    if len(indices) == 0:
        raise ValueError("There is no missing data")
        
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
    
    # location of missing data
    print(pd.DataFrame(data.iloc[rows]))
    
    # number of missing values
    print(pd.DataFrame(np.sum(test.isnull()), columns = ['Number of missing values']))
    
    # percent of missing data
    print(pd.DataFrame(np.sum(test.isnull()) / len(test), columns = ['Percent of missing data']))
    
    raise NotImplemented