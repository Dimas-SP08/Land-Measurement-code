import os
import platform

'''Prompt the user with a yes/no question and return boolean'''
def input_yes_no(prompt):
    while True:
        send_excel = input(prompt)
        if send_excel in ('y','n'):
            return send_excel == 'y'   
        print('\nchoose y/n!')

'''Clear terminal screen on Windows or Unix'''
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

