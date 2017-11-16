# nba_stats_spider_1.3
import nba_stats_scrapy as ny
import numpy as np
from pandas import DataFrame
import datetime
import pymysql
from sqlalchemy import create_engine


date = datetime.datetime(2017,10,18)
date_end = datetime.datetime(2017,10,17)

team_away = []
team_home = []
FGM_away = []
FGA_away = []
FG_ratio_away = []
threePM_away = []
threePA_away = []
threeP_ratio_away = []
FTM_away = []
FTA_away = []
FT_ratio_away = []
OREB_away = []
DREB_away = []
REB_away = []
AST_away = []
TOV_away = []
STL_away = []
BLK_away = []
PF_away = []
PTS_away = []
FGM_home = []
FGA_home = []
FG_ratio_home = []
threePM_home = []
threePA_home = []
threeP_ratio_home = []
FTM_home = []
FTA_home = []
FT_ratio_home = []
OREB_home = []
DREB_home = []
REB_home = []
AST_home = []
TOV_home = []
STL_home = []
BLK_home = []
PF_home = []
PTS_home = []

OffRtg_away = []
DefRtg_away = []
NetRtg_away = []
AST_percent_away = []
AST_div_TO_away = []
AST_Ratio_away = []
OREB_ratio_away = []
DREB_ratio_away = []
REB_ratio_away = []
TO_Ratio_away = []
eFG_ratio_away = []
TS_ratio_away = []
USG_ratio_away = []
PACE_away = []
PIE_away = []
OffRtg_home = []
DefRtg_home = []
NetRtg_home = []
AST_percent_home = []
AST_div_TO_home = []
AST_Ratio_home = []
OREB_ratio_home = []
DREB_ratio_home = []
REB_ratio_home = []
TO_Ratio_home = []
eFG_ratio_home = []
TS_ratio_home = []
USG_ratio_home = []
PACE_home = []
PIE_home =[]

PTS_OFF_TO_away = []
SEC_PTS_away = []
FBPS_away = []
PITP_away = []
BLK_away = []
PF_away = []
PTS_OFF_TO_home = []
SEC_PTS_home = []
FBPS_home = []
PITP_home = []
BLK_home = []
PF_home = []
ratio_FGA_2PT_away = []
ratio_FGA_3PT_away = []
ratio_PTS_2PT_away = []
ratio_PTS_2PT_MR_away = []
ratio_PTS_3PT_away = []
ratio_PTS_FBPS_away = []
ratio_PTS_FT_away = []
ratio_PTS_OFFTO_away = []
ratio_PTS_PITP_away = []
sec_FGM_ratio_AST_away = []
sec_FGM_ratio_UAST_away = []
thr_FGM_ratio_AST_away = []
thr_FGM_ratio_UAST_away = []
FGM_ratio_AST_away = []
FGM_ratio_UAST_away = []
ratio_FGA_2PT_home = []
ratio_FGA_3PT_home = []
ratio_PTS_2PT_home = []
ratio_PTS_2PT_MR_home = []
ratio_PTS_3PT_home = []
ratio_PTS_FBPS_home = []
ratio_PTS_FT_home = []
ratio_PTS_OFFTO_home = []
ratio_PTS_PITP_home = []
sec_FGM_ratio_AST_home = []
sec_FGM_ratio_UAST_home = []
thr_FGM_ratio_AST_home = []
thr_FGM_ratio_UAST_home = []
FGM_ratio_AST_home = []
FGM_ratio_UAST_home =[]
EFG_ratio_away = []
FTA_rate_away = []
TO_ratio_away = []
OREB_ratio_away = []
EFG_ratio_home = []
FTA_rate_home = []
TO_ratio_home = []
OREB_ratio_home = []
DIST_away = []
SPD_away = []
TCHS_away = []
PASS_away = []
AST_away = []
SAST_away = []
FTAST_away = []
DFGM_away = []
DFGA_away = []
DFG_ratio_away = []
ORBC_away = []
DRBC_away = []
FG_ration_away = []
CFGM_away = []
CFGA_away = []
CFG_ratio_away = []
UFGM_away = []
UFGA_away = []
UFG_ratio_away = []
DIST_home = []
SPD_home = []
TCHS_home = []
PASS_home = []
AST_home = []
SAST_home = []
FTAST_home = []
DFGM_home = []
DFGA_home = []
DFG_ratio_home = []
ORBC_home = []
DRBC_home = []
FG_ration_home = []
CFGM_home = []
CFGA_home = []
CFG_ratio_home = []
UFGM_home = []
UFGA_home = []
UFG_ratio_home = []
screen_ASS_away = []
deflections_away = []
loose_balls_recovered_away = []
charges_drawn_away = []
contest_2PT_shots_away = []
contest_3PT_shots_away = []
screen_ASS_home = []
deflections_home = []
loose_balls_recovered_home = []
charges_drawn_home = []
contest_2PT_shots_home = []
contest_3PT_shots_home = []
game_ID = []
game_date = []

