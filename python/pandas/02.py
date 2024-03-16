import pandas as pd
import numpy as np
x=pd.read_csv('first.csv')
print(x)
x["marks"][3]=69
print(x)
print(x.to_csv("first.csv"))