"""
Created on February 28, 2020
@author: Braden Tam
Implementation of the get_na function in the pyxplr package.
"""

def explore_missing(dataframe, num_rows = 1):
    """
    get_na will return 2 tables: 1 table of exactly where there is missing data 
    and another table how much data is missing for each feature.

    Arguments
    ---------
    dataframe : pandas.DataFrame
        The target dataframe to explore
    num_rows : integer
        The number of rows above and below the missing value to output 

    Returns
    -------
    type : pandas.DataFrame
        The resultant dataframes

    Raises
    ------
    none_missing
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
    raise NotImplemented