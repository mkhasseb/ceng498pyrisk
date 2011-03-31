'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.Goal import GoalFactory
from risk.Player import Player
from risk.Territory import Territory
from risk.Continent import Continent
from risk.Card import Card
from risk.Game import Game
from risk.cmd.CmdPlayer import CmdPlayer



class DefaultGameSetup(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    def init(self):
        '''Territories
            generated from image http://en.wikipedia.org/wiki/File:Risk_game_map_fixed.png
        '''
        '''North America'''
        alaska = Territory("Alaska")
        alberta = Territory("Alberta")
        centralAmerica = Territory("CentralAmerica")
        easternUnitedStates = Territory("EasternUnitedStates")
        greenland = Territory("Greenland")
        northwestTerritory = Territory("NorthewstTerritory")
        ontario = Territory("Ontario")
        quebec = Territory("Quebec")
        westernUnitedStates = Territory("WesternUnitedStates")
        '''South America'''
        argentina = Territory("Argentina")
        brazil = Territory("Brazil")
        peru = Territory("Peru")
        venezuela = Territory("Venezuela")
        '''Europe'''
        greatBritain = Territory("GreatBritain")
        iceland = Territory("Iceland")
        northernEurope = Territory("NorthernEurope")
        scandinavia = Territory("Scandinavia")
        southernEurope = Territory("SouthernEurope")
        ukraine = Territory("Ukraine")
        westernEurope = Territory("WesternEurope")
        
        '''Africa'''
        congo = Territory("Congo")
        eastAfrica = Territory("EastAfrica")
        egypt = Territory("Egypt")
        madagascar = Territory("Madagascar")
        northAfrica = Territory("NorthAfrica")
        southAfrica = Territory("SouthAfrica")

        '''Asia'''
        kazakhstan = Territory("Kazakhstan")
        china = Territory("China")
        india = Territory("India")
        irkutsk = Territory("Irkutsk")
        japan = Territory("Japan")
        kamchatka = Territory("Kamchatka")
        middleEast = Territory("MiddleEast")
        mongolia = Territory("Mongolia")
        siam = Territory("Siam")
        siberia = Territory("Siberia")
        ural = Territory("Ural")
        yakutsk = Territory("Yakutsk")

        '''Australia'''
        easternAustralia = Territory("EasternAustralia")
        indonesia = Territory("Indonesia")
        newGuinea = Territory("NewGuinea")
        westernAustralia = Territory("WesternAustralia")
        
        '''Continents'''
        northAmerica = Continent("North America", [alaska, alberta, centralAmerica, easternUnitedStates, greenland, northwestTerritory, ontario, quebec, westernUnitedStates], 5)
        southAmerica = Continent("South America", [argentina, brazil, peru, venezuela], 2);
        europe = Continent("Europe", [greatBritain, iceland, northernEurope, scandinavia, southernEurope, ukraine, westernEurope], 5)
        africa = Continent("Africa", [congo, eastAfrica, egypt, madagascar, northAfrica, southAfrica], 3)
        asia = Continent("Asia", [kazakhstan, china, india, irkutsk, japan, kamchatka, middleEast, mongolia, siam, siberia, ural, yakutsk], 7)
        australia = Continent("Australia", [easternAustralia, indonesia, newGuinea, westernAustralia], 2)
        
        continents = [ northAmerica, europe, southAmerica, africa, asia, australia]
        '''Neighbours'''
        '''North America'''
        alaska.addNeighbour(northAmerica.territories[1])
        alaska.addNeighbour(northAmerica.territories[5])
        alaska.addNeighbour(asia.territories[5])
        
        alberta.addNeighbour(northAmerica.territories[0])
        alberta.addNeighbour(northAmerica.territories[5])
        alberta.addNeighbour(northAmerica.territories[6])
        alberta.addNeighbour(northAmerica.territories[8])
        
        centralAmerica.addNeighbour(northAmerica.territories[3])
        centralAmerica.addNeighbour(northAmerica.territories[8])
        centralAmerica.addNeighbour(southAmerica.territories[2])
        centralAmerica.addNeighbour(southAmerica.territories[3])
        
        easternUnitedStates.addNeighbour(northAmerica.territories[2])
        easternUnitedStates.addNeighbour(northAmerica.territories[8])
        easternUnitedStates.addNeighbour(northAmerica.territories[6])
        easternUnitedStates.addNeighbour(northAmerica.territories[7])
        
        greenland.addNeighbour(northAmerica.territories[5])
        greenland.addNeighbour(northAmerica.territories[6])
        greenland.addNeighbour(northAmerica.territories[7])
        greenland.addNeighbour(europe.territories[1])
        
        northwestTerritory.addNeighbour(northAmerica.territories[0])
        northwestTerritory.addNeighbour(northAmerica.territories[1])
        northwestTerritory.addNeighbour(northAmerica.territories[6])
        northwestTerritory.addNeighbour(northAmerica.territories[4])
        
        ontario.addNeighbour(northAmerica.territories[1])
        ontario.addNeighbour(northAmerica.territories[5])
        ontario.addNeighbour(northAmerica.territories[4])
        ontario.addNeighbour(northAmerica.territories[7])
        ontario.addNeighbour(northAmerica.territories[3])
        ontario.addNeighbour(northAmerica.territories[8])
        
        quebec.addNeighbour(northAmerica.territories[4])
        quebec.addNeighbour(northAmerica.territories[6])
        quebec.addNeighbour(northAmerica.territories[3])
        
        westernUnitedStates.addNeighbour(northAmerica.territories[1])
        westernUnitedStates.addNeighbour(northAmerica.territories[6])
        westernUnitedStates.addNeighbour(northAmerica.territories[3])
        westernUnitedStates.addNeighbour(northAmerica.territories[2])
        
        '''South America'''
        argentina.addNeighbour(southAmerica.territories[1])
        argentina.addNeighbour(southAmerica.territories[2])
        
        brazil.addNeighbour(southAmerica.territories[2])
        brazil.addNeighbour(southAmerica.territories[3])
        brazil.addNeighbour(africa.territories[4])
        
        peru.addNeighbour(southAmerica.territories[0])
        peru.addNeighbour(southAmerica.territories[1])
        peru.addNeighbour(southAmerica.territories[3])
        
        venezuela.addNeighbour(southAmerica.territories[1])
        venezuela.addNeighbour(southAmerica.territories[2])
        venezuela.addNeighbour(northAmerica.territories[2])
        
        '''Europe'''
        greatBritain.addNeighbour(europe.territories[1])
        greatBritain.addNeighbour(europe.territories[3])
        greatBritain.addNeighbour(europe.territories[2])
        greatBritain.addNeighbour(europe.territories[6])
        
        iceland.addNeighbour(europe.territories[0])
        iceland.addNeighbour(europe.territories[3])
        iceland.addNeighbour(northAmerica.territories[4])
        
        northernEurope.addNeighbour(europe.territories[0])
        northernEurope.addNeighbour(europe.territories[6])
        northernEurope.addNeighbour(europe.territories[4])
        northernEurope.addNeighbour(europe.territories[3])
        northernEurope.addNeighbour(europe.territories[5])
        
        scandinavia.addNeighbour(europe.territories[5])
        scandinavia.addNeighbour(europe.territories[2])
        scandinavia.addNeighbour(europe.territories[0])
        scandinavia.addNeighbour(europe.territories[1])
        
        southernEurope.addNeighbour(europe.territories[6])
        southernEurope.addNeighbour(europe.territories[2])
        southernEurope.addNeighbour(europe.territories[5])
        southernEurope.addNeighbour(africa.territories[4])
        southernEurope.addNeighbour(africa.territories[2])
        southernEurope.addNeighbour(asia.territories[6])
        
        ukraine.addNeighbour(europe.territories[2])
        ukraine.addNeighbour(europe.territories[3])
        ukraine.addNeighbour(europe.territories[4])
        ukraine.addNeighbour(asia.territories[0])
        ukraine.addNeighbour(asia.territories[6])
        ukraine.addNeighbour(asia.territories[10])
        
        westernEurope.addNeighbour(europe.territories[0])
        westernEurope.addNeighbour(europe.territories[2])
        westernEurope.addNeighbour(europe.territories[4])
        westernEurope.addNeighbour(africa.territories[4])
        
        
        '''Africa'''
        congo.addNeighbour(africa.territories[1])
        congo.addNeighbour(africa.territories[4])
        congo.addNeighbour(africa.territories[5])

        eastAfrica.addNeighbour(africa.territories[0])
        eastAfrica.addNeighbour(africa.territories[2])
        eastAfrica.addNeighbour(africa.territories[3])
        eastAfrica.addNeighbour(africa.territories[4])
        eastAfrica.addNeighbour(africa.territories[5])
        eastAfrica.addNeighbour(asia.territories[6])

        egypt.addNeighbour(africa.territories[1])
        egypt.addNeighbour(africa.territories[4])
        egypt.addNeighbour(asia.territories[6])
        egypt.addNeighbour(europe.territories[4])

        madagascar.addNeighbour(africa.territories[1])
        madagascar.addNeighbour(africa.territories[5])

        northAfrica.addNeighbour(africa.territories[0])
        northAfrica.addNeighbour(africa.territories[1])
        northAfrica.addNeighbour(africa.territories[2])
        northAfrica.addNeighbour(europe.territories[4])
        northAfrica.addNeighbour(europe.territories[6])
        northAfrica.addNeighbour(southAmerica.territories[1])

        southAfrica.addNeighbour(africa.territories[0])
        southAfrica.addNeighbour(africa.territories[1])
        southAfrica.addNeighbour(africa.territories[3])
        
        '''Asia'''
        kazakhstan.addNeighbour(asia.territories[6])
        kazakhstan.addNeighbour(asia.territories[2])
        kazakhstan.addNeighbour(asia.territories[1])
        kazakhstan.addNeighbour(asia.territories[10])
        kazakhstan.addNeighbour(europe.territories[5])

        china.addNeighbour(asia.territories[7])
        china.addNeighbour(asia.territories[9])
        china.addNeighbour(asia.territories[10])
        china.addNeighbour(asia.territories[0])
        china.addNeighbour(asia.territories[2])
        china.addNeighbour(asia.territories[8])

        india.addNeighbour(asia.territories[8])
        india.addNeighbour(asia.territories[1])
        india.addNeighbour(asia.territories[0])
        india.addNeighbour(asia.territories[6])

        irkutsk.addNeighbour(asia.territories[5])
        irkutsk.addNeighbour(asia.territories[11])
        irkutsk.addNeighbour(asia.territories[9])
        irkutsk.addNeighbour(asia.territories[7])

        japan.addNeighbour(asia.territories[5])
        japan.addNeighbour(asia.territories[7])

        kamchatka.addNeighbour(asia.territories[11])
        kamchatka.addNeighbour(asia.territories[3])
        kamchatka.addNeighbour(asia.territories[7])
        kamchatka.addNeighbour(asia.territories[4])

        middleEast.addNeighbour(asia.territories[2])
        middleEast.addNeighbour(asia.territories[0])
        middleEast.addNeighbour(europe.territories[5])
        middleEast.addNeighbour(europe.territories[4])
        middleEast.addNeighbour(africa.territories[2])
        middleEast.addNeighbour(africa.territories[1])

        mongolia.addNeighbour(asia.territories[4])
        mongolia.addNeighbour(asia.territories[5])
        mongolia.addNeighbour(asia.territories[3])
        mongolia.addNeighbour(asia.territories[9])
        mongolia.addNeighbour(asia.territories[1])

        siam.addNeighbour(asia.territories[1])
        siam.addNeighbour(asia.territories[2])
        siam.addNeighbour(australia.territories[1])

        siberia.addNeighbour(asia.territories[10])
        siberia.addNeighbour(asia.territories[1])
        siberia.addNeighbour(asia.territories[7])
        siberia.addNeighbour(asia.territories[3])
        siberia.addNeighbour(asia.territories[11])

        ural.addNeighbour(asia.territories[9])
        ural.addNeighbour(asia.territories[1])
        ural.addNeighbour(asia.territories[0])
        ural.addNeighbour(europe.territories[5])

        yakutsk.addNeighbour(asia.territories[5])
        yakutsk.addNeighbour(asia.territories[3])
        yakutsk.addNeighbour(asia.territories[9])
        
        
        '''Australia'''
        easternAustralia.addNeighbour(australia.territories[2])
        easternAustralia.addNeighbour(australia.territories[3])

        indonesia.addNeighbour(australia.territories[2])
        indonesia.addNeighbour(australia.territories[3])
        indonesia.addNeighbour(asia.territories[8])

        newGuinea.addNeighbour(australia.territories[0])
        newGuinea.addNeighbour(australia.territories[3])
        newGuinea.addNeighbour(australia.territories[1])

        westernAustralia.addNeighbour(australia.territories[0])
        westernAustralia.addNeighbour(australia.territories[2])
        westernAustralia.addNeighbour(australia.territories[1])
        
        '''Cards'''
        cards = []
         
        
        cards.append(Card(Card.TYPE_INFANTRY, alaska))
        cards.append(Card(Card.TYPE_INFANTRY, alberta))
        cards.append(Card(Card.TYPE_INFANTRY, argentina))
        cards.append(Card(Card.TYPE_ARTILLERY, brazil))
        cards.append(Card(Card.TYPE_CAVALRY, centralAmerica))
        cards.append(Card(Card.TYPE_CAVALRY, china))
        cards.append(Card(Card.TYPE_CAVALRY, congo))
        cards.append(Card(Card.TYPE_ARTILLERY, eastAfrica))
        cards.append(Card(Card.TYPE_INFANTRY, easternAustralia))
        cards.append(Card(Card.TYPE_ARTILLERY, easternUnitedStates))
        cards.append(Card(Card.TYPE_INFANTRY, egypt))
        cards.append(Card(Card.TYPE_CAVALRY, greatBritain))
        cards.append(Card(Card.TYPE_CAVALRY , greenland))
        cards.append(Card(Card.TYPE_INFANTRY, iceland))
        cards.append(Card(Card.TYPE_INFANTRY, india))
        cards.append(Card(Card.TYPE_CAVALRY, indonesia))
        cards.append(Card(Card.TYPE_INFANTRY, irkutsk))
        cards.append(Card(Card.TYPE_INFANTRY, japan))
        cards.append(Card(Card.TYPE_CAVALRY, kamchatka))
        cards.append(Card(Card.TYPE_INFANTRY, kazakhstan))
        cards.append(Card(Card.TYPE_INFANTRY, madagascar))
        cards.append(Card(Card.TYPE_ARTILLERY, middleEast))
        cards.append(Card(Card.TYPE_ARTILLERY, mongolia))
        cards.append(Card(Card.TYPE_CAVALRY, newGuinea))
        cards.append(Card(Card.TYPE_INFANTRY, northAfrica))
        cards.append(Card(Card.TYPE_CAVALRY, northernEurope))
        cards.append(Card(Card.TYPE_ARTILLERY, northwestTerritory))
        cards.append(Card(Card.TYPE_CAVALRY, ontario))
        cards.append(Card(Card.TYPE_CAVALRY, peru))
        cards.append(Card(Card.TYPE_ARTILLERY, quebec))
        cards.append(Card(Card.TYPE_ARTILLERY, scandinavia))
        cards.append(Card(Card.TYPE_ARTILLERY, siam))
        cards.append(Card(Card.TYPE_ARTILLERY, siberia))
        cards.append(Card(Card.TYPE_ARTILLERY, southAfrica))
        cards.append(Card(Card.TYPE_CAVALRY, southernEurope))
        cards.append(Card(Card.TYPE_ARTILLERY, ukraine))
        cards.append(Card(Card.TYPE_CAVALRY, ural))
        cards.append(Card(Card.TYPE_ARTILLERY, venezuela))
        cards.append(Card(Card.TYPE_ARTILLERY, westernAustralia))
        cards.append(Card(Card.TYPE_INFANTRY, westernEurope))
        cards.append(Card(Card.TYPE_INFANTRY, westernUnitedStates))
        cards.append(Card(Card.TYPE_CAVALRY, yakutsk))
        
        '''Goals'''
        goals = []
        
        goals.append(GoalFactory.createConquer())
        goals.append(GoalFactory.createOccupy())
        goals.append(GoalFactory.createEliminate(Player.COLOR_BLACK))
        goals.append(GoalFactory.createEliminate(Player.COLOR_BLUE))
        goals.append(GoalFactory.createEliminate(Player.COLOR_GRAY))
        goals.append(GoalFactory.createEliminate(Player.COLOR_GREEN))
        goals.append(GoalFactory.createEliminate(Player.COLOR_RED))
        goals.append(GoalFactory.createEliminate(Player.COLOR_YELLOW))
        goals.append(GoalFactory.createConquerContinent([northAmerica, africa]))
        goals.append(GoalFactory.createConquerContinent([northAmerica, australia]))
        goals.append(GoalFactory.createConquerContinent([asia, africa]))
        goals.append(GoalFactory.createConquerContinent([asia, southAmerica]))
    
        players = []
        players.append(CmdPlayer(Player.COLOR_BLACK))
        players.append(CmdPlayer(Player.COLOR_BLUE))
        players.append(CmdPlayer(Player.COLOR_GRAY))
        players.append(CmdPlayer(Player.COLOR_GREEN))
        players.append(CmdPlayer(Player.COLOR_RED))
        players.append(CmdPlayer(Player.COLOR_YELLOW))
        
        return Game(continents, goals, cards, players);
