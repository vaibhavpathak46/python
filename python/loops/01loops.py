num=1
fact=int(input("enter the number"))
if(fact<=0):
    print("enter number greatee than 0")
else:
    for i in range(1,fact+1):
         num=num*i
print(num)