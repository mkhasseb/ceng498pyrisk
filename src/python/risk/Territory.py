'''
Created on 2011 3 31

@author: cihancimen
'''

class Territory(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.neighbours = []
        
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
    
