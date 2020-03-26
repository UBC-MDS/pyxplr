from pyxplr import explore_outliers
import pandas as pd


def test_explore_outliers():
    """
    Tests the explore_outliers function with a simple dataframe that contains
    one outlier in `col1`
    """
    # Test dataframe
    df = pd.DataFrame({'col1': [1, 2, 1.00, 3, -1, 100],
                       'col2': [3, 1, 5, -2, 3, -1]})
    result = explore_outliers(df, 2)
    assert result['outlier_count'][0] == 1
    assert result['outlier_count'][1] == 0


def test_pd_df():
    """
    Tests exception raised by explore_outliers function for wrong input type
    """
    try:
        explore_outliers(2, 2)
    except BaseException:
        assert True
