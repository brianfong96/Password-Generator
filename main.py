#!/usr/bin/env python
import pw_generator as pw_gen
from appJar import gui

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
        pw = pw_gen.pw_generator(usr, pw_len, valid_char, answers)
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