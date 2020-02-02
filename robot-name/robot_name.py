import string
import random

class Robot(object):
    def __init__(self):
        self.old_name = []
        self.name = self.generate_random_name()
        

    def generate_random_name(self):

        while(True):        
            name = ""
            for i in range(2):
                name += random.choice(string.ascii_uppercase)
                        
            for i in range(3):
                name += str(random.randint(0, 9));            

            if(name not in self.old_name):
                break
        
        self.old_name.append(name)
        return name

    def reset(self):
        self.name = self.generate_random_name()
