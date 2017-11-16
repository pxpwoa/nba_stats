# nba_features_1.0
import pymysql
import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine


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
sql = """ SELECT traditional_data_frame.*, advanced_data_frame.*,misc_data_frame.*,scoring_data_frame.*,
          fourfactors_data_frame.*,playertracking_data_frame.*,hustle_data_frame.*,line_frame.line_spread,line_frame.line_total
          FROM traditional_data_frame
          INNER JOIN advanced_data_frame ON traditional_data_frame.game_ID=advanced_data_frame.game_ID
          INNER JOIN misc_data_frame ON traditional_data_frame.game_ID=misc_data_frame.game_ID
          INNER JOIN scoring_data_frame ON traditional_data_frame.game_ID=scoring_data_frame.game_ID
          INNER JOIN fourfactors_data_frame ON traditional_data_frame.game_ID=fourfactors_data_frame.game_ID
          INNER JOIN playertracking_data_frame ON traditional_data_frame.game_ID=playertracking_data_frame.game_ID
          INNER JOIN hustle_data_frame ON traditional_data_frame.game_ID=hustle_data_frame.game_ID
          INNER JOIN line_frame ON traditional_data_frame.game_ID=line_frame.game_id
      """

data = pd.read_sql(sql, con=connection)

#csvfile = open('nba_data.csv', 'w', newline='')  #build a csv file
#data.to_csv('nba_data.csv')


data1 = data.replace(to_replace='%', value='', regex=True)
data2 = data1.apply(pd.to_numeric,errors='ignore') # 不知道为什么一些数据被四舍五入去掉了小数点，让数据失去一些精度
nba = data2.drop(['SPD_home','SPD_away'], 1)  #空值
nba = nba.loc[:,~nba.columns.duplicated()] #去掉重复列

if '' in nba.values:
    while True:
        print("there are NAN in the data!")


history_window = 5


nba_teams = ['BKN', 'DET', 'ORL', 'ATL', 'OKC', 'MIN', 'NYK', 'GSW', 'CHI', 'PHX',
            'POR', 'MIL', 'IND', 'CLE', 'MIA', 'LAL', 'HOU', 'SAS', 'NOP', 'BOS',
            'LAC', 'DAL', 'MEM', 'WAS', 'DEN', 'UTA', 'TOR', 'CHA', 'PHI', 'SAC']
nba_data =dict.fromkeys(nba_teams)
nba_features =dict.fromkeys(nba_teams)

for team in nba_data.keys():
    team_data = nba.loc[(nba['team_away'] == team) | (nba['team_home'] == team),:].sort_values(by='game_ID',ascending = True) # selsct the rows of the team
    team_data.game_ID = team_data.game_ID.shift(-1) # shift game_ID for history_window
    team_data = team_data.dropna()
    team_data['H_or_W'] = np.where(team_data['team_home']== team, 1, 0) # the home number in the window
    list_rows = []
    game_ID = team_data['game_ID'].tolist()
    nba_data[team] = dict.fromkeys(game_ID)
    for gid in game_ID:
        row = team_data.loc[team_data['game_ID'] == gid]
        the_home = row.filter(regex=(".*_home.*"))
        the_away = row.filter(regex=(".*_away.*"))
        the_other = row.loc[:,['date','game_ID','H_or_W','team_home','team_away']]
        if row['H_or_W'].iloc[0]:  # separate the data from the team and the oppo
            the_home.columns = [x.replace('_home', '_off') for x in row.filter(regex=(".*_home.*")).columns.tolist()]
            the_away.columns = [x.replace('_away', '_def') for x in row.filter(regex=(".*_away.*")).columns.tolist()]
        else:
            the_away.columns = [x.replace('_home', '_off') for x in row.filter(regex=(".*_home.*")).columns.tolist()]
            the_home.columns = [x.replace('_away', '_def') for x in row.filter(regex=(".*_away.*")).columns.tolist()]

        row_reconcat = pd.concat([the_home,the_away],axis = 1)
        off_data =   row_reconcat.filter(regex=(".*_off.*")).drop('team_off',axis = 1)
        def_data =   row_reconcat.filter(regex=(".*_def.*")).drop('team_def',axis = 1)
        off_data.columns = [x.replace('_off', 'dif') for x in off_data.columns.tolist()]
        def_data.columns = [x.replace('_def', 'dif') for x in def_data.columns.tolist()]
        dif_data = off_data.subtract(def_data, fill_value=0)
        other_data =   row.loc[:,['date','game_ID','H_or_W']]
        list_rows.append(pd.concat([other_data,dif_data],axis = 1))
    nba_features[team] = pd.concat(list_rows).rolling(min_periods=1, window=history_window).mean()
    #nba_features[team] = nba_features[team].set_index('game_ID').T.to_dict('list')

game_ID = nba['game_ID'].tolist()
features_index = nba.set_index('game_ID')
list_features = []

for gid in game_ID:
    team_away = features_index.loc[gid,'team_away']
    team_home = features_index.loc[gid,'team_home']
    other = nba.loc[nba['game_ID'] == gid].loc[:,['game_ID','date','SFL','team_away','team_home','PTS_away','PTS_home']].set_index('game_ID')
    if gid in nba_features[team_away]['game_ID'].tolist():
        features_away = nba_features[team_away].loc[nba_features[team_away]['game_ID'] == gid].set_index('game_ID')
        features_away.columns = [str(col) + '_away' for col in features_away.columns]
        features_home = nba_features[team_home].loc[nba_features[team_home]['game_ID'] == gid].set_index('game_ID')
        features_home.columns = [str(col) + '_home' for col in features_home.columns]
        list_features.append(pd.concat([other,features_away,features_home],axis = 1))
    else:
        continue

features_concat = pd.concat(list_features).sort_index().dropna().drop(['TO_Ratiodif_away','TO_Ratiodif_home','EFG_ratiodif_away','EFG_ratiodif_home'],axis = 1)
features_concat['spread_home'] = features_concat['PTS_home'] - features_concat['PTS_away']

cnx = create_engine('mysql+pymysql://root:blw3927493@127.0.0.1:3306/nba_1718_features', echo=False)

features_concat.to_sql(name='features_concat', con=cnx, if_exists = 'append', index=False)

csvfile = open('features_concat.csv', 'w', newline='')  #build a csv file
features_concat.to_csv('features_concat.csv')