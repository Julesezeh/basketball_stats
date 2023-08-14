import pandas as pd

url = "https://www.basketball-reference.com/players/t/tatumja01/splits/2023"

df = pd.read_html(url, header=0)

print(df)
