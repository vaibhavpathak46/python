from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[1,2,3,4,5]
y=[6,7,8,9,10]
x2=[11,12,13,14,15]
y2=[16,17,8,19,10]

plt.bar(x,y,'g',label="line one",linewidth=5)
plt.bar(x2,y2,'c',label="line two",linewidth=5)
plt.title("info")
plt.ylabel("yaxis")
plt.xlabel("xaxis")
plt.legend()
# 
plt.show()