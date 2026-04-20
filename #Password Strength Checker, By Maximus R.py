#Password Strength Checker, By Maximus Ramirez
# This program is a security tool designed to highlight the weaknesses in passwords.
# It will analyze the password and use scoring criteria to determine the strength.

import re 
import argparse
import sys

def check_password_strength(password): 
    score=0
    
    #length checks
    if len (password) > (8):
        score += 1
    if len (password) > (12):
        score += 2
    if len (password) > (16):
        score += 3
        
    if len (password) > (20):
        score += 4
    
    

    if re.search(r"[A-Z]", password):
        score += 2
    if re.search(r"[a-z]", password):
        score += 2
    if re.search(r"[!@#$%^&*?+_=\-]", password):
        score += 4
    if re.search(r"[0-9]", password):
        score += 2
    
    return score


user = input ("Enter your password: ")
result = check_password_strength(user)
print("Password strength score", result)


if result < 5:
    print("Weak password")
elif result < 10:
    print("Fair password")
elif result < 16:
    print("Strong password")
else:
    print("The Strongest")
   