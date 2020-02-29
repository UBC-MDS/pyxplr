def explore_feature_map(dataframe, features = []):
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
        Features specification includes an invalid / non-existent feature

    Notes
    -----
    (Additional notes to be filled during development)

    Examples
    --------
    from pyxplr import explore_feature_map

    chart = explore_feature_map(my_df)
    chart
    """
    raise NotImplemented