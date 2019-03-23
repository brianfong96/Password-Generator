#!/usr/bin/env python
import pw_generator as pw_gen
from appJar import gui
import clipboard

ACCOUNT = "What Account is this password used for?"
USERNAME = "Username"
PASSWORD_LENGTH = "Password Length (Default is 16 if invalid entry)"
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
GENERATE = "Generate"
CANCEL = "Cancel"
HELP = "Help"

def press(button):
    if button == CANCEL:
        app.stop()
    elif button == GENERATE:
        answers = list()
        usr = app.getEntry(USERNAME).strip()
        account = app.getEntry(ACCOUNT).strip()
        pw_len = app.getEntry(PASSWORD_LENGTH).strip()

        valid_char = list()
        if app.getCheckBox(LOWER_CASE):        
            valid_char.append(LOWER)
        if app.getCheckBox(UPPER_CASE):
            valid_char.append(UPPER)
        if app.getCheckBox(NUMBERS):
            valid_char.append(NUM)
        if app.getCheckBox(SYMBOLS):
            valid_char.append(SYM)
        exclude = app.getEntry(EXCLUDE)
        if exclude != str():
            l = len(exclude)
            
            temp = list()
            for l in valid_char:
                t = ""
                for c in l:
                    if not c in exclude:
                        t += c
                temp.append(l)
            valid_char = temp
            print(valid_char)  

        answers.append(usr)
        answers.append(account)
        answers.append(pw_len)
        for v in valid_char:
            answers.append(v)
        answers.append(exclude)

        if pw_len.isnumeric():
            pw_len = int(pw_len)
        else:
            pw_len = 16
        pw = pw_gen.pw_generator(usr, pw_len, valid_char, answers)
        clipboard.copy(pw.password)
        app.infoBox("Your Password", "You password is :\n" + pw.password +"\nIt has been added to your clipboard")
        
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


app.addButtons([GENERATE, CANCEL, HELP], press)
app.go()