while not( date == date_end):

    (nogame,game_id,ID,away,home,date_str)  = ny.gameid(date)

    if nogame == True:
        date -= datetime.timedelta(days=1)

    else:
        date -= datetime.timedelta(days=1)
        for i in range(len(game_id)):       
            traditional_data =ny.score_box_traditional(game_id[i])
            advanced_data =ny.score_box_advanced(game_id[i])
            misc_data =ny.score_box_misc(game_id[i])
            scoring_data =ny.score_box_scoring(game_id[i])
            fourfactors_data =ny.score_box_fourfactors(game_id[i])
            playertracking_data =ny.score_box_playertracking(game_id[i])
            hustle_data =ny.score_box_hustle(game_id[i])
            
            game_date.append(date_str)
            team_away.append(away[i])
            team_home.append(home[i])
            FGM_away.append(traditional_data[0])
            FGA_away.append(traditional_data[1])
            FG_ratio_away.append(traditional_data[2])
            threePM_away.append(traditional_data[3])
            threePA_away.append(traditional_data[4])
            threeP_ratio_away.append(traditional_data[5])
            FTM_away.append(traditional_data[6])
            FTA_away.append(traditional_data[7])
            FT_ratio_away.append(traditional_data[8])
            OREB_away.append(traditional_data[9])
            DREB_away.append(traditional_data[10])
            REB_away.append(traditional_data[11])
           # AST_away.append(traditional_data[11])
            TOV_away.append(traditional_data[13])
            STL_away.append(traditional_data[14])
          #  BLK_away.append(traditional_data[14])
           # PF_away.append(traditional_data[15])
            PTS_away.append(traditional_data[17])
            FGM_home.append(traditional_data[18])
            FGA_home.append(traditional_data[19])
            FG_ratio_home.append(traditional_data[20])
            threePM_home.append(traditional_data[21])
            threePA_home.append(traditional_data[22])
            threeP_ratio_home.append(traditional_data[23])
            FTM_home.append(traditional_data[24])
            FTA_home.append(traditional_data[25])
            FT_ratio_home.append(traditional_data[26])
            OREB_home.append(traditional_data[27])
            DREB_home.append(traditional_data[28])
            REB_home.append(traditional_data[29])
           # AST_home.append(traditional_data[28])
            TOV_home.append(traditional_data[31])
            STL_home.append(traditional_data[32])
           # BLK_home.append(traditional_data[31])
           # PF_home.append(traditional_data[32])
            PTS_home.append(traditional_data[35])
            game_ID.append(ID[i])

            OffRtg_away.append(advanced_data[0])
            DefRtg_away.append(advanced_data[1])
            NetRtg_away.append(advanced_data[2])
            AST_percent_away.append(advanced_data[3])
            AST_div_TO_away.append(advanced_data[4])
            AST_Ratio_away.append(advanced_data[5])
           # OREB_ratio_away.append(advanced_data[6])
            DREB_ratio_away.append(advanced_data[7])
            REB_ratio_away.append(advanced_data[8])
            TO_Ratio_away.append(advanced_data[9])
            eFG_ratio_away.append(advanced_data[10])
            TS_ratio_away.append(advanced_data[11])
            USG_ratio_away.append(advanced_data[12])
            PACE_away.append(advanced_data[13])
            PIE_away.append(advanced_data[14])
            OffRtg_home.append(advanced_data[15])
            DefRtg_home.append(advanced_data[16])
            NetRtg_home.append(advanced_data[17])
            AST_percent_home.append(advanced_data[18])
            AST_div_TO_home.append(advanced_data[19])
            AST_Ratio_home.append(advanced_data[20])
           # OREB_ratio_home.append(advanced_data[21])
            DREB_ratio_home.append(advanced_data[22])
            REB_ratio_home.append(advanced_data[23])
            TO_Ratio_home.append(advanced_data[24])
            eFG_ratio_home.append(advanced_data[25])
            TS_ratio_home.append(advanced_data[26])
            USG_ratio_home.append(advanced_data[27])
            PACE_home.append(advanced_data[28])
            PIE_home.append(advanced_data[29])


            PTS_OFF_TO_away.append(misc_data[0])
            SEC_PTS_away.append(misc_data[1])
            FBPS_away.append(misc_data[2])
            PITP_away.append(misc_data[3])
            BLK_away.append(misc_data[4])
            PF_away.append(misc_data[5])
            PTS_OFF_TO_home.append(misc_data[6])
            SEC_PTS_home.append(misc_data[7])
            FBPS_home.append(misc_data[8])
            PITP_home.append(misc_data[9])
            BLK_home.append(misc_data[10])
            PF_home.append(misc_data[11])

            ratio_FGA_2PT_away.append(scoring_data[0])
            ratio_FGA_3PT_away.append(scoring_data[1])
            ratio_PTS_2PT_away.append(scoring_data[2])
            ratio_PTS_2PT_MR_away.append(scoring_data[3])
            ratio_PTS_3PT_away.append(scoring_data[4])
            ratio_PTS_FBPS_away.append(scoring_data[5])
            ratio_PTS_FT_away.append(scoring_data[6])
            ratio_PTS_OFFTO_away.append(scoring_data[7])
            ratio_PTS_PITP_away.append(scoring_data[8])
            sec_FGM_ratio_AST_away.append(scoring_data[9])
            sec_FGM_ratio_UAST_away.append(scoring_data[10])
            thr_FGM_ratio_AST_away.append(scoring_data[11])
            thr_FGM_ratio_UAST_away.append(scoring_data[12])
            FGM_ratio_AST_away.append(scoring_data[13])
            FGM_ratio_UAST_away.append(scoring_data[14])
            ratio_FGA_2PT_home.append(scoring_data[15])
            ratio_FGA_3PT_home.append(scoring_data[16])
            ratio_PTS_2PT_home.append(scoring_data[17])
            ratio_PTS_2PT_MR_home.append(scoring_data[18])
            ratio_PTS_3PT_home.append(scoring_data[19])
            ratio_PTS_FBPS_home.append(scoring_data[20])
            ratio_PTS_FT_home.append(scoring_data[21])
            ratio_PTS_OFFTO_home.append(scoring_data[22])
            ratio_PTS_PITP_home.append(scoring_data[23])
            sec_FGM_ratio_AST_home.append(scoring_data[24])
            sec_FGM_ratio_UAST_home.append(scoring_data[25])
            thr_FGM_ratio_AST_home.append(scoring_data[26])
            thr_FGM_ratio_UAST_home.append(scoring_data[27])
            FGM_ratio_AST_home.append(scoring_data[28])
            FGM_ratio_UAST_home.append(scoring_data[29])

            EFG_ratio_away.append(fourfactors_data[0])
            FTA_rate_away.append(fourfactors_data[1])
            TO_ratio_away.append(fourfactors_data[2])
            OREB_ratio_away.append(fourfactors_data[3])
            EFG_ratio_home.append(fourfactors_data[4])
            FTA_rate_home.append(fourfactors_data[5])
            TO_ratio_home.append(fourfactors_data[6])
            OREB_ratio_home.append(fourfactors_data[7])

            DIST_away.append(playertracking_data[0])
            SPD_away.append(playertracking_data[1])
            TCHS_away.append(playertracking_data[2])
            PASS_away.append(playertracking_data[3])
            AST_away.append(playertracking_data[4])
            SAST_away.append(playertracking_data[5])
           # FTAST_away.append(playertracking_data[6])
            DFGM_away.append(playertracking_data[6])
            DFGA_away.append(playertracking_data[7])
            DFG_ratio_away.append(playertracking_data[8])
            ORBC_away.append(playertracking_data[9])
            DRBC_away.append(playertracking_data[10])
            FG_ration_away.append(playertracking_data[11])
            CFGM_away.append(playertracking_data[12])
            CFGA_away.append(playertracking_data[13])
            CFG_ratio_away.append(playertracking_data[14])
            UFGM_away.append(playertracking_data[15])
            UFGA_away.append(playertracking_data[16])
            UFG_ratio_away.append(playertracking_data[17])
            DIST_home.append(playertracking_data[18])
            SPD_home.append(playertracking_data[19])
            TCHS_home.append(playertracking_data[20])
            PASS_home.append(playertracking_data[21])
            AST_home.append(playertracking_data[22])
            SAST_home.append(playertracking_data[23])
           #FTAST_home.append(playertracking_data[25])
            DFGM_home.append(playertracking_data[24])
            DFGA_home.append(playertracking_data[25])
            DFG_ratio_home.append(playertracking_data[26])
            ORBC_home.append(playertracking_data[27])
            DRBC_home.append(playertracking_data[28])
            FG_ration_home.append(playertracking_data[29])
            CFGM_home.append(playertracking_data[30])
            CFGA_home.append(playertracking_data[31])
            CFG_ratio_home.append(playertracking_data[32])
            UFGM_home.append(playertracking_data[33])
            UFGA_home.append(playertracking_data[34])
            UFG_ratio_home.append(playertracking_data[35])


            screen_ASS_away.append(hustle_data[0])
            deflections_away.append(hustle_data[1])
            loose_balls_recovered_away.append(hustle_data[2])
            charges_drawn_away.append(hustle_data[3])
            contest_2PT_shots_away.append(hustle_data[4])
            contest_3PT_shots_away.append(hustle_data[5])
            screen_ASS_home.append(hustle_data[6])
            deflections_home.append(hustle_data[7])
            loose_balls_recovered_home.append(hustle_data[8])
            charges_drawn_home.append(hustle_data[9])
            contest_2PT_shots_home.append(hustle_data[10])
            contest_3PT_shots_home.append(hustle_data[11])




