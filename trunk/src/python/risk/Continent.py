'''
Created on 2011 3 31

@author: cihancimen
'''

class Continent(object):
    '''
    classdocs
    ''' 


    def __init__(self, name, territories, bonus):
        '''
        Constructor
        '''
        self.name = name
        self.territories = territories
        for territory in territories:
            territory.continent = self
        self.bonus = bonus
