Marks=int(input("ENTER THE NUMERIC VALUE :  ")) #Taking input frm the user
if(Marks>=90 and Marks<101):                   
    print("A")
else:
    if(Marks>=80 and Marks<90):
        print("B")  
    else:                     #if and elif statement id use to print grade according to the entered value
        if(Marks>=70 and Marks<80):
            print("C")
        else:
            if(Marks>=60 and Marks<70):
                print("D")
            else:
                if( Marks<60 and Marks>=0):
                    print("F")
                else:   #else statement is used to print a message that "NOT A VALID ENTRY" because value is beyond the range of 0 to 100
                    print("NOT A VALID ENTRY")