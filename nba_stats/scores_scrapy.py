import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')


def score_link(year,mon,day):
    mon = '{:02d}'.format(mon)
    day = '{:02d}'.format(day)
    link =  'http://stats.nba.com/scores#!/'+mon+'/'+day+'/'+str(year)
    return(link)

def scores(year,mon,day):
    link = score_link(year,mon,day)
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find("div",class_ = "linescores")
    
    for div in soup.find_all("div",class_ = "linescores"):
        trs = div.find_all("tr")
        tds_1 = trs[1].find_all("td")
        team_away = tds_1[0].text.split()[0]
        scores_away = tds_1[5].text.split()[0]
        tds_2 = trs[2].find_all("td")
        team_home = tds_2[0].text.split()[0]
        scores_home = tds_2[5].text.split()[0]
        
        game_id = div.find("a",text = "Box Score").get('href').split('/')[-1]
    
    return(list[team_away,team_home,scores_away,scores_home],game_id)        


def score_box_traditional(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/'
    driver.get(link)
    soup = bs(driver.page_source)  
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')
    FGM_away = tds_1[2].text
    FGA_away = tds_1[3].text
    FG_ratio_away = tds_1[4].text
    threePM_away = tds_1[5].text
    threePA_away = tds_1[6].text
    threeP_ratio_away = tds_1[7].text
    FTM_away = tds_1[8].text
    FTA_away = tds_1[9].text
    FT_ratio_away = tds_1[10].text
    OREB_away = tds_1[11].text
    REB_away = tds_1[12].text
    AST_away = tds_1[13].text
    TOV_away = tds_1[14].text
    STL_away = tds_1[15].text
    BLK_away = tds_1[16].text
    PF_away = tds_1[17].text
    
    
    tds_2 = div[1].tfoot.find_all('td')
    FGM_home = tds_2[2].text
    FGA_home = tds_2[3].text
    FG_ratio_home = tds_2[4].text
    threePM_home = tds_2[5].text
    threePA_home = tds_2[6].text
    threeP_ratio_home = tds_2[7].text
    FTM_home = tds_2[8].text
    FTA_home = tds_2[9].text
    FT_ratio_home = tds_2[10].text
    OREB_home = tds_2[11].text
    REB_home = tds_2[12].text
    AST_home = tds_2[13].text
    TOV_home = tds_2[14].text
    STL_home = tds_2[15].text
    BLK_home = tds_2[16].text
    PF_home = tds_2[17].text
    
    return( list[FGM_away ,
            FGA_away ,
            FG_ratio_away ,
            threePM_away ,
            threePA_away ,
            threeP_ratio_away ,
            FTM_away ,
            FTA_away ,
            FT_ratio_away ,
            OREB_away ,
            REB_away ,
            AST_away ,
            TOV_away ,
            STL_away ,
            BLK_away ,
            PF_away ,
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
            REB_home ,
            AST_home ,
            TOV_home ,
            STL_home ,
            BLK_home ,
            PF_home ])

def score_box_advanced(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/advanced/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')
        
    OffRtg_away = tds_1[2].text
    DefRtg_away = tds_1[3].text
    NetRtg_away = tds_1[4].text
    AST_ratio_away = tds_1[5].text
    AST_div_TO_away = tds_1[6].text
    AST_Ratio_away = tds_1[7].text
    OREB_ratio_away = tds_1[8].text
    DREB_ratio_away = tds_1[9].text
    REB_ratio_away = tds_1[10].text
    TO_Ratio_away = tds_1[11].text
    eFG_ratio_away = tds_1[12].text
    TS_ratio_away = tds_1[13].text
    USG_ratio_away = tds_1[14].text
    PACE_away = tds_1[15].text
    PIE_away = tds_1[16].text
   
    
    
    tds_2 = div[1].tfoot.find_all('td')
    OffRtg_home = tds_2[2].text
    DefRtg_home = tds_2[3].text
    NetRtg_home = tds_2[4].text
    AST_ratio_home = tds_2[5].text
    AST_div_TO_home = tds_2[6].text
    AST_Ratio_home = tds_2[7].text
    OREB_ratio_home = tds_2[8].text
    DREB_ratio_home = tds_2[9].text
    REB_ratio_home = tds_2[10].text
    TO_Ratio_home = tds_2[11].text
    eFG_ratio_home = tds_2[12].text
    TS_ratio_home = tds_2[13].text
    USG_ratio_home = tds_2[14].text
    PACE_home = tds_2[15].text
    PIE_home = tds_2[16].text
    
    return( list[OffRtg_away ,
            DefRtg_away ,
            NetRtg_away ,
            AST_ratio_away ,
            AST_div_TO_away ,
            AST_Ratio_away ,
            OREB_ratio_away ,
            DREB_ratio_away ,
            REB_ratio_away ,
            TO_Ratio_away ,
            eFG_ratio_away ,
            TS_ratio_away ,
            USG_ratio_away ,
            PACE_away ,
            PIE_away ,
            OffRtg_home ,
            DefRtg_home ,
            NetRtg_home ,
            AST_ratio_home ,
            AST_div_TO_home ,
            AST_Ratio_home ,
            OREB_ratio_home ,
            DREB_ratio_home ,
            REB_ratio_home ,
            TO_Ratio_home ,
            eFG_ratio_home ,
            TS_ratio_home ,
            USG_ratio_home ,
            PACE_home ,
            PIE_home ])

def score_box_misc(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/misc/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')

    PTS_OFF_TO_away = tds_1[2].text
    SEC_PTS_away = tds_1[3].text
    FBPS_away = tds_1[4].text
    PITP_away = tds_1[5].text
    BLK_away = tds_1[10].text
    PF_away = tds_1[12].text
    
    
    tds_2 = div[1].tfoot.find_all('td')
    PTS_OFF_TO_home = tds_2[2].text
    SEC_PTS_home = tds_2[3].text
    FBPS_home = tds_2[4].text
    PITP_home = tds_2[5].text
    BLK_home = tds_2[10].text
    PF_home = tds_2[12].text
    
    return( list[ PTS_OFF_TO_away ,
            SEC_PTS_away ,
            FBPS_away ,
            PITP_away ,
            BLK_away ,
            PF_away ,
            PTS_OFF_TO_home ,
            SEC_PTS_home ,
            FBPS_home ,
            PITP_home ,
            BLK_home ,
            PF_home ])
   
    
def score_box_scoring(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/advanced/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')
        
    ratio_FGA_2PT_away = tds_1[2].text
    ratio_FGA_3PT_away = tds_1[3].text
    ratio_PTS_2PT_away = tds_1[4].text
    ratio_PTS_2PT_MR_away = tds_1[5].text
    ratio_PTS_3PT_away = tds_1[6].text
    ratio_PTS_FBPS_away = tds_1[7].text
    ratio_PTS_FT_away = tds_1[8].text
    ratio_PTS_OFFTO_away = tds_1[9].text
    ratio_PTS_PITP_away = tds_1[10].text
    sec_FGM_ratio_AST_away = tds_1[11].text
    sec_FGM_ratio_UAST_away = tds_1[12].text
    thr_FGM_ratio_AST_away = tds_1[13].text
    thr_FGM_ratio_UAST_away = tds_1[14].text
    FGM_ratio_AST_away = tds_1[15].text
    FGM_ratio_UAST_away = tds_1[16].text

   
    
    
    tds_2 = div[1].tfoot.find_all('td')
    ratio_FGA_2PT_home = tds_2[2].text
    ratio_FGA_3PT_home = tds_2[3].text
    ratio_PTS_2PT_home = tds_2[4].text
    ratio_PTS_2PT_MR_home = tds_2[5].text
    ratio_PTS_3PT_home = tds_2[6].text
    ratio_PTS_FBPS_home = tds_2[7].text
    ratio_PTS_FT_home = tds_2[8].text
    ratio_PTS_OFFTO_home = tds_2[9].text
    ratio_PTS_PITP_home = tds_2[10].text
    sec_FGM_ratio_AST_home = tds_2[11].text
    sec_FGM_ratio_UAST_home = tds_2[12].text
    thr_FGM_ratio_AST_home = tds_2[13].text
    thr_FGM_ratio_UAST_home = tds_2[14].text
    FGM_ratio_AST_home = tds_2[15].text
    FGM_ratio_UAST_home = tds_2[16].text

    return( list[ratio_FGA_2PT_away ,
            ratio_FGA_3PT_away ,
            ratio_PTS_2PT_away ,
            ratio_PTS_2PT_MR_away ,
            ratio_PTS_3PT_away ,
            ratio_PTS_FBPS_away ,
            ratio_PTS_FT_away ,
            ratio_PTS_OFFTO_away ,
            ratio_PTS_PITP_away ,
            sec_FGM_ratio_AST_away ,
            sec_FGM_ratio_UAST_away ,
            thr_FGM_ratio_AST_away ,
            thr_FGM_ratio_UAST_away ,
            FGM_ratio_AST_away ,
            FGM_ratio_UAST_away ,
            ratio_FGA_2PT_home ,
            ratio_FGA_3PT_home ,
            ratio_PTS_2PT_home ,
            ratio_PTS_2PT_MR_home ,
            ratio_PTS_3PT_home ,
            ratio_PTS_FBPS_home ,
            ratio_PTS_FT_home ,
            ratio_PTS_OFFTO_home ,
            ratio_PTS_PITP_home ,
            sec_FGM_ratio_AST_home ,
            sec_FGM_ratio_UAST_home ,
            thr_FGM_ratio_AST_home ,
            thr_FGM_ratio_UAST_home ,
            FGM_ratio_AST_home ,
            FGM_ratio_UAST_home ])
    
    
def score_box_fourfactors(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/four-factors/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')

    EFG_ratio_away = tds_1[2].text
    FTA_rate_away = tds_1[3].text
    TO_ratio_away = tds_1[4].text
    OREB_ratio_away = tds_1[5].text

    
    
    tds_2 = div[1].tfoot.find_all('td')
    EFG_ratio_home = tds_2[2].text
    FTA_rate_home = tds_2[3].text
    TO_ratio_home = tds_2[4].text
    OREB_ratio_home = tds_2[5].text
    
    return( list[EFG_ratio_away ,
            FTA_rate_away ,
            TO_ratio_away ,
            OREB_ratio_away ,
            EFG_ratio_home ,
            FTA_rate_home ,
            TO_ratio_home ,
            OREB_ratio_home ])
    
    
def score_box_playretracking(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/advanced/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')
        
    DIST_away = tds_1[2].text
    SPD_away = tds_1[3].text
    TCHS_away = tds_1[4].text
    PASS_away = tds_1[5].text
    AST_away = tds_1[6].text
    SAST_away = tds_1[7].text
    FTAST_away = tds_1[8].text
    DFGM_away = tds_1[9].text
    DFGA_away = tds_1[10].text
    DFG_ratio_away = tds_1[11].text
    ORBC_away = tds_1[12].text
    DRBC_away = tds_1[13].text
    FG_ration_away = tds_1[15].text
    CFGM_away = tds_1[15].text
    CFGA_away = tds_1[16].text
    CFG_ratio_away = tds_1[17].text
    UFGM_away = tds_1[18].text
    UFGA_away = tds_1[19].text
    UFG_ratio_away = tds_1[20].text

   
    
    
    DIST_home = tds_2[2].text
    SPD_home = tds_2[3].text
    TCHS_home = tds_2[4].text
    PASS_home = tds_2[5].text
    AST_home = tds_2[6].text
    SAST_home = tds_2[7].text
    FTAST_home = tds_2[8].text
    DFGM_home = tds_2[9].text
    DFGA_home = tds_2[10].text
    DFG_ratio_home = tds_2[11].text
    ORBC_home = tds_2[12].text
    DRBC_home = tds_2[13].text
    FG_ration_home = tds_2[15].text
    CFGM_home = tds_2[15].text
    CFGA_home = tds_2[16].text
    CFG_ratio_home = tds_2[17].text
    UFGM_home = tds_2[18].text
    UFGA_home = tds_2[19].text
    UFG_ratio_home = tds_2[20].text
    
    return( list[DIST_away ,
            SPD_away ,
            TCHS_away ,
            PASS_away ,
            AST_away ,
            SAST_away ,
            FTAST_away ,
            DFGM_away ,
            DFGA_away ,
            DFG_ratio_away ,
            ORBC_away ,
            DRBC_away ,
            FG_ration_away ,
            CFGM_away ,
            CFGA_away ,
            CFG_ratio_away ,
            UFGM_away ,
            UFGA_away ,
            UFG_ratio_away ,
            DIST_home ,
            SPD_home ,
            TCHS_home ,
            PASS_home ,
            AST_home ,
            SAST_home ,
            FTAST_home ,
            DFGM_home ,
            DFGA_home ,
            DFG_ratio_home ,
            ORBC_home ,
            DRBC_home ,
            FG_ration_home ,
            CFGM_home ,
            CFGA_home ,
            CFG_ratio_home ,
            UFGM_home ,
            UFGA_home ,
            UFG_ratio_home ])
    
    
def score_box_hustle(game_id):
    driver = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver')
    game_id = '0041600203'
    link = 'http://stats.nba.com/game/#!/'+game_id+'/hustle/'
    driver.get(link)
    soup = bs(driver.page_source)
    div = soup.find_all('div',class_ = 'nba-stat-table__overflow')
    
    tds_1 = div[0].tfoot.find_all('td')

    screen_ASS_away = tds_1[2].text
    deflections_away = tds_1[3].text
    loose_balls_recovered_away = tds_1[4].text
    charges_drawn_away = tds_1[5].text
    contest_2PT_shots_away = tds_1[6].text
    contest_3PT_shots_away = tds_1[7].text


    
    
    tds_2 = div[1].tfoot.find_all('td')
    screen_ASS_home = tds_2[2].text
    deflections_home = tds_2[3].text
    loose_balls_recovered_home = tds_2[4].text
    charges_drawn_home = tds_2[5].text
    contest_2PT_shots_home = tds_2[6].text
    contest_3PT_shots_home = tds_2[7].text
    
    return( list[screen_ASS_away ,
            deflections_away ,
            loose_balls_recovered_away ,
            charges_drawn_away ,
            contest_2PT_shots_away ,
            contest_3PT_shots_away ,
            screen_ASS_home ,
            deflections_home ,
            loose_balls_recovered_home ,
            charges_drawn_home ,
            contest_2PT_shots_home ,
            contest_3PT_shots_home ])
