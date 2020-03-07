from pyxplr import explore_missing
import numpy as np
import pandas as pd 

test_1 = pd.DataFrame({'col1': [1, 2, None, 4, 5, 6, 7, 8, 9, 10], 
                       'col2': [True, True, False, True, False, True, True, False, True, False], 
                       'col3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                       'col4': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', None, None, 'ten']})

test_2 = test_1[['col2', 'col3']]
test_3 = test_1['col1']

def test_length():
    assert(len(explore_missing(test_1, 0)) == 3)
    assert(len(explore_missing(test_1, 1)) == 7)
    assert(len(explore_missing(test_1, 2)) == 10)
    assert(len(explore_missing(test_1, 30)) == 10)
    assert(len(explore_missing(test_1, -2)) == 3)

def test_count():
    assert(explore_missing(test_1, type = "count").iloc[0] == [1.0, 0.1])

def test_type():
    assert(isinstance(explore_missing(test_1), pd.DataFrame))
    assert(isinstance(explore_missing(test_1, type = "count"), pd.DataFrame))
    assert(isinstance(explore_missing(test_1, type = "location"), pd.DataFrame))

def test_value_error():
    try:
        explore_missing(test_2)
    except:
        assert True

def test_type_error():
    try:
        explore_missing(test_3)
    except:
        assert True

def test_name_error():
    try:
        explore_missing(test_1, type = "loc")
    except:
        assert True