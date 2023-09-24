import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL2021")

df = pd.read_html(url, header=0)

# with open("tatum_data.csv", "a+") as tatum:
#     for x in df:
#         tatum.write(x.to_csv)
# tatum.close()

# def save_data():
#     pass
print(len(df))
df[0].to_csv("tatum2021.csv")
