from bs4 import BeautifulSoup
import lxml
import requests


response = requests.get("https://www.basketball-reference.com/players/t/tatumja01.html")

soup = BeautifulSoup(response.text, "lxml")
print(soup)
