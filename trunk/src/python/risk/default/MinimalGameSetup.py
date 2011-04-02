'''
Created on 2011 4 2

@author: cihancimen
'''
from risk.Game import Game
from risk.Territory import Territory
from risk.Continent import Continent
from risk.Card import Card
from risk.Goal import GoalFactory
from risk.Player import Player
from risk.cmd.CmdPlayer import CmdPlayer

class MinimalGameSetup(object):
    def __init__(self):
        pass
    def init(self):
        
        a = Territory("a")
        b = Territory("b")
        c = Territory("c")
        d = Territory("d")
        e = Territory("e")
        
        a.addNeighbour(b);
        a.addNeighbour(c);
        
        b.addNeighbour(a)
        b.addNeighbour(c)
        
        c.addNeighbour(a)
        c.addNeighbour(b)
        c.addNeighbour(d)
        c.addNeighbour(e)
        
        d.addNeighbour(c)
        
        e.addNeighbour(c)
        
        abc = Continent("ABC", [a,b,c], 5)
        de = Continent("DE", [d,e], 3)
        
        continents = [abc, de]
        cards = []
        cards.append(Card(Card.TYPE_INFANTRY, territory=a))
        cards.append(Card(Card.TYPE_CAVALRY, territory=b))
        cards.append(Card(Card.TYPE_CAVALRY, territory=c))
        cards.append(Card(Card.TYPE_INFANTRY, territory=c))
        cards.append(Card(Card.TYPE_CAVALRY, territory=d))
        cards.append(Card(Card.TYPE_INFANTRY, territory=e))
        cards.append(Card(Card.TYPE_WILD))
        goals = []
        goals.append( GoalFactory.createConquer(4, 5))
        goals.append( GoalFactory.createConquer(5, 2))
        goals.append( GoalFactory.createEliminate(Player.COLOR_BLACK, 5))
        goals.append( GoalFactory.createEliminate(Player.COLOR_BLUE, 5))
        
        players = []
        players.append(CmdPlayer(Player.COLOR_BLACK))
        players.append(CmdPlayer(Player.COLOR_BLUE))
        
        return Game(continents, goals, cards, players)