traditional_data_dict = {'date':game_date ,
                        'team_home':team_home ,
                        'team_away':team_away ,
                        'game_ID':game_ID ,
                        'FGM_away':FGM_away,
                        'FGA_away':FGA_away,
                        'FG_ratio_away':FG_ratio_away,
                        'threePM_away':threePM_away,
                        'threePA_away':threePA_away,
                        'threeP_ratio_away':threeP_ratio_away,
                        'FTM_away':FTM_away,
                        'FTA_away':FTA_away,
                        'FT_ratio_away':FT_ratio_away,
                        'OREB_away':OREB_away,
                        'REB_away':REB_away,
                        #'AST_away':AST_away,
                        'TOV_away':TOV_away,
                        'STL_away':STL_away,
                        #'BLK_away':BLK_away,
                        #'PF_away':PF_away,
                        'PTS_away':PTS_away,
                        'FGM_home':FGM_home,
                        'FGA_home':FGA_home,
                        'FG_ratio_home':FG_ratio_home,
                        'threePM_home':threePM_home,
                        'threePA_home':threePA_home,
                        'threeP_ratio_home':threeP_ratio_home,
                        'FTM_home':FTM_home,
                        'FTA_home':FTA_home,
                        'FT_ratio_home':FT_ratio_home,
                        'OREB_home':OREB_home,
                        'REB_home':REB_home,
                        #'AST_home':AST_home,
                        'TOV_home':TOV_home,
                        'STL_home':STL_home,
                       # 'BLK_home':BLK_home,
                       # 'PF_home':PF_home,
                        'PTS_home':PTS_home}

