#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


Rank=list()
Name=list()
Gp=list()
Mpg=list()
Fgm=list()
Fga=list()
Fg_percent=list()
Threepm=list()
Threepa=list()
Three_percent=list()
Ftm=list()
Fta=list()
Freethrow_percent=list()
Tov=list()
Pf=list()
Orb=list()
Drb=list()
Rpg=list()
Apg=list()
Spg=list()
Bpg=list()
Ppg=list()
Height=list()
Weight=list()


# In[3]:


start=1
end=47
for start in range (1,end):
    page = str(start)
    url="https://basketball.realgm.com/nba/stats/Historical/Averages/All/points/All/desc/"+page+"/Regular_Season"
    html=requests.get(url)
    soup=BeautifulSoup(html.content,"html.parser")
    table=soup("table",attrs={"class":"tablesaw"})[0]
    for row in table.find_all("tr"):
        cells=row.find_all("td")
        if(len(cells)<22):
            continue
        Rank.append(cells[0].get_text().strip())
        Name.append(cells[1].get_text().strip())
        Gp.append(cells[3].get_text().strip())
        Mpg.append(cells[4].get_text().strip())
        Fgm.append(cells[5].get_text().strip())
        Fga.append(cells[6].get_text().strip())
        Fg_percent.append(cells[7].get_text().strip())
        Threepm.append(cells[8].get_text().strip())
        Threepa.append(cells[9].get_text().strip())
        Three_percent.append(cells[10].get_text().strip())
        Ftm.append(cells[11].get_text().strip())
        Fta.append(cells[12].get_text().strip())
        Freethrow_percent.append(cells[13].get_text().strip())
        Tov.append(cells[14].get_text().strip())
        Pf.append(cells[15].get_text().strip())
        Orb.append(cells[16].get_text().strip())
        Drb.append(cells[17].get_text().strip())
        Rpg.append(cells[18].get_text().strip())
        Apg.append(cells[19].get_text().strip())
        Spg.append(cells[20].get_text().strip())
        Bpg.append(cells[21].get_text().strip())
        Ppg.append(cells[22].get_text().strip())
        Height.append(0)
        Weight.append(0)


# In[4]:


df=pd.DataFrame({"Rank":Rank,"Name":Name,"GP":Gp,"MPG":Mpg,"FGM":Fgm,"FGA":Fga,"FG%":Fg_percent,"3PM":Threepm,"3PA":Threepa,"3P%":Three_percent,"FTM":Ftm,"FTA":Fta,"FT%":Freethrow_percent,"TOV":Tov,"PF":Pf,"ORB":Orb,"DRB":Drb,"RPG":Rpg,"APG":Apg,"SPG":Spg,"BPG":Bpg,"PPG":Ppg,"Height":Height,"Weight":Weight})
df['Name']  = df['Name'].str.replace('*', '')
df


# In[ ]:



       


# In[5]:


dfh=pd.read_csv(r'C:\Users\shake\OneDrive\Desktop\all_seasons.csv')
dfh


# In[6]:


dfh = dfh.drop_duplicates(subset=["player_name"])
dfh


# In[7]:


for i in range(0,len(df)) :
    for j in range(0,len(dfh)) :
        if df['Name'].iloc[i] == dfh['player_name'].iloc[j]:
            df['Height'].iloc[i]=dfh['player_height'].iloc[j]
            df['Weight'].iloc[i]=dfh['player_weight'].iloc[j]


# In[8]:


df


# In[10]:


df.to_csv('first_data.csv')


# In[ ]:




