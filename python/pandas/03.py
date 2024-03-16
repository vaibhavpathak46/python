import numpy as np
import pandas as pd

ser = pd.Series(np.random.rand(34))
newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))

# print(newdf)
print(newdf.to_numpy())
print(newdf.T)
print(type(newdf[0]))