advanced_data_dict = {  'game_ID':game_ID ,
                        'OffRtg_away':OffRtg_away,
                        'DefRtg_away':DefRtg_away,
                        'NetRtg_away':NetRtg_away,
                        'AST_percent_away':AST_percent_away,
                        'AST_div_TO_away':AST_div_TO_away,
                        'AST_Ratio_away':AST_Ratio_away,
                        #'OREB_ratio_away':OREB_ratio_away,
                        'DREB_ratio_away':DREB_ratio_away,
                        'REB_ratio_away':REB_ratio_away,
                        'TO_Ratio_away':TO_Ratio_away,
                        'eFG_ratio_away':eFG_ratio_away,
                        'TS_ratio_away':TS_ratio_away,
                        'USG_ratio_away':USG_ratio_away,
                        'PACE_away':PACE_away,
                        'PIE_away':PIE_away,
                        'OffRtg_home':OffRtg_home,
                        'DefRtg_home':DefRtg_home,
                        'NetRtg_home':NetRtg_home,
                        'AST_percent_home':AST_percent_home,
                        'AST_div_TO_home':AST_div_TO_home,
                        'AST_Ratio_home':AST_Ratio_home,
                       # 'OREB_ratio_home':OREB_ratio_home,
                        'DREB_ratio_home':DREB_ratio_home,
                        'REB_ratio_home':REB_ratio_home,
                        'TO_Ratio_home':TO_Ratio_home,
                        'eFG_ratio_home':eFG_ratio_home,
                        'TS_ratio_home':TS_ratio_home,
                        'USG_ratio_home':USG_ratio_home,
                        'PACE_home':PACE_home,
                        'PIE_home':PIE_home}


