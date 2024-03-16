current_fee=2500
increase_percentage=4
print("projected rates for next six year :")
for i in range(1,7):
    current_fee=(current_fee)*(1+increase_percentage/100)
    print( f"fee for year {i} is : ${current_fee}")