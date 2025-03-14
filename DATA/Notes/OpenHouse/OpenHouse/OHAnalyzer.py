import pandas as pd
'''
    What schools came and how many from each
    What programs were visited and how many from each
    
'''
df = pd.read_csv("OriginalData/Foyer.csv",header=0)
print(df)

schools = df["school"].unique()
print(schools)