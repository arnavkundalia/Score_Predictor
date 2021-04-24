import pandas as pd
df = pd.read_csv('all_matches.csv')
df2=df
# print (df2)
relevantCols=['match_id','venue','innings','ball',
'batting_team','bowling_team','striker','non_striker',
'bowler','runs_off_bat','extras']
df2=df2[relevantCols]
df2['total_runs']=df2['runs_off_bat'].astype(int)+df2['extras'].astype(int)
df2=df2.drop(columns=['runs_off_bat','extras'])
df2=df2[df2['ball']<=5.6]
df2=df2[df2['innings']<=2]
# df=df.groupby(['match_id','venue','innings',
#  'batting_team','bowling_team','total_runs'])
df2.reset_index(inplace=True)
df2.to_csv("my_ipl2.csv",index=True)
# df2.to_csv("my_ipl6.csv")
print (df2)