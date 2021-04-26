import pandas as pd
import numpy as np

df = pd.read_csv('all_matches.csv')

#filtering all the irrelevant columns from the original dataset.

relevantCols=['match_id','venue','innings','ball',
'batting_team','bowling_team','striker','non_striker',
'bowler','runs_off_bat','extras','wicket_type']
df=df[relevantCols]

#adding the extras and runs off bat to the column 'total runs'

df['total_runs'] = df['runs_off_bat'].astype(int)+df['extras'].astype(int)
df=df.drop(columns=['extras'])

#reducing the dataset to only 6 overs per innings 

df=df[(df['ball']<=5.6) & (df['innings']<=2)]

#filling all the elements which have no element to 0 and storing it to a new dataframe
df1=df.fillna(0)

# creating an empty 2D array
data = [[]]
#counter vars and sum var
indexer = 0
score = 0
park = 0
j=0
wic=0

run_rate_1=0

#intializing a new dataframe

df_final=pd.DataFrame()

#initializing new numpy arrays and lists to be used as data elements in creating the new df

total_score = np.array([],dtype="int")
match_id = np.array([],dtype="str")
match_innings = np.array([])
match_venue = np.array([],dtype="str")
batting_team = np.array([],dtype="str")
bowling_team = np.array([],dtype="str")
wicket = np.array([],dtype="int")
run_rate = np.array([],dtype="float")
df[run_rate]= np.array([])
category = []
boundries = np.array([],dtype="int")
df[boundries]=np.array([])
wickets = ['caught','bowled','lbw','run out','stumped','caught and bowled','retired hurt']
wicket = np.array([],dtype="str")

# iterating through all rows of the df1

for i in range(df1.shape[0]): 
        score = score+df1.iloc[i,11]
        
        # adding the score ball by ball in c

        if(df1.iloc[i,10] in wickets):
             wic=wic+1
        
        if(df1.iloc[i,9]==4 or df1.iloc[i,9]==6):
                park=park+1
        if(df1.iloc[i,3]==5.6):

                #adding the element in the array

                match_id=(df1.iloc[i,0])
                match_innings=(df1.iloc[i,2])
                match_venue=(df1.iloc[i,1])
                batting_team=(df1.iloc[i,4])
                bowling_team=(df1.iloc[i,5])
                total_score= score
                boundries=park
                run_rate = total_score / 6
                wicket=wic

                # inserting the elements in the 2 d array

                data.insert(indexer,[match_id, match_venue, match_innings, batting_team, bowling_team, boundries,wicket, run_rate, total_score ])
                df_final=pd.DataFrame(data, columns=['match_id','match_venue','match_innings','batting_team','bowling_team', 'boundry_count','wickets fallen','run_rate','total_score'])
               
                # print(df_final.iloc[1,6]) 
                                                                    
                indexer = indexer + 1
                score =0
                park = 0
                wic=0

                #categorizing the stadium the stadium 

                run_rate_1=df_final.iloc[j,7]
                if(run_rate_1>=9):
                    category.append('High scoring')  
                elif(run_rate_1>=6.5 and run_rate_1<9):
                    category.append('Medium scoring')                     
                elif(run_rate_1<6.5):
                    category.append('Low scoring') 
                j=j+1


if(run_rate_1>=9):
    category.append('High scoring')  
elif(run_rate_1>=6.5 and run_rate_1<9):
    category.append('Medium scoring')                    
elif(run_rate_1<6.5):
    category.append('Low scoring')    

df_final['Stadium_Category']=category
df_final.drop([j], axis=0, inplace=True)

#converting df_csv  to the preprocessed csv file

df_final.to_csv("PREPROCCESED40.csv",index=True)
#print(df_final)