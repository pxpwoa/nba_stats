# wnba_features_1.0
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
sql = """ SELECT traditional_data_frame.*, advanced_data_frame.*,fourfactors_data_frame.*,wnba_odds_frame.*
          FROM traditional_data_frame
          INNER JOIN advanced_data_frame ON traditional_data_frame.game_ID=advanced_data_frame.game_ID
          INNER JOIN fourfactors_data_frame ON traditional_data_frame.game_ID=fourfactors_data_frame.game_ID
          INNER JOIN wnba_odds_frame ON traditional_data_frame.game_ID=wnba_odds_frame.game_ID
      """

data = pd.read_sql(sql, con=connection)

connection.close()

data = data.replace(to_replace='%', value='', regex=True)
data = data.replace(to_replace='Ev', value='0', regex=True)
wnba = data.apply(pd.to_numeric,errors='ignore')
wnba = wnba.loc[:,~wnba.columns.duplicated()]

if '' in wnba:
    print('nonononono!')



#X_int = wnba.drop(['PTS_home','PTS_away','game_ID','date','team_away','team_home'], 1)

Y_spread = wnba['PTS_home'].values - wnba['PTS_away'].values
Y_total = wnba['PTS_home'].values + wnba['PTS_away'].values



history_window = 2



wnba_teams = ['ATL', 'MIN',  'CHI', 'PHO', 'IND',  'LAS', 'SAN','NYL', 'CON',
             'DAL',  'WAS', 'SEA']
wnba_data =dict.fromkeys(wnba_teams)
wnba_features =dict.fromkeys(wnba_teams)
game_features =dict.fromkeys(['off','def','other'])
for team in wnba_data.keys():
    #team = 'ATL'
    team_data = wnba.loc[(wnba['team_away'] == team) | (wnba['team_home'] == team),:].sort_values(by='game_ID',ascending = True) # selsct the rows of the team
    team_data.game_ID = team_data.game_ID.shift(-1) # shift game_ID for history_window
    team_data = team_data.dropna()
    team_data['H_or_W'] = np.where(team_data['team_home']== team, 1, 0) # the home number in the window
    list_rows = []
    game_ID = team_data['game_ID'].tolist()
    wnba_data[team] = dict.fromkeys(game_ID)
    for gid in game_ID:
        row = team_data.loc[team_data['game_ID'] == gid]
        the_home = row.filter(regex=(".*_home.*"))
        the_away = row.filter(regex=(".*_away.*"))
        the_other = row.loc[:,['Date','game_ID','H_or_W','team_home','team_away']]
        if row['H_or_W'].iloc[0]:
            the_home.columns = [x.replace('_home', '_off') for x in row.filter(regex=(".*_home.*")).columns.tolist()]
            the_away.columns = [x.replace('_away', '_def') for x in row.filter(regex=(".*_away.*")).columns.tolist()]
        else:
            the_away.columns = [x.replace('_away', '_off') for x in row.filter(regex=(".*_away.*")).columns.tolist()]
            the_home.columns = [x.replace('_home', '_def') for x in row.filter(regex=(".*_home.*")).columns.tolist()]

        row_reconcat = pd.concat([the_home,the_away],axis = 1)
        off_data =   row_reconcat.filter(regex=(".*_off.*")).drop('team_off',axis = 1)
        def_data =   row_reconcat.filter(regex=(".*_def.*")).drop('team_def',axis = 1)
        off_data.columns = [x.replace('_off', 'dif') for x in off_data.columns.tolist()]
        def_data.columns = [x.replace('_def', 'dif') for x in def_data.columns.tolist()]
        dif_data = off_data.subtract(def_data, fill_value=0)
        other_data =   row.loc[:,['Date','game_ID','H_or_W']]
        list_rows.append(pd.concat([other_data,dif_data],axis = 1))
    wnba_features[team] = pd.concat(list_rows).rolling(min_periods=1, window=history_window).mean()
   #wnba_features[team] = wnba_features[team].set_index('game_ID').T.to_dict('list')

game_ID = wnba['game_ID'].tolist()
features_index = wnba.set_index('game_ID')
list_features = []

