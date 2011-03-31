'''
Created on 2011 3 31

@author: cihancimen
'''
import uuid


class Card(object):
    '''
    classdocs
    '''
    type_infantry = "infantry"
    type_cavalry = "cavalry"
    type_artillery = "artillery"
    type_wild = "wild"
    type_tip = "tip"

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
    
        