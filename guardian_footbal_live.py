from urllib.request import urlopen
from bs4 import BeautifulSoup
url ="https://www.theguardian.com/football/live"
html = urlopen(url)

soup = BeautifulSoup(html.read(),"html.parser")
options = []
for leagues in soup.find_all("div",{"class","football-table__container"}):
        leagueName = leagues.div.table.caption.a#(leagues.find("a",{"class":"football-matches__heading"}))

        dates = leagues.div.table.caption.span
        print(dates.text)
        
        league={}
        
        print(leagueName.text)
        leagues['name']=leagueName.text

        fix={}

        main = leagues.div.table.tbody.tr.find("td",{"class":"football-match__teams table-column--main"})
        #print(main)

        fixLink = main.a.attrs['href']
        print(fixLink)
        fix['link']=fixLink

        teamsPlaying=[]
        for fixTeams in main.find_all("span",class_="team-name__long"):
                print(fixTeams.text)
                teamsPlaying.append(fixTeams.text)
        fix['teams']=teamsPlaying

        mStat = main.parent.find("td",class_="football-match__status football-match__status--f table-column--sub")
        print(mStat.time.text)


        
        
        
        
                
print(options)
        
        