misc_data_dict = {      'game_ID':game_ID ,
                        'PTS_OFF_TO_away':PTS_OFF_TO_away,
                        'SEC_PTS_away':SEC_PTS_away,
                        'FBPS_away':FBPS_away,
                        'PITP_away':PITP_away,
                        'BLK_away':BLK_away,
                        'PF_away':PF_away,
                        'PTS_OFF_TO_home':PTS_OFF_TO_home,
                        'SEC_PTS_home':SEC_PTS_home,
                        'FBPS_home':FBPS_home,
                        'PITP_home':PITP_home,
                        'BLK_home':BLK_home,
                        'PF_home':PF_home}


scoring_data_dict ={    'game_ID':game_ID ,
                        'ratio_FGA_2PT_away':ratio_FGA_2PT_away,
                        'ratio_FGA_3PT_away':ratio_FGA_3PT_away,
                        'ratio_PTS_2PT_away':ratio_PTS_2PT_away,
                        'ratio_PTS_2PT_MR_away':ratio_PTS_2PT_MR_away,
                        'ratio_PTS_3PT_away':ratio_PTS_3PT_away,
                        'ratio_PTS_FBPS_away':ratio_PTS_FBPS_away,
                        'ratio_PTS_FT_away':ratio_PTS_FT_away,
                        'ratio_PTS_OFFTO_away':ratio_PTS_OFFTO_away,
                        'ratio_PTS_PITP_away':ratio_PTS_PITP_away,
                        'sec_FGM_ratio_AST_away':sec_FGM_ratio_AST_away,
                        'sec_FGM_ratio_UAST_away':sec_FGM_ratio_UAST_away,
                        'thr_FGM_ratio_AST_away':thr_FGM_ratio_AST_away,
                        'thr_FGM_ratio_UAST_away':thr_FGM_ratio_UAST_away,
                        'FGM_ratio_AST_away':FGM_ratio_AST_away,
                        'FGM_ratio_UAST_away':FGM_ratio_UAST_away,
                        'ratio_FGA_2PT_home':ratio_FGA_2PT_home,
                        'ratio_FGA_3PT_home':ratio_FGA_3PT_home,
                        'ratio_PTS_2PT_home':ratio_PTS_2PT_home,
                        'ratio_PTS_2PT_MR_home':ratio_PTS_2PT_MR_home,
                        'ratio_PTS_3PT_home':ratio_PTS_3PT_home,
                        'ratio_PTS_FBPS_home':ratio_PTS_FBPS_home,
                        'ratio_PTS_FT_home':ratio_PTS_FT_home,
                        'ratio_PTS_OFFTO_home':ratio_PTS_OFFTO_home,
                        'ratio_PTS_PITP_home':ratio_PTS_PITP_home,
                        'sec_FGM_ratio_AST_home':sec_FGM_ratio_AST_home,
                        'sec_FGM_ratio_UAST_home':sec_FGM_ratio_UAST_home,
                        'thr_FGM_ratio_AST_home':thr_FGM_ratio_AST_home,
                        'thr_FGM_ratio_UAST_home':thr_FGM_ratio_UAST_home,
                        'FGM_ratio_AST_home':FGM_ratio_AST_home,
                        'FGM_ratio_UAST_home':FGM_ratio_UAST_home}


