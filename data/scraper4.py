import pandas as pd


resource = pd.read_html(
    "https://www.basketball-reference.com/boxscores/202305290BOS.html"
)

# print(resource, type(resource[0]), len(resource))

for x in resource:
    print(x.describe())
