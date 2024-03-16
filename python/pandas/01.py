import pandas as pd
import numpy as np
dict1={
    "name":['vaibhav','sundar','ayush','shudhansu'],
    "marks":[95,89,78,66],
    "city":["jaunpur","rudrapur","lalkuan","gaziabad"]
}
df1=pd.DataFrame(dict1)
print(df1)
df1.to_csv("first.csv")
# #use to conevert dataframe into xl sheet
df1.to_csv("first_falseindex.csv",index=False)
# to print start and ending number of rows 
# print(df1.head(2))
# print(df1.tail(2))
# print(df1.describe( ))