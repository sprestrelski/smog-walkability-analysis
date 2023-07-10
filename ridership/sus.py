import pandas as pd

df = pd.read_excel('March 2023 Complete Monthly Ridership.xlsx', sheet_name=None)  
for key in df.keys(): 
    df[key].to_csv('%s.csv' %key)