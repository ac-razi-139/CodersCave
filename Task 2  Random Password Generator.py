# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:36:31 2023

@author: hp
"""
import string
import random
class RandomPasswordGenerator:
    def __init__(self):
        self.length=10
    def generate_password(self):
        self.characters=string.ascii_letters+string.digits+string.punctuation
        self.password=''
        for _ in range(self.length):
            self.password += random.choice(self.characters)
        print(self.password)
obj=RandomPasswordGenerator()
obj.generate_password()
        