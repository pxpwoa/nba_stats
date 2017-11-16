# nba_features_1.0
import pymysql
import pandas as pd
import numpy as np
import datetime
from functools import reduce
from collections import defaultdict, deque
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import mutual_info_regression
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import SVR
from sklearn import linear_model
from sklearn.ensemble import ExtraTreesRegressor,RandomForestRegressor


#连接配置信息
config = {
     'host':'127.0.0.1',
     'port':3306,
     'user':'root',
     'password':'blw3927493',
     'db':'nba_stats',
     }
# 创建连接
connection = pymysql.connect(**config)

# 使用cursor()方法获取操作游标
cursor = connection.cursor()
# SQL 查询语句
sql = """ SELECT traditional_data_frame.*, advanced_data_frame.*,misc_data_frame.*,scoring_data_frame.*,
          fourfactors_data_frame.*,playertracking_data_frame.*,hustle_data_frame.*,pregame.SFL
          FROM traditional_data_frame
          INNER JOIN advanced_data_frame ON traditional_data_frame.game_ID=advanced_data_frame.game_ID
          INNER JOIN misc_data_frame ON traditional_data_frame.game_ID=misc_data_frame.game_ID
          INNER JOIN scoring_data_frame ON traditional_data_frame.game_ID=scoring_data_frame.game_ID
          INNER JOIN fourfactors_data_frame ON traditional_data_frame.game_ID=fourfactors_data_frame.game_ID
          INNER JOIN playertracking_data_frame ON traditional_data_frame.game_ID=playertracking_data_frame.game_ID
          INNER JOIN hustle_data_frame ON traditional_data_frame.game_ID=hustle_data_frame.game_ID
          INNER JOIN pregame ON traditional_data_frame.game_ID=pregame.game_ID
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
        other_data =   row.loc[:,['date','game_ID','H_or_W']]
        list_rows.append(pd.concat([other_data,off_data,def_data],axis = 1))
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

features_concat = pd.concat(list_features).sort_index().dropna()
features_concat['spread_home'] = features_concat['PTS_home'] - features_concat['PTS_away']

features = features_concat.drop(['date_away','date_home','date','team_away','team_home','PTS_away','PTS_home','spread_home'],axis = 1)

X_history = features.values
Y_spread = features_concat['spread_home'].values
spread_line = features_concat['SFL'].values

ohe = OneHotEncoder(categorical_features = [0])       
team_le = LabelEncoder()
date_le = LabelEncoder()
stdsc = StandardScaler()
vt = VarianceThreshold(threshold=(.8 * (1 - .8)))
sp = SelectPercentile(score_func = mutual_info_regression, percentile=90)
reg = linear_model.Lasso(alpha = 0.05).fit(X_history,Y_spread)
model = SelectFromModel(reg, prefit=True)


team_le.fit(features_concat['team_away'])
#pd.get_dummies(df[['away_team','home_team']])
features_concat['team_away'] = ohe.fit_transform(team_le.transform(features_concat['team_away']))
features_concat['team_home'] = ohe.fit_transform(team_le.transform(features_concat['team_home']))
X_team = features_concat.loc[:,['team_away','team_home']].values

date_test = datetime.datetime(2017,2,1)
date_end = datetime.datetime(2017,4,9)
features_concat['date'] = pd.to_datetime(features_concat['date'])
scores_date= []

#while not( date_test == date_end):
scores = [[],[],[],[]]
date_test += datetime.timedelta(days=1)
# Divide up the data
train_len = features_concat.loc[features_concat['date'] <= date_test].shape[0]

X_history_new = vt.fit_transform(X_history)
X_history_new = sp.fit_transform(X_history,Y_spread)
X_history_new = model.transform(X_history)
X_history_new = X_history
X_train = X_history_new[:train_len]
X_test = X_history_new[train_len:]
Y_train = Y_spread[:train_len]
Y_test = Y_spread[train_len:]
spread_line_test = spread_line[train_len:]

X_train_std = stdsc.fit_transform(X_train)   
X_test_std = stdsc.transform(X_test)
svr_rbf = SVR(kernel='rbf')
reg = linear_model.BayesianRidge()
etree = ExtraTreesRegressor()
rtree = RandomForestRegressor()
# FIT
svr_rbf.fit(X_train_std, Y_train)
reg.fit(X_train_std, Y_train)
etree.fit(X_train_std, Y_train)
rtree.fit(X_train_std, Y_train)
# Predictions
svr_deltas = svr_rbf.predict(X_test_std)
brr_deltas = reg.predict(X_test_std)
etree_deltas = etree.predict(X_test_std)
rtree_deltas = rtree.predict(X_test_std)
for m,models in enumerate([svr_deltas,brr_deltas,etree_deltas,rtree_deltas]):
    money_pot = 1
    bets_won_away = 0
    bets_won_home = 0
    num_games = 0
    for i, pred in enumerate(models):
        betting_line = spread_line_test[i]
        actual_score = Y_test[i]
        if pred < betting_line and actual_score < betting_line:
            bets_won_away += 1
            money_pot += .93*money_pot/2.0
        elif pred > betting_line and actual_score > betting_line:
            bets_won_home += 1
            money_pot += .93*money_pot/2.0
        else:
            money_pot -= money_pot/2.0
        num_games += 1
        bets_won = bets_won_away + bets_won_home
    scores[m].append((bets_won * 1.0/num_games, money_pot, bets_won_home, bets_won_away))
scores_date.append(scores)

















