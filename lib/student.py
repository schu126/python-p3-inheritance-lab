#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge_string):
        if isinstance(knowledge_string, str):
            self.knowledge.append(knowledge_string)
        else:
            print ("Must be a string")