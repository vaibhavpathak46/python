import matplotlib.pyplot as plt
plt .bar([4,6,8,7],[6,4,7,9],label="first")
plt .bar([5,9,10,8],[7,4,2,6],label="second", color="g")
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('BAR GRAPH')
plt.show()