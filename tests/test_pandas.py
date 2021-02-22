import pandas as pd

print('doing pandas test')

df = pd.read_csv("pandas_test.csv")

assert df["bar"].min() == 11
assert df["foo"].max() == 30
assert df["baz"].iloc[2] == 32

