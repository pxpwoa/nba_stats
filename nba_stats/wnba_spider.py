#wnba_spider1.0
import wnba_scrapy
from pandas import DataFrame
import datetime
import pymysql
from sqlalchemy import create_engine

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
PF_away = []
STL_away = []
TOV_away = []
BS_away = []
BA_away = []
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
PF_home = []
STL_home = []
TOV_home = []
BS_home = []
BA_home = []
PTS_home = []

POSS_away = []
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
POSS_home = []
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

EFG_ratio_away = []
FTA_rate_away = []
TO_ratio_away = []
OREB_ratio_away = []
EFG_ratio_home = []
FTA_rate_home = []
TO_ratio_home = []
OREB_ratio_home = []

team_home = []
team_away = []
game_ID = []
date = []

mon = 9
year =2015
mon_end = 4
while not( mon == mon_end):

    (game_link,game_id,game_date)  = wnba_scrapy.gameid(mon,year)
    mon -= 1
#    game_id = game_id[12:]
#    game_link = game_link[12:]
#    game_date = game_date[12:]
    for i in range(len(game_id)):       
        (traditional_data,advanced_data,fourfactors_data,team_name) =wnba_scrapy.score_box_data(game_link[i])

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
        AST_away.append(traditional_data[12])
        PF_away.append(traditional_data[13])
        STL_away.append(traditional_data[14])
        TOV_away.append(traditional_data[15])
        BS_away.append(traditional_data[16])
        BA_away.append(traditional_data[17])
        PTS_away.append(traditional_data[18])
        FGM_home.append(traditional_data[19])
        FGA_home.append(traditional_data[20])
        FG_ratio_home.append(traditional_data[21])
        threePM_home.append(traditional_data[22])
        threePA_home.append(traditional_data[23])
        threeP_ratio_home.append(traditional_data[24])
        FTM_home.append(traditional_data[25])
        FTA_home.append(traditional_data[26])
        FT_ratio_home.append(traditional_data[27])
        OREB_home.append(traditional_data[28])
        DREB_home.append(traditional_data[29])
        REB_home.append(traditional_data[30])
        AST_home.append(traditional_data[31])
        PF_home.append(traditional_data[32])
        STL_home.append(traditional_data[33])
        TOV_home.append(traditional_data[34])
        BS_home.append(traditional_data[35])
        BA_home.append(traditional_data[36])
        PTS_home.append(traditional_data[37])

        POSS_away.append(advanced_data[0])
        OffRtg_away.append(advanced_data[1])
        DefRtg_away.append(advanced_data[2])
        NetRtg_away.append(advanced_data[3])
        AST_percent_away.append(advanced_data[4])
        AST_div_TO_away.append(advanced_data[5])
        OREB_ratio_away.append(advanced_data[6])
        DREB_ratio_away.append(advanced_data[7])
        REB_ratio_away.append(advanced_data[8])
        TO_Ratio_away.append(advanced_data[9])
        eFG_ratio_away.append(advanced_data[10])
        TS_ratio_away.append(advanced_data[11])
        USG_ratio_away.append(advanced_data[12])
        PACE_away.append(advanced_data[13])
        PIE_away.append(advanced_data[14])
        POSS_home.append(advanced_data[15])
        OffRtg_home.append(advanced_data[16])
        DefRtg_home.append(advanced_data[17])
        NetRtg_home.append(advanced_data[18])
        AST_percent_home.append(advanced_data[19])
        AST_div_TO_home.append(advanced_data[20])
        OREB_ratio_home.append(advanced_data[21])
        DREB_ratio_home.append(advanced_data[22])
        REB_ratio_home.append(advanced_data[23])
        TO_Ratio_home.append(advanced_data[24])
        eFG_ratio_home.append(advanced_data[25])
        TS_ratio_home.append(advanced_data[26])
        USG_ratio_home.append(advanced_data[27])
        PACE_home.append(advanced_data[28])
        PIE_home.append(advanced_data[29])

        
        FTA_rate_away.append(fourfactors_data[1])
        FTA_rate_home.append(fourfactors_data[5])


        team_away.append(team_name[0])
        team_home.append(team_name[1])
        game_ID.append(game_id[i])
        date.append(game_date[i])



