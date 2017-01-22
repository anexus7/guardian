from urllib.request import urlopen
from bs4 import BeautifulSoup

url ="https://www.theguardian.com/football/live"
html = urlopen(url)
soup = BeautifulSoup(html.read(),"html.parser")

options = []

for leagues in soup.find_all("div",{"class","football-table__container"}):

        league={}

        lName = leagues.div.table.caption.a
        dates = leagues.div.table.caption.span

        print(dates.text)
        league['date']=dates.text
        
        print(lName.text)
        league['name']=lName.text

        

        match = leagues.div.table.tbody.find_all("tr")

        fix={}
        for f in match:
                            
                main=f.find("td",{"class":"football-match__teams table-column--main"})
                fixLink = f.a.attrs['href']
                print(fixLink)
                fix['link']=fixLink

                teamsPlaying=[]
                homeTeam = main.find("div",{"class":"football-match__team football-match__team--home football-team"})
                awayTeam = main.find("div",{"class":"football-match__team football-match__team--away football-team"})
                print((homeTeam.span.text)," ",homeTeam.find("div",class_="football-team__score").text)
                teamsPlaying.append(homeTeam.span.text)
                print((awayTeam.span.text)," ",awayTeam.find("div",class_="football-team__score").text)
                teamsPlaying.append(awayTeam.span.text)
                fix['teams']=teamsPlaying

                mStat = f.parent.find("td",class_="football-match__status football-match__status--f table-column--sub")
                if(mStat):
                        print("would begin at:",mStat.time.text," now go back to work!\n")
                        fix['stat']=mStat.time.text
                
                mStat = f.parent.find("td",class_="football-match__status football-match__status--ft table-column--sub")
                if(mStat):
                        print(mStat.text)
                        fix['stat']=mStat.text
                #print(fix)

##                mStat = f.parent.find("td",class_="football-match__status football-match__status--*******************")
##                if (mStat):
##                        #print(mStat.text)
##                        #fix['stat']=mStat.text
##
##                else:
##                        print("you missed a case of football-match__status, inspect that element NOW!!!!")
                
                league['fixture']=fix
        options.append(league)



