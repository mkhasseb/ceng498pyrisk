'''
Created on 2011 3 31

@author: cihancimen
'''
import uuid


class Card(object):
    '''
    classdocs
    '''
    TYPE_INFANTRY = "infantry"
    TYPE_CAVALRY = "cavalry"
    TYPE_ARTILLERY = "artillery"
    TYPE_WILD = "wild"
    TYPE_TIP = "tip"

    def __init__(self, type, territory=None, tip=None):
        '''
        Constructor
        '''
        self.id = uuid.uuid4()
        self.type = type;
        if(territory):
            self.territory = territory
        if(tip):
            self.tip = tip
    
        
