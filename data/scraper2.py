import pandas as pd

url = "https://www.basketball-reference.com/players/t/tatumja01/splits/2023"

df = pd.read_html(url, header=0)

# with open("tatum_data.csv", "a+") as tatum:
#     for x in df:
#         tatum.write(x.to_csv)
# tatum.close()

# def save_data():
#     pass

for x in df:
    print(x)
