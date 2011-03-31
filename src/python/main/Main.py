'''
Created on 2011 3 31

@author: cihancimen
'''
from risk.DefaultGameSetup import DefaultGameSetup



if __name__ == '__main__':
    df = DefaultGameSetup()
    for goal in df.getGoals():
        print goal.verbose