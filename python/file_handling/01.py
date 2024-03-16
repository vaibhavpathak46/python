import os
file=open(r"c:\users\vaibh\onedrive\desktop\new text document.txt",'r')
print(file.read())
file.close()

file=open(r"c:\users\vaibh\onedrive\desktop\new text document.txt",'w')
print(file.write("hello"))
file.close()

file=open(r"c:\users\vaibh\onedrive\desktop\new text document.txt",'r')
print(file.read())
file.close()

file=open(r"c:\users\vaibh\onedrive\desktop\new text document.txt",'a')
print(file.append("world"))
file.close()

file=open(r"c:\users\vaibh\onedrive\desktop\new text document.txt",'r')
print(file.read())
file.close()