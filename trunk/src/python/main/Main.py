'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.default.DefaultGameSetup import DefaultGameSetup




if __name__ == '__main__':
    df = DefaultGameSetup();
    game = df.init()
    for cont in game.continents.values():
        #print cont.name
        i = 0
        for ter in cont.territories:
            i = i + 1
            print i, ter.name
            for n in ter.neighbours:
                print '\t', n.name            
