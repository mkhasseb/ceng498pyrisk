'''
Created on 2011 3 31

@author: cihancimen
'''

class GoalFactory(object):
    VERBOSE_OCCUPY = "Occupy %d Territories of your choice."
    VERBOSE_CONQUER = "Conquer %d Territories of your choice and Occupy each with at least %d Armies."
    VERBOSE_CONTINENT = "Conquer the Continents of"
    VERBOSE_ELIMINATE = "Destroy all"
    def __init__(self):
        pass
    @staticmethod
    def createOccupy(num):
        return Goal(Goal.TYPE_OCCUPY, (GoalFactory.VERBOSE_OCCUPY % (num)), num=num)
    @staticmethod
    def createConquer(num, numArmy):
        return Goal(Goal.TYPE_CONQUER, (GoalFactory.VERBOSE_CONQUER % (num, numArmy)), num=num, numArmy=numArmy)
    @staticmethod
    def createConquerContinent(continents):
        verbose = GoalFactory.VERBOSE_CONQUER + " " + continents[0].name
        verbose += " and " + continents[1].name
        return Goal(Goal.TYPE_CONTINENT, verbose, continents=continents)
    @staticmethod
    def createEliminate(color, num):
        alternate = GoalFactory.createOccupy(num)
        verbose = GoalFactory.VERBOSE_CONTINENT + " " + color + " troops. If yours are the " + color + " Troops, then: " + alternate.verbose  
        return Goal(Goal.TYPE_ELIMINATE, verbose, color=color, alternate=alternate)
    
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
    TYPE_ELIMINATE = "eliminate"
    TYPE_CONTINENT = "continent"
    TYPE_OCCUPY = "occupy" #24 Territories
    TYPE_CONQUER = "conquer" #18 Territory at least two armies

    #FIXME For different maps, number of territories and minimum number of armies on each territory may change
    def __init__(self, type, verbose, num=24, numArmy=2, continents=None, color=None, alternate=None):
        '''
        Generic Constructor
        
        '''
        self.numArmy = numArmy 
        self.num = num
        self.type = type
        self.verbose = verbose
        if(continents):
            self.continents = continents
        if(color):
            self.color = color
            self.alternate = alternate
        
