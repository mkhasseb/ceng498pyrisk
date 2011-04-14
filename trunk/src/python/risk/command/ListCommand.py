# To change this template, choose Tools | Templates
# and open the template in the editor.
from risk.command.AbstractCommand import AbstractCommand

__author__ = "ozgur"
__date__ = "$Apr 1, 2011 3:33:37 PM$"


class ListCommand(AbstractCommand):
    '''
    classdocs
    '''
    def __init__(self, orig,verbose):
        '''
        Constructor
        '''
        AbstractCommand.__init__(self, orig)
        self.verbose = verbose
        
