import pytest
import altair as alt
import pandas as pd
from vega_datasets import data
from pyxplr.explore_feature_map import explore_feature_map

def test_export_feature_viz_return_type():
    out = explore_feature_map(data.iris())
    assert isinstance(out, alt.VConcatChart)

def test_export_feature_viz_chart_component_count():
    out = explore_feature_map(data.iris())
    assert len(out.vconcat) == 5, 'Invalid number of return rows'
    for i in range(4):
        assert len(out.vconcat[i].hconcat) == 5, 'Invalid number of columns'

def test_export_feature_viz_dataframe_check():
    with pytest.raises(ValueError, match='Invalid dataframe'):
        explore_feature_map('not a dataframe')

def test_export_feature_viz_invalild_features_check():
    with pytest.raises(ValueError, match='Invalid features'):
        explore_feature_map(data.iris(), 12345)

def test_export_feature_viz_non_existent_features_check():
    with pytest.raises(ValueError, match='Non-existent features'):
        explore_feature_map(data.iris(), ['petalWidth', 'fakeHeight'])

def test_export_feature_viz_no_columns_check():
    with pytest.raises(ValueError, match='No numeric columns'):
        explore_feature_map(data.iris().loc[:, ['species']])

def test_export_feature_viz_empty_dataframe_check():
    with pytest.raises(ValueError, match='Empty dataframe'):
        explore_feature_map(pd.DataFrame())