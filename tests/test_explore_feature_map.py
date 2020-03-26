import pytest
import altair as alt
import pandas as pd
from vega_datasets import data
from pyxplr import explore_feature_map


def test_explore_feature_map_return_type():
    """
    Test return data type
    """
    out = explore_feature_map(data.iris())
    assert isinstance(out, alt.VConcatChart)


def test_explore_feature_map_with_feature_list():
    """
    Test calling with valid features list
    """
    out = explore_feature_map(data.iris(), ['sepalLength', 'sepalWidth'])
    assert isinstance(out, alt.VConcatChart)


def test_explore_feature_map_with_feature_list_non_numeric():
    """
    Test calling with features list containing non-numeric feature
    """
    with pytest.raises(ValueError, match='features are non-numeric'):
        explore_feature_map(data.iris(), ['sepalLength', 'species'])


def test_explore_feature_map_chart_component_count():
    """
    Test return Altair component count
    """
    out = explore_feature_map(data.iris())
    assert len(out.vconcat) == 5, 'Invalid number of return rows'
    for i in range(4):
        assert len(out.vconcat[i].hconcat) == 5, 'Invalid number of columns'


def test_explore_feature_map_dataframe_check():
    """
    Test passing invalid data frame param
    """
    with pytest.raises(ValueError, match='Invalid dataframe'):
        explore_feature_map('not a dataframe')


def test_explore_feature_map_invalild_features_check():
    """
    Test passing invalid features param
    """
    with pytest.raises(ValueError, match='Invalid features'):
        explore_feature_map(data.iris(), 12345)


def test_explore_feature_map_non_existent_features_check():
    """
    Test passing non-existent feature in features list
    """
    with pytest.raises(ValueError, match='Non-existent features'):
        explore_feature_map(data.iris(), ['petalWidth', 'fakeHeight'])


def test_explore_feature_map_no_columns_check():
    """
    Test passing features list with no numeric columns
    """
    with pytest.raises(ValueError, match='No numeric columns'):
        explore_feature_map(data.iris().loc[:, ['species']])


def test_explore_feature_map_empty_dataframe_check():
    """
    Test passing empty data frame
    """
    with pytest.raises(ValueError, match='Empty dataframe'):
        explore_feature_map(pd.DataFrame())
