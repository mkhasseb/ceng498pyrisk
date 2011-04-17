'''
Created on 2011 3 31

@author: cihancimen
'''
import sys

from risk.default.DefaultGameSetup import DefaultGameSetup



if __name__ == '__main__':
    argc = len(sys.argv)
    
        
    if(argc == 2):
        df = DefaultGameSetup(sys.argv[1])
    elif(argc == 3):
        df = DefaultGameSetup(sys.argv[1], host = sys.argv[2])
    elif(argc == 4):
        df = DefaultGameSetup(sys.argv[1], host = sys.argv[2], port = int(sys.argv[3]))
    else:
        print 'Usage game mode 1 or 2, optional arguments <host> <port>'
        sys.exit(0)
    game = df.init()

    game.setup()
    victor = game.play()
    print 'victor is ', victor.color, ', with mission ', victor.mission        

'''from risk.default.MinimalGameSetup import MinimalGameSetup


if __name__ == '__main__':
    df = MinimalGameSetup();
    game = df.init()
    for cont in game.continents.values():
        #print cont.name
        i = 0
        for ter in cont.territories:
            i = i + 1
            print ter.name

    game.setup()
    victor = game.play()
    print 'victor is ', victor.color, ', with mission ', victor.mission'''
