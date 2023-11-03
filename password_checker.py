import re

def validate_password(password):
    if len(password)<6:
        return False
    if len(password)>12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$,@,_,&,%]", password):
        return False
    return True

password = "P@ssword2"  
if validate_password(password):  
    print("Valid password")  
else:  
    print("Invalid password")