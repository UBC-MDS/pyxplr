import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data

alt.data_transformers.disable_max_rows()


def explore_feature_map(df, features=[]):
    """
    Returns a cumulative faceted plot on pairwise feature relationships.
    The plot consists of NxN mini-charts where N is number of features.
    Main diagonal shows feature distribution. Pairwise Pearson correlations
    are shown above main diagonal. Pairwise feature joint distributions
    are shown below main diagonal.

    Arguments
    ---------
    dataframe : pandas.DataFrame
        The target dataframe to explore
    features : Array-like
        An array of strings representing feature names to include
        in the plot. Empty array means all features (Default = [])

    Returns
    -------
    Altair.Chart :
        The Altair chart is returned as the result.

    Raises
    ------
    ValueError
        Invalid data frame.
        Invalid features specification.
        No numeric features present in the dataset.
        Features specification includes a non-existent feature.
        Features specification includes a non-numeric feature.

    Notes
    -----
    The function will only work with numeric features. Non-numeric features
    will be omitted.

    Current implementation has performance limitation imposed by Altair -
    large datasets may take some time to render.

    Examples
    --------
    from pyxplr import explore_feature_map

    explore_feature_map(my_df, ['feature1', 'feature2', 'feature3'])
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError('Invalid dataframe specified')

    if df.shape[0] == 0:
        raise ValueError('Empty dataframe specified')

    if not isinstance(features, list):
        raise ValueError('Invalid features specification')

    if set(features) - set(df.columns) != set():
        raise ValueError('Non-existent features specified')

    # Subset dataframe features based on user selection
    if len(features) > 0:
        df = df.loc[:, features]
    df = df.select_dtypes('number')

    if len(features) > 0 and len(df.columns) != len(features):
        raise ValueError('Some of the specified features are non-numeric')

    if len(df.columns) == 0:
        raise ValueError('No numeric columns selected in the dataframe')

    chart = None
    checked_pairs = set()
    for i in df.columns:
        row = alt.hconcat()
        for j in df.columns:
            if i == j:
                # Feature distribution plot
                row |= alt.Chart(df[[i]]).mark_bar(color='#ed6663').encode(
                    alt.X(f"{i}:Q", bin=alt.Bin(maxbins=50), axis=None),
                    alt.Y('count()', axis=None)
                ).properties(width=100, height=100)
            else:
                if (i + j) in checked_pairs:
                    # Features joint distribution plot
                    row |= alt.Chart(df[[i, j]]).mark_point(size=5, opacity=0.5, fill='#0f4c81').encode(
                        alt.X(f"{i}:Q", axis=None),
                        alt.Y(f"{j}:Q", axis=None),
                    ).properties(width=100, height=100)
                else:
                    # Pearson correlation block
                    corr = np.corrcoef(df[i].values, df[j].values)[0][1].round(4)
                    row |= alt.Chart(pd.DataFrame({'corr': [corr]})).mark_text(baseline='middle', size=16).encode(
                        text='corr:Q').properties(width=100, height=100)
                    checked_pairs.add(j + i)

        # Add row name to the right
        row |= alt.Chart(pd.DataFrame({'caption': [i]})).mark_text(baseline='middle', angle=270, size=12).encode(
            text='caption:N').properties(width=30, height=100)

        # Append row to the chart
        if chart:
            chart &= row
        else:
            chart = row

    # Bottom captions row
    row = alt.hconcat()
    for i in df.columns:
        row |= alt.Chart(pd.DataFrame({'caption': [i]})).mark_text(baseline='middle', size=12).encode(
            text='caption:N').properties(width=100, height=30)

    chart &= row

    return chart.configure_view(strokeWidth=0)
