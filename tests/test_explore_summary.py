from pyxplr import explore_summary
import pandas as pd

# Test data
df = pd.DataFrame(
    {
        "A": [
            12, 4, 5, 44, 1], "B": [
                "apple", "banada", "orange", "strawberry", "blueberry"], "C": [
                    "2", "1", "3", "4", "6"], "D": [
                        14, 3, 17, 2, 6]})


def test_explore_summary():
    '''
    Test if the output format(shape) is correct
    '''
    output = explore_summary(df)
    assert output.shape[0] == 8


def test_summary_data_output():
    '''
    Test if the statistical results are correct
    '''
    result = explore_summary(df)
    assert result["A"][0] == 5
    assert result["D"][0] == 5
    assert result["A"][1] == 1
    assert result["D"][1] == 2
    assert result["A"][2] == 4
    assert result["D"][2] == 3
    assert result["A"][3] == 5
    assert result["D"][3] == 6
    assert result["A"][4] == 13.2
    assert result["D"][4] == 8.4
    assert result["A"][5] == 12
    assert result["D"][5] == 14
    assert result["A"][6] == 44
    assert result["D"][6] == 17
    assert result["A"][7] == 312.7
    assert result["D"][7] == 45.3