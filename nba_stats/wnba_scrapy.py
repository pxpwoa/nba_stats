# wnba_scrapy_1.0
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
import re
import datetime

gameday = re.compile(r'gameday.*')

def gameid(mon,year):
    #driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = []
    game_link = []
    game_date = []
    while True:
        driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')

        link = 'http://www.wnba.com/schedule/#?month='+'{:02d}'.format(mon)+'&season='+str(year)+'&seasontype=02'

        try:
            driver.get(link)
            soup = bs(driver.page_source)
            gamelink = soup.find_all("a", text = 'Game Info')
            for link in gamelink:
                game_link.append(link.get('href'))
                game_id.append(link.get('href').split('/')[-3]+link.get('href').split('/')[-2])
                date = datetime.datetime.strptime(link.get('href').split('/')[-3], "%Y%m%d").date().strftime('%m/%d/%Y')
                game_date.append(date)

        except (TimeoutException,WebDriverException,IndexError,AttributeError):
            driver.quit()
        else:
            break

    driver.quit()

    return(game_link,game_id,game_date)     


def score_box_data(game_link):
    while True:
        driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
        link = game_link
        try:
            driver.get(link)
            soup = bs(driver.page_source)
            team_home = soup.find_all('th',class_ ='game__box-score-team')[0].text.strip()
            team_away = soup.find_all('th',class_ ='game__box-score-team')[1].text.strip()
            div = soup.find_all('div',class_ = 'stat-table__overflow')   
            tds_4 = div[0].tfoot.find_all('td')
            tds_5 = div[1].tfoot.find_all('td')
            tds_6 = div[2].tbody.find_all('td')
            tds_1 = div[3].tfoot.find_all('td')
            tds_2 = div[4].tfoot.find_all('td')
            tds_3 = div[5].tbody.find_all('td')
            FGM_home = tds_1[2].text.split()[0].strip()
            FGA_home = tds_1[2].text.split()[2].strip()
            FG_ratio_home = tds_1[3].text.strip()
            threePM_home = tds_1[4].text.split()[0].strip()
            threePA_home = tds_1[4].text.split()[2].strip()
            threeP_ratio_home = tds_1[5].text.strip()
            FTM_home = tds_1[6].text.split()[0].strip()
            FTA_home = tds_1[6].text.split()[2].strip()
            FT_ratio_home = tds_1[7].text.strip()
            OREB_home = tds_1[9].text.strip()
            DREB_home = tds_1[10].text.strip()
            REB_home = tds_1[11].text.strip()
            AST_home = tds_1[12].text.strip()
            PF_home = tds_1[13].text.strip()
            STL_home = tds_1[14].text.strip()
            TOV_home = tds_1[15].text.strip()
            BS_home = tds_1[16].text.strip()
            BA_home = tds_1[17].text.strip()
            PTS_home = tds_1[18].text.strip()

            FGM_away = tds_4[2].text.split()[0].strip()
            FGA_away = tds_4[2].text.split()[2].strip()
            FG_ratio_away = tds_4[3].text.strip().strip()
            threePM_away = tds_4[4].text.split()[0].strip()
            threePA_away = tds_4[4].text.split()[2].strip()
            threeP_ratio_away = tds_4[5].text.strip()
            FTM_away = tds_4[6].text.split()[0].strip()
            FTA_away = tds_4[6].text.split()[2].strip()
            FT_ratio_away = tds_4[7].text.strip()
            OREB_away = tds_4[9].text.strip()
            DREB_away = tds_4[10].text.strip()
            REB_away = tds_4[11].text.strip()
            AST_away = tds_4[12].text.strip()
            PF_away = tds_4[13].text.strip()
            STL_away = tds_4[14].text.strip()
            TOV_away = tds_4[15].text.strip()
            BS_away = tds_4[16].text.strip()
            BA_away = tds_4[17].text.strip()
            PTS_away = tds_4[18].text.strip()


            POSS_home = tds_2[2].text.strip()
            OffRtg_home = tds_2[3].text.strip()
            DefRtg_home = tds_2[4].text.strip()
            NetRtg_home = tds_2[5].text.strip()
            AST_ratio_home = tds_2[6].text.strip()
            AST_div_TO_home = tds_2[7].text.strip()
            OREB_ratio_home = tds_2[8].text.strip()
            DREB_ratio_home = tds_2[9].text.strip()
            REB_ratio_home = tds_2[10].text.strip()
            TO_Ratio_home = tds_2[11].text.strip()
            eFG_ratio_home = tds_2[12].text.strip()
            TS_ratio_home = tds_2[13].text.strip()
            USG_ratio_home = tds_2[14].text.strip()
            PACE_home = tds_2[15].text.strip()
            PIE_home = tds_2[16].text.strip()


            POSS_away = tds_5[2].text.strip()
            OffRtg_away = tds_5[3].text.strip()
            DefRtg_away = tds_5[4].text.strip()
            NetRtg_away = tds_5[5].text.strip()
            AST_ratio_away = tds_5[6].text.strip()
            AST_div_TO_away = tds_5[7].text.strip()
            OREB_ratio_away = tds_5[8].text.strip()
            DREB_ratio_away = tds_5[9].text.strip()
            REB_ratio_away = tds_5[10].text.strip()
            TO_Ratio_away = tds_5[11].text.strip()
            eFG_ratio_away = tds_5[12].text.strip()
            TS_ratio_away = tds_5[13].text.strip()
            USG_ratio_away = tds_5[14].text.strip()
            PACE_away = tds_5[15].text.strip()
            PIE_away = tds_5[16].text.strip()

            EFG_ratio_home = tds_3[0].text.strip()
            FTA_rate_home = tds_3[1].text.strip()
            TO_ratio_home = tds_3[3].text.strip()
            OREB_ratio_home = tds_3[2].text.strip()

            EFG_ratio_away = tds_6[0].text.strip()
            FTA_rate_away = tds_6[1].text.strip()
            TO_ratio_away = tds_6[3].text.strip()
            OREB_ratio_away = tds_6[2].text.strip()
        except (TimeoutException,WebDriverException,IndexError,AttributeError):
            driver.quit()
        else:
            break


    driver.quit()
    return([FGM_away ,
            FGA_away ,
            FG_ratio_away ,
            threePM_away ,
            threePA_away ,
            threeP_ratio_away ,
            FTM_away ,
            FTA_away ,
            FT_ratio_away ,
            OREB_away ,
            DREB_away ,
            REB_away ,
            AST_away ,
            PF_away ,
            STL_away ,
            TOV_away ,
            BS_away ,
            BA_away ,
            PTS_away ,
            FGM_home ,
            FGA_home ,
            FG_ratio_home ,
            threePM_home ,
            threePA_home ,
            threeP_ratio_home ,
            FTM_home ,
            FTA_home ,
            FT_ratio_home ,
            OREB_home ,
            DREB_away ,
            REB_home ,
            AST_home ,
            PF_home ,
            STL_home ,
            TOV_home ,
            BS_home ,
            BA_home ,
            PTS_home ],

            [POSS_away ,
            OffRtg_away ,
            DefRtg_away ,
            NetRtg_away ,
            AST_ratio_away ,
            AST_div_TO_away ,
            OREB_ratio_away ,
            DREB_ratio_away ,
            REB_ratio_away ,
            TO_Ratio_away ,
            eFG_ratio_away ,
            TS_ratio_away ,
            USG_ratio_away ,
            PACE_away ,
            PIE_away ,
            POSS_home ,
            OffRtg_home ,
            DefRtg_home ,
            NetRtg_home ,
            AST_ratio_home ,
            AST_div_TO_home ,
            OREB_ratio_home ,
            DREB_ratio_home ,
            REB_ratio_home ,
            TO_Ratio_home ,
            eFG_ratio_home ,
            TS_ratio_home ,
            USG_ratio_home ,
            PACE_home ,
            PIE_home],

            [EFG_ratio_away ,
            FTA_rate_away ,
            TO_ratio_away ,
            OREB_ratio_away ,
            EFG_ratio_home ,
            FTA_rate_home ,
            TO_ratio_home ,
            OREB_ratio_home],

            [team_home ,
            team_away ])


