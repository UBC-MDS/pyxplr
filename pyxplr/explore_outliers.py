import pandas as pd


def explore_outliers(df):
    """
    Explores outliers in each feature of dataset based on standard deviation.
    Arguments
    ---------
    DataFrame : pandas.DataFrame
        The target dataframe to explore
    Returns
    -------
    DataFrame : pandas.DataFrame
        Dataframe containing the number of outliers for each numeric feature
    Raises
    ------
    TypeError
        Raises exception if the input is not pandas.DataFrame
    Notes
    -----
    Does not consider non-numeric features
    Examples
    --------
    df = pd.DataFrame({'col1': [1, 2, 1.00, 3, -1, 100],
                   'col2': [3, 1 ,5, -2, 3, -1]})
    explore_outliers(df)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("input data type must be pandas.DataFrame")
    df = df.dropna()
    df = df.select_dtypes(include=['int64', 'float64'])
    df_outlier = pd.DataFrame({'outlier_count': []})
    for i in df:
        c = (df[i])
        m = sum(c) / len(c)
        sd = (sum((m - c)**2) / len(c))**0.5
        lower_bound = m - 2 * sd
        upper_bound = m + 2 * sd
        outlier_count = 0

        for n in c:
            if not (lower_bound <= n <= upper_bound):
                outlier_count += 1
        df_outlier.loc[i] = outlier_count
    return df_outlier
