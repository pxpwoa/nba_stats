# wnba_odds_scrapy_1.0
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from pandas import Series,DataFrame,merge
import pandas as pd
import re
import csv


year =2017
mon_end = 5
day_end = 13
mon = 6
day = 10

team_win_away = []
team_lost_away = []
team_win_home = []
team_lost_home = []
line_spread = []
line_total = []   
game_id = []

def montonum(x):
    return { 'May':5,
             'Jun':6,
             'Jul':7,
             'Aug':8,
             'Sep':9,
             'Oct':10,
            }.get(x, x) 
    
def name_replace(x):
    return { 'SA':'SAN',
             'LOS':'LAS',
             'NY':'NYL',
            }.get(x, x) 

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER',
}
while(not(mon == mon_end and day <= day_end)):
    
    link_w = 'http://www.oddsshark.com/wnba/scores?date='+'{:02d}'.format(mon)+'/'+'{:02d}'.format(day)+'/'+str(year)
    
    r = requests.get(link_w)
    soup = bs(r.text) 
    divs = soup.find_all('div',class_ = 'scores-table')
    #div = divs[0]
    for div in divs:
        if div.find('td',class_ = 'date').text.split()[1] == str(day):
            cells = div.find_all('tr')
            away = cells[2].find_all('td')
            home = cells[3].find_all('td')
            team_win_away.append(away[1].text.split('-')[0])
            team_lost_away.append(away[1].text.split('-')[1])
            team_win_home.append(home[1].text.split('-')[0])
            team_lost_home.append(home[1].text.split('-')[1])
            line_spread.append(home[2].text.split()[0].replace('+',''))
            line_total.append(away[3].text.split()[0])     
            game_id.append(str(year)+'{:02d}'.format(mon)+'{:02d}'.format(day)+name_replace(away[0].text)+name_replace(home[0].text))
            
    date = soup.find('div',id = 'scoreboard-date-picker').text.split()
    mon = montonum(date[2])
    day = int(date[3])
    
    
wnba_odds_dict = {      'game_ID':game_id ,
                        'team_win_away':team_win_away ,
                        'team_lost_away':team_lost_away ,
                        'team_win_home':team_win_home ,
                        'team_lost_home':team_lost_home ,
                        'line_spread':line_spread ,
                        'line_total':line_total 
                 }

wnba_odds_frame = DataFrame(wnba_odds_dict)



cnx = create_engine('mysql+pymysql://root:blw3927493@127.0.0.1:3306/wnba_stats', echo=False)

wnba_odds_frame.to_sql(name='wnba_odds_frame', con=cnx, if_exists = 'replace', index=False)
