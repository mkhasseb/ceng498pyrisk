'''
Created on 2011 4 2

@author: cihancimen
'''

from risk.default.MinimalGameSetupSocket import MinimalGameSetupSocket



if __name__ == '__main__':
    df = MinimalGameSetupSocket();
    game = df.init()
    for cont in game.continents.values():
        #print cont.name
        i = 0
        for ter in cont.territories:
            i = i + 1
            print ter.name

    game.setup()
    victor = game.play()
    print 'victor is ', victor.color, ', with mission ', victor.mission  
