# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:16:03 2023

@author: hp
"""
import random
import time
class TypingSpeedTester:
    def __init__(self):
        self.length=50
        self.characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def generate_random_text(self):
        self.original_text=''
        for _ in range(self.length):
            self.original_text += random.choice(self.characters)
        print("Type the following text:")
        print(self.original_text)
    def typing_speed_test(self):
        input("Press Enter when you're ready to start...")
        self.start_time=time.time()
        self.user_input=input("Start Typing: ")
        self.end_time=time.time()
    def words_per_minute_WPM(self):
        wpm=len(self.user_input)/((self.end_time-self.start_time)/60)
        print(f"You typing speed is: {wpm}")
    def check_correct_characters(self):
        self.correct_char=0
        for c1,c2 in zip(self.original_text,self.user_input):
            if c1==c2:
                self.correct_char += 1
    def check_accuracy(self):
        accuracy=(self.correct_char / self.length) *100
        print(f"Accuracy: {accuracy}")
obj=TypingSpeedTester()
obj.generate_random_text()
obj.typing_speed_test()
obj.words_per_minute_WPM()
obj.check_correct_characters()
obj.check_accuracy()
            
        