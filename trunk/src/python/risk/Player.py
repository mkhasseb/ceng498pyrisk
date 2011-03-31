'''
Created on 2011 3 31

@author: cihancimen
'''

class Player(object):
    '''
    classdocs
    '''
    COLOR_RED = "Red"
    COLOR_BLUE = "Blue"
    COLOR_GREEN = "Green"
    COLOR_GRAY = "Gray"
    COLOR_BLACK = "Black"
    COLOR_YELLOW = "Yellow"


    def __init__(self, color):
        '''
        Constructor
        '''
        self.color = color
        self.game = None
        self.armies = 0
        self.mission = None
        self.occupied = []
    def placeSingle(self, game):
        print "I am %s have %d armies. I am placing one" % (self.color, self.armies)
        
    def placeArmies(self, game):
        print "I am %s have %d armies. I am placing arbitrary" % (self.color, self.armies) 
        pass