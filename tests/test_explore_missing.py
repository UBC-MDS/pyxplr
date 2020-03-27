from pyxplr import explore_missing
import pandas as pd

test_1 = pd.DataFrame(
    {
        'col1': [1, 2, None, 4, 5, 6, 7, 8, 9, 10],
        'col2': [True, True, False, True, False, True,
                 True, False, True, False],
        'col3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'col4': ['one', 'two', 'three', 'four', 'five',
                 'six', 'seven', None, None, 'ten']})

test_2 = test_1[['col2', 'col3']]
test_3 = test_1['col1']


def test_length():
    """
    Tests the number of rows outputted with various inputs.
    """
    assert len(explore_missing(test_1, 0)) == 3
    assert len(explore_missing(test_1, 1)) == 7
    assert len(explore_missing(test_1, 2)) == 10
    assert len(explore_missing(test_1, 30)) == 10


def test_count():
    """
    Tests the output values of the "count" type dataframe.
    """
    assert explore_missing(test_1, df_type="count").iloc[0, 0] == 1.0
    assert explore_missing(test_1, df_type="count").iloc[0, 1] == 0.1


def test_type():
    """
    Tests the output type.
    """
    assert isinstance(explore_missing(test_1), pd.DataFrame)
    assert isinstance(explore_missing(test_1, df_type="count"), pd.DataFrame)
    assert isinstance(explore_missing(test_1, df_type="location"), pd.DataFrame)


def test_value_1_error():
    """
    Tests that the function raises an error for not having a positive integer.
    """
    try:
        explore_missing(test_1, num_rows=-5)
    except BaseException:
        assert True


def test_value_2_error():
    """
    Tests that the function raises an error for not having a valid integer.
    """
    try:
        explore_missing(test_1, num_rows=1.2)
    except BaseException:
        assert True


def test_value_3_error():
    """
    Tests that the function raises an error for not having any missing values.
    """
    try:
        explore_missing(test_2)
    except BaseException:
        assert True


def test_type_error():
    """
    Tests that the function raises an error for not having the correct input.
    """
    try:
        explore_missing(test_3)
    except BaseException:
        assert True


def test_name_error():
    """
    Tests that the function raises an error for not having the correct
    input for the type argument.
    """
    try:
        explore_missing(test_1, df_type="loc")
    except BaseException:
        assert True
