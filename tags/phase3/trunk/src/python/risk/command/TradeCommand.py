# To change this template, choose Tools | Templates
# and open the template in the editor.
from risk.command.AbstractCommand import AbstractCommand

__author__="ozgur"
__date__ ="$Apr 3, 2011 5:28:38 PM$"

class TradeCommand(AbstractCommand):
    '''
    classdocs
    '''
    def __init__(self, orig, cards):
        '''
        Constructor
        '''
        AbstractCommand.__init__(self, orig)
        self.cards = cards
