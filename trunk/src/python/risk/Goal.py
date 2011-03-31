'''
Created on 2011 3 31

@author: cihancimen
'''

class GoalFactory(object):
    verbose_occupy= "Occupy 24 Territories of your choice."
    verbose_conquer = "Conquer 18 Territories of your choice and Occupy each with at least 2 Armies."
    verbose_continent = "Conquer the Continents of"
    verbose_eliminate = "Destroy all"
    def __init__(self):
        pass
    @staticmethod
    def createOccupy():
        return Goal(Goal.type_occupy, GoalFactory.verbose_occupy)
    @staticmethod
    def createConquer():
        return Goal(Goal.type_conquer, GoalFactory.verbose_conquer)
    @staticmethod
    def createConquerContinent(continents):
        verbose = GoalFactory.verbose_conquer+" " + continents[0].name
        verbose += " and " + continents[2].name
        return Goal(Goal.type_continent, verbose, continents=continents)
    @staticmethod
    def createEliminate(color):
        alternate = GoalFactory.createOccupy()
        verbose = GoalFactory.verbose_continent + " " + color + " troops." + alternate.verbose  
        return Goal(Goal.type_eliminate, verbose, color=color, alternate=alternate)
    
class Goal(object):
    '''
    classdocs
    All of the goals are listed below
    Occupy 24 Territories of your choice.
    Conquer the Continents of North America and Africa.
    Conquer the Continents of North America and Australia.
    Conquer the Continents of Asia and Africa.
    Conquer the Continents of Asia and South America.
    Destroy all Black troops. If yours are the Black Troops, then: Occupy 24 Territories of your choice.
    Destroy all Gray troops. If yours are the Gray Troops, then: Occupy 24 Territories of your choice.
    Destroy all Green troops. If yours are the Green Troops, then: Occupy 24 Territories of your choice.
    Destroy all Yellow troops. If yours are the Yellow Troops, then: Occupy 24 Territories of your choice.
    Destroy all Red troops. If yours are the Red Troops, then: Occupy 24 Territories of your choice.    
    Destroy all Blue troops. If yours are the Blue Troops, then: Occupy 24 Territories of your choice.
    Conquer 18 Territories of your choice and Occupy each with at least 2 Armies.
    '''
    type_eliminate = "eliminate"
    type_continent = "continent"
    type_occupy="occupy" #24 Territories
    type_conquer ="conquer" #18 Territory at least two armies

    def __init__(self, type, verbose, continents=None, color =None, alternate = None):
        '''
        Generic Constructor
        
        '''
        self.type = type
        self.verbose = verbose
        if(continents):
            self.continents = continents
        if(color):
            self.color = color
            self.alternate = alternate
        