for gid in game_ID:
    team_away = features_index.loc[gid,'team_away']
    team_home = features_index.loc[gid,'team_home']
    other = wnba.loc[wnba['game_ID'] == gid].loc[:,['game_ID','Date','line_spread','line_total','team_away','team_home','PTS_away','PTS_home']].set_index('game_ID')
    if gid in wnba_features[team_away]['game_ID'].tolist():
        features_away = wnba_features[team_away].loc[wnba_features[team_away]['game_ID'] == gid].set_index('game_ID')
        features_away.columns = [str(col) + '_away' for col in features_away.columns]
        features_home = wnba_features[team_home].loc[wnba_features[team_home]['game_ID'] == gid].set_index('game_ID')
        features_home.columns = [str(col) + '_home' for col in features_home.columns]
        list_features.append(pd.concat([other,features_away,features_home],axis = 1))
    else:
        continue

features_concat = pd.concat(list_features).sort_index().dropna()
features_concat['spread'] = features_concat['PTS_home'] - features_concat['PTS_away']
features_concat['total'] = features_concat['PTS_home'] + features_concat['PTS_away']

features = features_concat.drop(['Date_away','Date_home','Date','team_away','team_home','PTS_away','PTS_home','spread','total'],axis = 1)

X_history = features.values
Y_spread = features_concat['spread'].values
line_spread = features_concat['line_spread'].values
Y_total = features_concat['total'].values
line_total = features_concat['line_total'].values

ohe = OneHotEncoder(categorical_features = [0])       
team_le = LabelEncoder()
date_le = LabelEncoder()
stdsc = StandardScaler()
vt = VarianceThreshold(threshold=(.8 * (1 - .8)))
sp = SelectPercentile(score_func = mutual_info_regression, percentile=10)
reg = linear_model.Lasso(alpha = 0.2).fit(X_history,Y_spread)
model = SelectFromModel(reg, prefit=True)


team_le.fit(features_concat['team_away'])
#pd.get_dummies(df[['away_team','home_team']])
features_concat['team_away'] = ohe.fit_transform(team_le.transform(features_concat['team_away']))
features_concat['team_home'] = ohe.fit_transform(team_le.transform(features_concat['team_home']))
X_team = features_concat.loc[:,['team_away','team_home']].values

date_test = datetime.datetime(2017,5,31)
date_end = datetime.datetime(2017,6,10)
features_concat['Date'] = pd.to_datetime(features_concat['Date'])
scores_date= []

#while not( date_test == date_end):
scores = [[],[]]
date_test += datetime.timedelta(days=1)
# Divide up the data
train_len = features_concat.loc[features_concat['Date'] <= date_test].shape[0]
train_len = 30
vt = VarianceThreshold(threshold=(.8 * (1 - .8)))
sp = SelectPercentile(score_func = mutual_info_regression, percentile=45)
X_history_new = vt.fit_transform(X_history)
X_history_new = sp.fit_transform(X_history_new,Y_spread)
reg = linear_model.Lasso(alpha = 0.35).fit(X_history_new,Y_spread)
model = SelectFromModel(reg, prefit=True)

X_history_new = model.transform(X_history_new)

X_train = X_history_new[:train_len]
X_test = X_history_new[train_len:]
Y_train = Y_spread[:train_len]
Y_test = Y_spread[train_len:]
line_test = [-x for x in line_spread[train_len:]]

X_train_std = stdsc.fit_transform(X_train)   
X_test_std = stdsc.transform(X_test)
svr_rbf = SVR(kernel='rbf')
reg = linear_model.BayesianRidge()
# FIT
svr_rbf.fit(X_train_std, Y_train)
reg.fit(X_train_std, Y_train)
# Predictions
svr_deltas = svr_rbf.predict(X_test_std)
brr_deltas = reg.predict(X_test_std)
for m,models in enumerate([svr_deltas,brr_deltas]):
    money_pot = 1
    bets_won_away = 0
    bets_won_home = 0
    num_games = 0
    for i, pred in enumerate(models):
        betting_line = line_test[i]
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
    print(scores[m][-1])
scores_date.append(scores)















