from urllib.request import urlopen
from bs4 import BeautifulSoup
url ="https://www.theguardian.com/football/live"
html = urlopen(url)

soup = BeautifulSoup(html.read(),"html.parser")

for leagues in soup.find_all("div",{"class":"football-table__container"}):
        anchortags = (leagues.find_all("a"))
        for i in anchortags:
                print(i.text)

