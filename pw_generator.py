#!/usr/bin/env python
import random
import math
import os

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
        temp = list()        
        for l in self.valid_char:
            temp.append(self.scramble(l, seed))
        self.valid_char = temp
        random.seed(seed)
        for i in range(self.password_len):
            section = random.randint(0,len(self.valid_char)-1)
            self.password += self.valid_char[section][random.randint(0,len(self.valid_char[section])-1)]
        self.scramble(self.password, seed)
        return