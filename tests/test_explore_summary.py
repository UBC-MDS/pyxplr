from pyxplr.explore_summary import explore_summary
import pandas as pd

# Test data
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                   "B":["apple", "banada", "orange", "strawberry", "blueberry"],
                   "C":["2", "1", "3", "4", "6"],
                   "D":[14, 3, 17, 2, 6]})

def test_explore_summary():
  result = explore_summary(df)
  assert result.shape[0] == 8
