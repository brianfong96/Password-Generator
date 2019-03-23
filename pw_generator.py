#!/usr/bin/env python
import random
import math
import os
import argparse

class pw_generator:
    """
    A password generator which asks questions about the specifications of the password
    As well some personal questions and generates a password based on the answers
    No passwords are saved, only the questions asked.
    """
    def __init__(self, user = str()):
        """
        Initialize variables needed 
        Receive user input 
        Generate password and print
        Save questions asked as a txt file
        """
        self.questions = list()
        self.answers = list()
        self.seed = int()
        self.valid_char = str()
        self.password_len = int()
        self.password = str()
        self.user = str()                

        self.read_file()
        self.ask_question()
        self.generate_password()        
        
        input("Your passowrd is :\n" + self.password)
        return

    def read_file(self):
        """        
        If a user name is given, then read the file for the user
        If a user name is not given, then read the generic file
        self.questions will be updated to store the results
        """
        file_name = str()
        if self.user != str():
            file_name = self.user +'.txt'
        else:
            file_name = 'questions.txt'
        
        with open(file_name, 'r') as f:
            self.questions = f.read()
        f.close()    
        self.questions = self.questions.split("\n")
        return


    def validate(self, question_type, answer):
        """
        Based on question type suffix, determines if the answer is valid or not
        """

        question_type_suffix = ['y/n', 'Must be an integer', '']
        if question_type == question_type_suffix[0]:
            if answer.lower() == 'y' or answer.lower() == 'n':
                return True
        elif question_type == question_type_suffix[1]:
            return answer.isnumeric()
            
        elif question_type == question_type_suffix[2]:
            return True
        return False
            

    def valid_answer(self, question):
        """
        Based on the question suffix, validates user input
        Returns:
            answer - string that the user enters to respond to string
        """

        start_paren = question.find('(')+1
        end_paren = question.find(')')
        question_type = question[start_paren:end_paren]                
        question = question[1:]
        answer = input(question+": ").strip()
        while not self.validate(question_type, answer):            
            answer = input(question+": ").strip()            
        
        temp = answer.split(' ')
        answer = ''
        for w in temp:
            answer += w
        return answer

    def ask_question(self):
        """
        Asks questions from self.questions
        """
        additional_question = '%Do you want to answer more additional questions?(y/n)'
        question_type_prefix = ['#', '%', '*']
        for q in self.questions:            
            if q[0] == question_type_prefix[0]:          
                self.answers.append(self.valid_answer(q))      
            elif q[0] == question_type_prefix[1]:
                if self.valid_answer(q) == 'n' and q == additional_question:
                    break
            elif q[0] == question_type_prefix[2]:
                self.answers.append(self.valid_answer(q))
                if self.valid_answer(additional_question) == 'n':
                    break
        return

    def generate_valid_chars(self):
        """
        First 6 questions must be
        #How long do you want your password? (Must be an integer)
        #Do you want lowercase letters in your password?(y/n)
        #Do you want uppercase letters in your password?(y/n)
        #Do you want numbers in your password?(y/n)
        #Do you want symbols in your password? These are the symbols available !@#$%^&*()-=_+[]:;",.<>/?`~ (y/n)
        #Are there symbols that are not allowed? Enter all characters not allowed, if all characters are allowed, just press enter()
        """
        self.password_len = int(self.answers[0])        
        if self.answers[1] == 'y':
            self.valid_char += 'qwertyuiopasdfghjklzxcvbnm'
        if self.answers[2] == 'y':
            self.valid_char += 'qwertyuiopasdfghjklzxcvbnm'.upper()
        if self.answers[3] == 'y':
            self.valid_char += '1234567890'
        if self.answers[4] == 'y':
            self.valid_char += '!@#$%^&*()-=_+[]:;",.<>/?`~'
        if self.answers[5] == 'y':
            l = len(self.valid_char)
            for char in self.answers[5]:
                pos = self.valid_char.find(char)                
                if pos != -1:
                    self.valid_char = self.valid_char[0:pos] + self.valid_char[pos+1:l]            
        return

    def generate_seed(self):
        """
        Take the strings in self.answers and adds the value to use as key
        """
        for answer in self.answers:
            for char in answer:
                self.seed += ord(char)
        return

    def scramble(self, s):
        """
        Based on seed, scramble characters in answer
        """
        random.seed(self.seed)
        new_pos = random.sample(range(0,len(s)), len(s))
        temp = str()
        for i in new_pos:
            temp += s[i]
        return temp

    def generate_password(self):
        """
        Generates password using seed and valid chars
        """
        self.generate_valid_chars()
        self.generate_seed()        
        self.scramble(self.valid_char)        
        random.seed(self.seed)
        for i in range(self.password_len):
            self.password += self.valid_char[random.randint(0,len(self.valid_char)-1)]
        self.scramble(self.password)

        return

if __name__ == "__main__":
    pw_generator()
    pass
    
