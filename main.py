import sys
import os
import password_generator.code_generator

def help():
    """Contains help messages regarding how to use the password generator"""
    help_list = ['For all commands type help', # 0
                 'Generate a userdefined password, by typing user', # 1
                 'Generate a 20 characters long, random password by typing strong', # 2
                 'Generate a 15 characters long, password by typing inter', # 3
                 'Generate a 10 characters long, password by typing medium', # 4
                 'Generate a 5 characters long, password by typing weak' # 5
                 ]

    return help_list


def welcome():
    """Displays welcome message on startup"""
    print("""Welcome to Alexanders, password generator""")


def userloop():
    """User loop for user input and validating the input"""
    while True:
        try:
            size = int(input('How long would you like your password? > '))

        except:
            print('Wrong integer supplied, please try again.')
            # startover the loop, asking for a new integer again
            continue

        else:
            return size


password = code_generator(mainloop())
print('Your secret password is: {}'.format(password))
