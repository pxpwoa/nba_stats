traditional_rows =['BKN', 'DET', 'ORL', 'ATL', 'OKC', 'MIN', 'NYK', 'GSW', 'CHI', 'PHX',
            'POR', 'MIL', 'IND', 'CLE', 'MIA', 'LAL', 'HOU', 'SAS', 'NOP', 'BOS',
            'LAC', 'DAL', 'MEM', 'WAS', 'DEN', 'UTA', 'TOR', 'CHA', 'PHI', 'SAC']

for i in range(len(traditional_rows)):

    print ('\''+traditional_rows[i]+'\':'+traditional_rows[i]+',')


for i in range(len(traditional_rows)):

    print (traditional_rows[i]+'.append(traditional_rows['+str(i)+'])')


advanced_rows = [
'OffRtg_away' ,
'DefRtg_away' ,
'NetRtg_away' ,
'AST_ratio_away' ,
'AST_div_TO_away' ,
'AST_Ratio_away' ,
'OREB_ratio_away' ,
'DREB_ratio_away' ,
'REB_ratio_away' ,
'TO_Ratio_away' ,
'eFG_ratio_away' ,
'TS_ratio_away' ,
'USG_ratio_away' ,
'PACE_away' ,
'PIE_away' ,
'OffRtg_home' ,
'DefRtg_home' ,
'NetRtg_home' ,
'AST_ratio_home' ,
'AST_div_TO_home' ,
'AST_Ratio_home' ,
'OREB_ratio_home' ,
'DREB_ratio_home' ,
'REB_ratio_home' ,
'TO_Ratio_home' ,
'eFG_ratio_home' ,
'TS_ratio_home' ,
'USG_ratio_home' ,
'PACE_home' ,
'PIE_home' ]

for i in range(len(advanced_rows)):

    print ('\''+advanced_rows[i]+'\':'+advanced_rows[i]+',')


for i in range(len(advanced_rows)):

    print (advanced_rows[i]+'.append(advanced_rows['+str(i)+'])')

misc_rows = [
'PTS_OFF_TO_away' ,
'SEC_PTS_away' ,
'FBPS_away' ,
'PITP_away' ,
'BLK_away' ,
'PF_away' ,
'PTS_OFF_TO_home' ,
'SEC_PTS_home' ,
'FBPS_home' ,
'PITP_home' ,
'BLK_home' ,
'PF_home' ]
'
for i in range(len(advanced_rows)):

    print ('\''+advanced_rows[i]+'\':'+advanced_rows[i]+',')


for i in range(len(advanced_rows)):

    print (advanced_rows[i]+'.append(advanced_rows['+str(i)+'])')


scoring_rows = [
'ratio_FGA_2PT_away' ,
'ratio_FGA_3PT_away' ,
'ratio_PTS_2PT_away' ,
'ratio_PTS_2PT_MR_away' ,
'ratio_PTS_3PT_away' ,
'ratio_PTS_FBPS_away' ,
'ratio_PTS_FT_away' ,
'ratio_PTS_OFFTO_away' ,
'ratio_PTS_PITP_away' ,
'sec_FGM_ratio_AST_away' ,
'sec_FGM_ratio_UAST_away' ,
'thr_FGM_ratio_AST_away' ,
'thr_FGM_ratio_UAST_away' ,
'FGM_ratio_AST_away' ,
'FGM_ratio_UAST_away' ,
'ratio_FGA_2PT_home' ,
'ratio_FGA_3PT_home' ,
'ratio_PTS_2PT_home' ,
'ratio_PTS_2PT_MR_home' ,
'ratio_PTS_3PT_home' ,
'ratio_PTS_FBPS_home' ,
'ratio_PTS_FT_home' ,
'ratio_PTS_OFFTO_home' ,
'ratio_PTS_PITP_home' ,
'sec_FGM_ratio_AST_home' ,
'sec_FGM_ratio_UAST_home' ,
'thr_FGM_ratio_AST_home' ,
'thr_FGM_ratio_UAST_home' ,
'FGM_ratio_AST_home' ,
'FGM_ratio_UAST_home' ]

for i in range(len(scoring_rows)):

    print ('\''+scoring_rows[i]+'\':'+scoring_rows[i]+',')


for i in range(len(scoring_rows)):

    print (scoring_rows[i]+'.append(scoring_rows['+str(i)+'])')

fourfactors_rows = [
'EFG_ratio_away' ,
'FTA_rate_away' ,
'TO_ratio_away' ,
'OREB_ratio_away' ,
'EFG_ratio_home' ,
'FTA_rate_home' ,
'TO_ratio_home' ,
'OREB_ratio_home' ]
'
for i in range(len(fourfactors_rows)):

    print ('\''+fourfactors_rows[i]+'\':'+fourfactors_rows[i]+',')


for i in range(len(fourfactors_rows)):

    print (fourfactors_rows[i]+'.append(fourfactors_rows['+str(i)+'])')

playtracking_rows =[
'DIST_away' ,
'SPD_away' ,
'TCHS_away' ,
'PASS_away' ,
'AST_away' ,
'SAST_away' ,
'FTAST_away' ,
'DFGM_away' ,
'DFGA_away' ,
'DFG_ratio_away' ,
'ORBC_away' ,
'DRBC_away' ,
'FG_ration_away' ,
'CFGM_away' ,
'CFGA_away' ,
'CFG_ratio_away' ,
'UFGM_away' ,
'UFGA_away' ,
'UFG_ratio_away' ,
'DIST_home' ,
'SPD_home' ,
'TCHS_home' ,
'PASS_home' ,
'AST_home' ,
'SAST_home' ,
'FTAST_home' ,
'DFGM_home' ,
'DFGA_home' ,
'DFG_ratio_home' ,
'ORBC_home' ,
'DRBC_home' ,
'FG_ration_home' ,
'CFGM_home' ,
'CFGA_home' ,
'CFG_ratio_home' ,
'UFGM_home' ,
'UFGA_home' ,
'UFG_ratio_home' ]
'
for i in range(len(playtracking_rows)):

    print ('\''+playtracking_rows[i]+'\':'+playtracking_rows[i]+',')


for i in range(len(playtracking_rows)):

    print (playtracking_rows[i]+'.append(playtracking_rows['+str(i)+'])')



hustle_rows =[
'screen_ASS_away' ,
'deflections_away' ,
'loose_balls_recovered_away' ,
'charges_drawn_away' ,
'contest_2PT_shots_away' ,
'contest_3PT_shots_away' ,
'screen_ASS_home' ,
'deflections_home' ,
'loose_balls_recovered_home' ,
'charges_drawn_home' ,
'contest_2PT_shots_home' ,
'contest_3PT_shots_home' ]

for i in range(len(hustle_rows)):

    print ('\''+hustle_rows[i]+'\':'+hustle_rows[i]+',')


for i in range(len(hustle_rows)):

    print (hustle_rows[i]+'.append(hustle_rows['+str(i)+'])')
