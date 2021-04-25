import pandas as pd

df = pd.read_csv('Dataset/all_matches.csv')

relevantCols=['match_id','venue','innings','ball',
'batting_team','bowling_team','striker','non_striker',
'bowler','runs_off_bat','extras']
df=df[relevantCols]

df['total_runs']=df['runs_off_bat'].astype(int)+df['extras'].astype(int)
df=df.drop(columns=['runs_off_bat','extras'])

df=df[(df['ball']<=5.6) & (df['innings']<=2)]

# creating an empty 2D array
data = [[]]
#counter var
indexer = 0
score = 0

total_score = []
match_id = []
match_innings = []
match_venue = []
batting_team = []
bowling_team = []
run_rate = []
df[run_rate]= []

for i in range(df.shape[0]): # iterating through all rows
        score = score+df.iloc[i,9] # adding the score ball by ball in c
        if(df.iloc[i,3]==5.6):
                match_id=(df.iloc[i,0])#adding the element in the array
                match_innings=(df.iloc[i,2])
                match_venue=(df.iloc[i,1])
                batting_team=(df.iloc[i,4])
                bowling_team=(df.iloc[i,5])
                total_score= score
                run_rate = total_score / 6
                # inserting the elements in the 2 d array
                data.insert(indexer,[match_id,match_venue,match_innings,batting_team,bowling_team,total_score, run_rate])
                indexer = indexer + 1
                score =0

df_final=pd.DataFrame(data, columns=['match_id','match_venue','match_innings','batting_team','bowling_team','total_score','run_rate'])
df_final.to_csv("PREPROCCESED.csv",index=False)