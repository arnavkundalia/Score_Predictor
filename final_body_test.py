import pandas as pd
import numpy as np
df=pd.read_csv('\Score_Predictor\my_ipl_225_lines.csv')
#print(df)
data=[[]]# creating an empty 2D array
f=0 # counter var
c=0
N_total_score=[]
N_match_id=[]
N_match_innings=[]
N_match_venue=[]
N_batting_team=[]
N_bowling_team=[]
# print(df.iloc[0,12])
for i in range(224): # iterating through all rows       
        c=c+df.iloc[i,11] # adding the score ball by ball in c    
        if(df.iloc[i,5]==5.6):
                N_match_id=(df.iloc[i,2])#adding the element in the array 
                N_match_innings=(df.iloc[i,4])
                N_match_venue=(df.iloc[i,3]) 
                N_batting_team=(df.iloc[i,6])
                N_bowling_team=(df.iloc[i,7])
                N_total_score=c
                data.insert(f,[N_match_id,N_match_venue,N_match_innings,N_batting_team,N_bowling_team,N_total_score])# inserting the elements in the 2 d array              
                f=f+1# f is the index where the new element is to be added
                c=0# reset the score adder
# print (data)
df2=pd.DataFrame(data, columns=['N1_match_id','N1_match_venue','N1_match_innings','N1_batting_team','N1_bowling_team','N1_total_score'])
# print(df2)
df2.to_csv("my_ipl90.csv",index=True)