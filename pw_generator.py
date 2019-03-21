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
        self.lower_char = 'qwertyuiopasdfghjklzxcvbnm'
        self.upper_char = self.lower_char.upper()
        self.nums = '1234567890'
        self.symbols = '!@#$%^&*()-=_+[]:;",.<>/?`~'
        self.invalid_symbols = str()
        self.answer = list()
        self.seed = int()
        self.valid_char = str()
        self.password_len = int()
        self.password = str()
        self.user = str()
        self.question_type = {1:'y/n', 2:'Must be an integer', 3:''}

        self.read_file()
        self.ask_question()
        self.generate_seed()
        self.scramble()
        self.substitute()
        print(self.password)
        self.write_file()
        return

    def read_file(self):
        """

        """
        file_name = str()
        if usr != str():
            file_name = usr+'.txt'
        
        return
    
    def write_file(self):
        """

        """
        return

    def ask_question(self):
        """

        """
        return

    def generate_seed(self):
        """

        """
        return

    def scramble(self):
        """

        """
        return

    def substitute(self):
        """

        """
        return

if __name__ == "__main__":
    
    pass
    
