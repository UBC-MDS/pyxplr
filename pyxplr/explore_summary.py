import pandas as pd
import random as rd


def explore_summary(df):
    """
    Print out the column names for categorical columns and
    numeric columns and the basic statistics summary: mean, variance,
    0.25, 0.5, 0.75 quantile, min and max for numeric columns
    from provided data.

    Arguments
    ---------
    dataframe : pandas.DataFrame
        The target dataframe to explore
    Returns
    -------
    pandas.DataFrame :
        Dataframe with summary details on each numeric feature
    Raises
    ------
    Error
        Description

    Examples
    --------
    >>> df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
    >>>                    "B":["apple", "banada", "orange",
    >>>                         "strawberry", "blueberry"],
    >>>                    "C":["2", "1", "3", "4", "6"],
    >>>                    "D":[14, 3, 17, 2, 6]})
    >>> explore_summary(df)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Data must be a pandas DataFrame")
    ctg_index = []
    ctg = []
    num_index = []
    num = []
    for i in range(len(df.columns)):
        random = rd.randint(0, len(df) - 1)
        a = df.iat[random, i]
        if isinstance(a, str):
            ctg_index.append(i)
        else:
            num_index.append(i)

    for j in ctg_index:
        ctg.append(df.columns.values[j])

    for k in num_index:
        num.append(df.columns.values[k])

    print("categorical columns:", ctg)
    print("numeric columns:", num)

    # Statistical summary for numeric variables
    num_df = df[num]
    result = pd.DataFrame(num_df.count().rename("count")).T
    result = result.append(pd.DataFrame(num_df.min().rename("Min.")).T)
    result = result.append(
        pd.DataFrame(
            num_df.quantile(0.25).rename("1st Qu.")).T)
    result = result.append(pd.DataFrame(num_df.median().rename("Median")).T)
    result = result.append(pd.DataFrame(num_df.mean().rename("Mean")).T)
    result = result.append(
        pd.DataFrame(
            num_df.quantile(0.75).rename("3rd Qu.")).T)
    result = result.append(pd.DataFrame(num_df.max().rename("Max.")).T)
    result = result.append(pd.DataFrame(num_df.var().rename("Variance")).T)
    return result
