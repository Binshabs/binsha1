"""mail,password"""

import re

terms="^[A-Za-z].+@[a-zA-Z]{2,}\.[A-Za-z]{2,}$"
email=str(input("enter the email:"))
x=re.search(terms,"email")
if x:
    print("validate")
else:
    print("not validate")
    
terms="^[A-Z][A-Za-z]{3,}\W\w{2,}$"
a=input("enter the password: ")

x=re.search(terms,"a")
if x:
    print("valid")
else:
    print("not valid")
