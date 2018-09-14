from re import *
# import re



def chack_email(email) :
    pattern = compile( '(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)' )
    is_valid = pattern.match( email )

    if is_valid :
        return True
    else:
        return False

def chack_name(name) :
    pattern = compile( '[a-zA-Z]' )
    is_valid = pattern.match( name )

    if is_valid :
        return True
    else:
        return False

# email = input( 'Enter Your Email email: ' )
# result=chack_email(email)
# print(result)

name = input( 'Enter Your name: ' )
result=chack_name(name)
print(result)