traditional_data_dict ={'team_home':team_home ,
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
                        'AST_away':AST_away,
                        'TOV_away':TOV_away,
                        'STL_away':STL_away,
                        'BS_away':BS_away,
                        'BA_away':BA_away,
                        'PF_away':PF_away,
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
                        'AST_home':AST_home,
                        'TOV_home':TOV_home,
                        'STL_home':STL_home,
                        'BA_home':BA_home,
                        'BS_home':BS_home,
                        'PF_home':PF_home,
                        'PTS_home':PTS_home,
                        'Date': date}


advanced_data_dict = {  'game_ID':game_ID ,
                        'POSS_away':POSS_away ,
                        'OffRtg_away':OffRtg_away,
                        'DefRtg_away':DefRtg_away,
                        'NetRtg_away':NetRtg_away,
                        'AST_percent_away':AST_percent_away,
                        'AST_div_TO_away':AST_div_TO_away,
                        #'AST_Ratio_away':AST_Ratio_away,
                        'OREB_ratio_away':OREB_ratio_away,
                        'DREB_ratio_away':DREB_ratio_away,
                        'REB_ratio_away':REB_ratio_away,
                        'TO_Ratio_away':TO_Ratio_away,
                        'eFG_ratio_away':eFG_ratio_away,
                        'TS_ratio_away':TS_ratio_away,
                        'USG_ratio_away':USG_ratio_away,
                        'PACE_away':PACE_away,
                        'PIE_away':PIE_away,
                        'POSS_home':POSS_home ,
                        'OffRtg_home':OffRtg_home,
                        'DefRtg_home':DefRtg_home,
                        'NetRtg_home':NetRtg_home,
                        'AST_percent_home':AST_percent_home,
                        'AST_div_TO_home':AST_div_TO_home,
                        #'AST_Ratio_home':AST_Ratio_home,
                        'OREB_ratio_home':OREB_ratio_home,
                        'DREB_ratio_home':DREB_ratio_home,
                        'REB_ratio_home':REB_ratio_home,
                        'TO_Ratio_home':TO_Ratio_home,
                        'eFG_ratio_home':eFG_ratio_home,
                        'TS_ratio_home':TS_ratio_home,
                        'USG_ratio_home':USG_ratio_home,
                        'PACE_home':PACE_home,
                        'PIE_home':PIE_home}

fourfactors_data_dict = {'game_ID':game_ID ,
                        'FTA_rate_away':FTA_rate_away,
                        'FTA_rate_home':FTA_rate_home
                        }


traditional_data_frame = DataFrame(traditional_data_dict).iloc[14:,]
advanced_data_frame = DataFrame(advanced_data_dict).iloc[14:,]
fourfactors_data_frame = DataFrame(fourfactors_data_dict).iloc[14:,]






cnx = create_engine('mysql+pymysql://root:blw3927493@127.0.0.1:3306/wnba_stats', echo=False)

traditional_data_frame.to_sql(name='traditional_data_frame', con=cnx, if_exists = 'append', index=False)
advanced_data_frame.to_sql(name='advanced_data_frame', con=cnx, if_exists = 'append', index=False)
fourfactors_data_frame.to_sql(name='fourfactors_data_frame', con=cnx, if_exists = 'append', index=False)


#连接配置信息
config = {
     'host':'127.0.0.1',
     'port':3306,
     'user':'root',
     'password':'blw3927493',
     'db':'wnba_stats',
     }
# 创建连接
connection = pymysql.connect(**config)

# 使用cursor()方法获取操作游标
cursor = connection.cursor()
# SQL 查询语句
sql = """ ALTER IGNORE TABLE traditional_data_frame
          ADD UNIQUE (game_ID(255));
          ALTER IGNORE TABLE advanced_data_frame
          ADD UNIQUE (game_ID(255));
          ALTER IGNORE TABLE fourfactors_data_frame
          ADD UNIQUE (game_ID(255));
      """

cursor.execute(sql)
