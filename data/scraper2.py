import pandas as pd

url = "https://www.basketball-reference.com/players/t/tatumja01.html"

df = pd.read_html(url, header=0)
print(df)
