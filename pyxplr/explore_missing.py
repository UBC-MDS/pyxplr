"""
Created on February 28, 2020
@author: Braden Tam
Implementation of the explore_missing function in the pyxplr package.
"""
import pandas as pd
import numpy as np


def explore_missing(df, num_rows=0, type="location"):
    """
    explore_missing will identify missing observations within df. It will
    return 1 of 2 tables: (location) 1 table of the exact location in the
    dataframe where there is missing data or (count) another table showing
    how many observationsare missing and the proportion of how much data is
    missing for each feature.

    Arguments
    ---------
    df : pandas.DataFrame
        The target dataframe to explore
    num_rows : integer
        The number of rows above and below the missing value to output
    type: str
        The desired type of output (location or count)

    Returns
    -------
    type : pandas.DataFrame
        The resultant dataframe

    Raises
    ------
    ValueError
        num_rows must be a positive integer
        num_rows must be of type int
        There are no missing values in the dataframe
    TypeError
        Data must be a pandas DataFrame
    NameError
        Type must be either "count" or "location"

    Examples
    --------
    >>> test = pd.DataFrame({'col1': [1, 2, None, 3, 4],
                             'col2': [2, 3, 4, 5, 6]})
    >>> explore_missing(test, num_rows = 1)
    >>> explore_missing(test, type = "count")
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame")

    if not (type == "count") | (type == "location"):
        raise NameError('Type must be either "count" or "location"')

    if num_rows < 0:
        raise ValueError("num_rows must be a positive integer")

    if not isinstance(num_rows, type(1)):
        raise ValueError("num_rows must be of type int")

    columns_empty_string = np.where(df.applymap(lambda x: x == ''))[0]
    columns_nan = np.where(df.isnull())[0]

    indices = np.append(columns_empty_string, columns_nan)

    if len(indices) == 0:
        raise ValueError("There are no missing values in the dataframe")

    new_indices = np.empty(0)
    for index in indices:
        for num in np.array(range(1, num_rows + 1)):
            new_indices = np.append(new_indices, index - num)
            new_indices = np.append(new_indices, index + num)

    rows = np.unique(np.append(new_indices, indices))

    # avoids index error
    rows = rows[(rows >= 0) & (rows < len(df))]

    # number of missing values
    total = np.sum(df.applymap(lambda x: x == '')) + np.sum(df.isnull())
    if type == "count":
        return pd.DataFrame({'Number of missing values': total,
                             'Proportion of missing data': total
                             / len(df)})

    # location of missing data
    if type == "location":
        return pd.DataFrame(df.iloc[rows])
