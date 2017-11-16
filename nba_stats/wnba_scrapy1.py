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
     'db':'wwnba_stats',
     }
# 创建连接
connection = pymysql.connect(**config)

# 使用cursor()方法获取操作游标
cursor = connection.cursor()
# SQL 查询语句
sql = """ SELECT traditional_data_frame.*, advanced_data_frame.*,fourfactors_data_frame.*,pregame.SFL
          FROM traditional_data_frame
          INNER JOIN advanced_data_frame ON traditional_data_frame.game_ID=advanced_data_frame.game_ID
          INNER JOIN fourfactors_data_frame ON traditional_data_frame.game_ID=fourfactors_data_frame.game_ID
          INNER JOIN pregame ON traditional_data_frame.game_ID=pregame.game_ID
      """

data = pd.read_sql(sql, con=connection)

connection.close()

data = data.replace(to_replace='%', value='', regex=True)
data = data.convert_objects(convert_numeric=True)
wnba = data.drop(['SPD_home','SPD_away','SFL'], 1)
wnba = wnba.loc[:,~wnba.columns.duplicated()]

if '' in wnba.values:
    while True:
        print("there are NAN in the data!")



X_int = wnba.drop(['PTS_home','PTS_away','game_ID','date','team_away','team_home'], 1)

Y_spread = wnba['PTS_home'].values - wnba['PTS_away'].values
Y_total = wnba['PTS_home'].values + wnba['PTS_away'].values



spread_line = data['SFL'].values
history_window = 5



wnba_teams = ['BKN', 'DET', 'ORL', 'ATL', 'OKC', 'MIN', 'NYK', 'GSW', 'CHI', 'PHX',
            'POR', 'MIL', 'IND', 'CLE', 'MIA', 'LAL', 'HOU', 'SAS', 'NOP', 'BOS',
            'LAC', 'DAL', 'MEM', 'WAS', 'DEN', 'UTA', 'TOR', 'CHA', 'PHI', 'SAC']
wnba_data =dict.fromkeys(wnba_teams)
wnba_features =dict.fromkeys(wnba_teams)
game_features =dict.fromkeys(['off','def','other'])
for team in wnba_data.keys():
    team_data = wnba.loc[(wnba['team_away'] == team) | (wnba['team_home'] == team),:].sort('game_ID',ascending = True)
    team_data.PTS_home = team_data.PTS_home.shift(-1)
    team_data.PTS_away = team_data.PTS_away.shift(-1)
    team_data = team_data.dropna()
    team_data['H_or_W'] = np.where(team_data['team_home']== team, 1, 0)
    list_rows = []
    game_ID = team_data['game_ID'].tolist()
    wnba_data[team] = dict.fromkeys(game_ID)
    for gid in game_ID:
        row = team_data.loc[team_data['game_ID'] == gid]
        the_home = row.filter(regex=(".*_home.*"))
        the_away = row.filter(regex=(".*_away.*"))
        the_other = row.loc[:,['date','game_ID','H_or_W','team_home','team_away']]
        if row['H_or_W'].iloc[0]:
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
    wnba_features[team] = pd.concat(list_rows).rolling(min_periods=1, window=history_window).mean()
    wnba_features[team] = wnba_features[team].set_index('game_ID').T.to_dict('list')

for x in wnba_data:
    wnba_teams.remove(x)
    for y in wnba_teams:
        wnba_features_list.append(pd.merge(wnba_data[x],wnba_data[y],on='game_ID'))

wnba_features = pd.concat(wnba_features_list)

















ohe = OneHotEncoder(categorical_features = [0])       
team_le = LabelEncoder()
date_le = LabelEncoder()
stdsc = StandardScaler()
vt = VarianceThreshold(threshold=(.8 * (1 - .8)))
sp = SelectPercentile(score_func = mutual_info_regression, percentile=90)
reg = linear_model.Lasso(alpha = 0.05).fit(X_history,Y_spread)
model = SelectFromModel(reg, prefit=True)

X_team = wnba.loc[:,['team_away','team_home']].values

team_le.fit(wnba['team_away'])
#pd.get_dummies(df[['away_team','home_team']])
wnba['team_away'] = ohe.fit_transform(team_le.transform(wnba['team_away']))
wnba['team_home'] = ohe.fit_transform(team_le.transform(wnba['team_home']))


date = datetime.datetime(2017,4,1)
date_end = datetime.datetime(2017,4,9)
wnba['date'] = pd.to_datetime(wnba['date'])


while not( date == date_end):
    scores = [[],[]]
    date += datetime.timedelta(days=1)
    # Divide up the data
    train_len = wnba.loc[wnba['date'] <= date].shape[1]

    X_history_new = vt.fit_transform(X_history)
    X_history_new = sp.fit_transform(X_history,Y_spread)
    X_history_new = model.transform(X_history)

    X_train = X_history_new[:train_len]
    X_test = X_history_new[train_len:]
    Y_train = Y_spread[:train_len]
    Y_test = Y_spread[train_len:]

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
            betting_line = spread_line[i]
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
        scores[m].append((bets_won * 1.0/num_games, money_pot, bets_won_under, bets_won_over))

