fourfactors_data_dict = {'game_ID':game_ID ,
                        'EFG_ratio_away':EFG_ratio_away,
                        'FTA_rate_away':FTA_rate_away,
                        'TO_ratio_away':TO_ratio_away,
                        'OREB_ratio_away':OREB_ratio_away,
                        'EFG_ratio_home':EFG_ratio_home,
                        'FTA_rate_home':FTA_rate_home,
                        'TO_ratio_home':TO_ratio_home,
                        'OREB_ratio_home':OREB_ratio_home}


playertracking_data_dict ={ 'game_ID':game_ID ,
                            'DIST_away':DIST_away,
                            'SPD_away':SPD_away,
                            'TCHS_away':TCHS_away,
                            'PASS_away':PASS_away,
                            'AST_away':AST_away,
                            'SAST_away':SAST_away,
                            #'FTAST_away':FTAST_away,
                            'DFGM_away':DFGM_away,
                            'DFGA_away':DFGA_away,
                            'DFG_ratio_away':DFG_ratio_away,
                            'ORBC_away':ORBC_away,
                            'DRBC_away':DRBC_away,
                            'FG_ration_away':FG_ration_away,
                            'CFGM_away':CFGM_away,
                            'CFGA_away':CFGA_away,
                            'CFG_ratio_away':CFG_ratio_away,
                            'UFGM_away':UFGM_away,
                            'UFGA_away':UFGA_away,
                            'UFG_ratio_away':UFG_ratio_away,
                            'DIST_home':DIST_home,
                            'SPD_home':SPD_home,
                            'TCHS_home':TCHS_home,
                            'PASS_home':PASS_home,
                            'AST_home':AST_home,
                            'SAST_home':SAST_home,
                            #'FTAST_home':FTAST_home,
                            'DFGM_home':DFGM_home,
                            'DFGA_home':DFGA_home,
                            'DFG_ratio_home':DFG_ratio_home,
                            'ORBC_home':ORBC_home,
                            'DRBC_home':DRBC_home,
                            'FG_ration_home':FG_ration_home,
                            'CFGM_home':CFGM_home,
                            'CFGA_home':CFGA_home,
                            'CFG_ratio_home':CFG_ratio_home,
                            'UFGM_home':UFGM_home,
                            'UFGA_home':UFGA_home,
                            'UFG_ratio_home':UFG_ratio_home}


