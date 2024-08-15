import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
df1 = pd.json_normalize(results)

cherry = df1.loc[df1["name"] == "Cherry"]
print((cherry.iloc[0]["family"]), (cherry.iloc[0]["genus"]))

banana = df1.loc[df1["name"] == "Banana"]
print(banana.iloc[0]["nutritions.calories"])
