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


import re
terms='binsha?'
x=re.search(terms,"binsha")
if x:
    print("matched")
else:
    print("not matched")

