import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"

tables = pd.read_html(URL)
df = tables[0]
print(df)

hsbc = df.loc[df["Bank name"] == "HSBC"]
print(hsbc.iloc[0]["Rank"])
