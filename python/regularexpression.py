# import re
# terms="hello"
# # x=re.match(terms,"hello synnefo")
# #x=re.findall(terms," synnefo hello hello")
# # x=re.split(terms," synnefo hello hello")
# x=re.search(terms,"synnefo hello")
# print(x)


"""match"""
# import re
# # terms='[abcd]'
# terms='[a-z,A-Z,0-9]'
# x=re.match(terms,"Binsha")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
    
# import re   
# terms='[a-z].....'
# x=re.match(terms,"Binsha")
# if x:
#     print("matched")
# else:
#     print("not matched")


"""serach"""


# import re
# terms="binsha?"
# x=re.match(terms,"binsha")
# if x:
#     print("matched")
# else:
#     print("not matched")

# import re
# terms="\d"
# x=re.match(terms,"6hello s9ynnefo")
# if x:
#     print("matched")
# else:
#     print("not matched")



# import re
# terms="^[^h]ello"
# x=re.search(terms,"hello synnefo")
# if x:
#     print("matched")
# else:
#     print("not matched")



# import re
# terms="^[5-9]\d{9}$"
# x=re.search(terms,"5123456789")
# if x:
#     print("validate")
# else:
#     print("not validate")

"""user input"""

# import re
# username=str(input("enter your username: "))
# terms="^[a-zA-Z]\w{3,25}$"
# x=re.search(terms,"username")
# if x:
#     print("validate")
# else:
#     print("not validate")



"""calender"""

# import re
# day=str(input("enter the date:"))
# terms="^([012]\d|3[01])(.|\|-)([0]\d|1[012])(.|\|-)(\d{4})$"
# a=re.search(terms,"00.00.0000")
# if a:
#      print("validate")
# else:
#      print("not validate")
     
"""calender"""


# import re
# day=str(input("enter the date:"))
# terms="^([^00]|[0][1,9]|[12][1,9]|3[1]|[123][0])(.|\|-)([^00]|[0][1,9]|1[012])(.|\|-)([^0000]\d{4})$"
# a=re.search(terms,"00.00.0000")
# if a:
#      print("validate")
# else:
#      print("not validate")
     
     
     
     
"""EMAIL"""


# import re

# terms="^[A-Za-z].+@[a-zA-Z]{2,}\.[A-Za-z]{2,}$"
# email=str(input("enter the email:"))
# x=re.search(terms,"email")
# if x:
#     print("validate")
# else:
#     print("not validate")



"""password"""

#import re

# terms="^[A-Z][A-Za-z]{3,}\W\w{2,}$"
# a=input("enter the password: ")

# x=re.search(terms,"a")
# if x:
#     print("valid")
# else:
#     print("not valid")


"""vowels"""


# import re

# terms="a|e|i|o|u"
# a=str(input("enter the string:"))

# x=re.findall(terms,a)
# print(x)
# print(len(x))


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



