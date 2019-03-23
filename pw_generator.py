#!/usr/bin/env python
import random
import math
import os
import argparse
from appJar import gui

class pw_generator:
    """
    A password generator which asks questions about the specifications of the password
    As well some personal questions and generates a password based on the answers
    No passwords are saved, only the questions asked.
    """
    def __init__(self, usr = str(), pw_len = int(), val_chr = list(), ans = list()):
        """
        Initialize variables needed 
        Receive user input 
        Generate password and print
        Save questions asked as a txt file
        """        
        self.valid_char = val_chr
        self.password_len = pw_len        
        self.user = usr                
        self.answers = ans

        self.password = str()
        self.generate_password()                    
        return

    def generate_seed(self):
        """
        Take the strings in self.answers and adds the value to use as key
        """
        seed = 0
        for answer in self.answers:
            for char in answer:
                seed += ord(char)
        return seed

    def scramble(self, string, seed):
        """
        Based on seed, scramble characters in answer
        """
        random.seed(seed)
        new_pos = random.sample(range(0,len(string)), len(string))
        temp = str()
        for i in new_pos:
            temp += string[i]
        return temp

    def generate_password(self):
        """
        Generates password using seed and valid chars
        """

        seed = self.generate_seed()        
        self.scramble(self.valid_char, seed)        
        random.seed(seed)
        for i in range(self.password_len):
            self.password += self.valid_char[random.randint(0,len(self.valid_char)-1)]
        self.scramble(self.password, seed)
        return

if __name__ == "__main__":
    ACCOUNT = "What Account is this password used for?"
    USERNAME = "Username"
    PASSWORD_LENGTH = "Password Length"
    LOWER_CASE = "Include Lowercase Letters?"
    UPPER_CASE = "Include Uppercase Letters?"
    NUMBERS = "Include Numbers?"
    SYMBOLS = "Include these symbols? '!@#$%^&*()-=_+[]:;',.<>/?`~'"
    EXCLUDE = "Enter any characters to exclude"    
    EXTRA = "Do you want to answer more questions?"
    LOWER = 'qwertyuiopasdfghjklzxcvbnm'
    UPPER = LOWER.upper()
    NUM = '1234567890'
    SYM = "!@#$%^&*()-=_+[]:;',.<>/?`~"
    SUBMIT = "Submit"
    CANCEL = "Cancel"
    def press(button):
        if button == CANCEL:
            app.stop()
        elif button == SUBMIT:
            answers = list()
            usr = app.getEntry(USERNAME).strip()
            account = app.getEntry(ACCOUNT).strip()
            pw_len = app.getEntry(PASSWORD_LENGTH).strip()

            valid_char = ""
            if app.getCheckBox(LOWER_CASE):
                valid_char += LOWER
            if app.getCheckBox(UPPER_CASE):
                valid_char += UPPER
            if app.getCheckBox(NUMBERS):
                valid_char += NUM
            if app.getCheckBox(SYMBOLS):
                valid_char += SYM
            exclude = app.getEntry(EXCLUDE)
            if exclude != str():
                l = len(exclude)
                for char in exclude:
                    pos = valid_char.find(char)                
                    if pos != -1:
                        valid_char = valid_char[0:pos] + valid_char[pos+1:l]   

            answers.append(usr)
            answers.append(account)
            answers.append(pw_len)
            answers.append(valid_char)

            if pw_len.isnumeric():
                pw_len = int(pw_len)
            else:
                pw_len = 16
            pw = pw_generator(usr, pw_len, valid_char, answers)
            app.infoBox("Your Password", pw.password)
        return 
        
    
            

    app = gui("Password Generator", "800x400")
    app.setBg("green")
    app.setFont(18)
    app.addLabel("title", "Password Generator")
    app.setLabelBg("title", "blue")
    app.addLabelEntry(ACCOUNT)
    app.addLabelEntry(USERNAME)
    app.addLabelEntry(PASSWORD_LENGTH)
    app.addCheckBox(LOWER_CASE)
    app.setCheckBox(LOWER_CASE, ticked=True)
    app.addCheckBox(UPPER_CASE)
    app.setCheckBox(UPPER_CASE, ticked=True)
    app.addCheckBox(NUMBERS)
    app.setCheckBox(NUMBERS, ticked=True)
    app.addCheckBox(SYMBOLS)
    app.setCheckBox(SYMBOLS, ticked=True)
    app.addLabelEntry(EXCLUDE)
    

    app.addButtons([SUBMIT, CANCEL], press)
    app.go()
    pass
    