hustle_data_dict = {    'game_ID':game_ID ,
                        'screen_ASS_away':screen_ASS_away,
                        'deflections_away':deflections_away,
                        'loose_balls_recovered_away':loose_balls_recovered_away,
                        'charges_drawn_away':charges_drawn_away,
                        'contest_2PT_shots_away':contest_2PT_shots_away,
                        'contest_3PT_shots_away':contest_3PT_shots_away,
                        'screen_ASS_home':screen_ASS_home,
                        'deflections_home':deflections_home,
                        'loose_balls_recovered_home':loose_balls_recovered_home,
                        'charges_drawn_home':charges_drawn_home,
                        'contest_2PT_shots_home':contest_2PT_shots_home,
                        'contest_3PT_shots_home':contest_3PT_shots_home}

begin = 2

traditional_data_frame = DataFrame(traditional_data_dict).iloc[begin:,]
advanced_data_frame = DataFrame(advanced_data_dict).iloc[begin:,]
misc_data_frame = DataFrame(misc_data_dict).iloc[begin:,]
scoring_data_frame = DataFrame(scoring_data_dict).iloc[begin:,]
fourfactors_data_frame = DataFrame(fourfactors_data_dict).iloc[begin:,]
playertracking_data_frame = DataFrame(playertracking_data_dict).iloc[begin:,]
hustle_data_frame = DataFrame(hustle_data_dict).iloc[begin:,]

csvfile = open('traditional_data_frame.csv', 'w', newline='')  #build a csv file
traditional_data_frame.to_csv('traditional_data_frame.csv')
csvfile = open('advanced_data_frame.csv', 'w', newline='')  #build a csv file
advanced_data_frame.to_csv('advanced_data_frame.csv')
csvfile = open('misc_data_frame.csv', 'w', newline='')  #build a csv file
misc_data_frame.to_csv('misc_data_frame.csv')
csvfile = open('scoring_data_frame.csv', 'w', newline='')  #build a csv file
scoring_data_frame.to_csv('scoring_data_frame.csv')
csvfile = open('fourfactors_data_frame.csv', 'w', newline='')  #build a csv file
fourfactors_data_frame.to_csv('fourfactors_data_frame.csv')
csvfile = open('playertracking_data_frame.csv', 'w', newline='')  #build a csv file
playertracking_data_frame.to_csv('playertracking_data_frame.csv')
csvfile = open('hustle_data_frame.csv', 'w', newline='')  #build a csv file
hustle_data_frame.to_csv('hustle_data_frame.csv')





cnx = create_engine('mysql+pymysql://root:blw3927493@127.0.0.1:3306/nba_1718', echo=False)

traditional_data_frame.to_sql(name='traditional_data_frame', con=cnx, if_exists = 'append', index=False)
advanced_data_frame.to_sql(name='advanced_data_frame', con=cnx, if_exists = 'append', index=False)
misc_data_frame.to_sql(name='misc_data_frame', con=cnx, if_exists = 'append', index=False)
scoring_data_frame.to_sql(name='scoring_data_frame', con=cnx, if_exists = 'append', index=False)
fourfactors_data_frame.to_sql(name='fourfactors_data_frame', con=cnx, if_exists = 'append', index=False)
playertracking_data_frame.to_sql(name='playertracking_data_frame', con=cnx, if_exists = 'append', index=False)
hustle_data_frame.to_sql(name='hustle_data_frame', con=cnx, if_exists = 'append', index=False)




#连接配置信息
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'blw3927493',
    'db':'nba_1718',
    }
# 创建连接
connection = pymysql.connect(**config)

# 使用cursor()方法获取操作游标
cursor = connection.cursor()
# SQL 查询语句
# SQL 查询语句
sql = """ ALTER IGNORE TABLE traditional_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE advanced_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE misc_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE scoring_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE fourfactors_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE playertracking_data_frame
         ADD UNIQUE (game_ID(255));
         ALTER IGNORE TABLE hustle_data_frame
         ADD UNIQUE (game_ID(255));
     """

cursor.execute(sql)