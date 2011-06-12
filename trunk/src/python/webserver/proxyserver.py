from ClientHelper import ClientHelper
from itty import *
from serveraccessor import ServerAccessor
import json
import sys
import traceback
import uuid
import time

COLOR_RED = "Red"
COLOR_LPINK = "Pink"
COLOR_GREEN = "Green"
COLOR_GRAY = "Gray"
COLOR_ORANGE = "Orange"
COLOR_YELLOW = "Yellow"
clientHelpers = {}
mapFileNames = {}
occupantColors = { COLOR_RED : "#FD121A",  COLOR_LPINK : "#EE8FFF", COLOR_GREEN : "#93FF1F", COLOR_GRAY: "#B7B7B7", COLOR_ORANGE: "#FB710E", COLOR_YELLOW:"#F1ED04"}
continentColors = ["#029D11", "#010AFE", "#9703D6", "#713800", "#601515", "#000000", "#FFFFFF"]

def sendAsJSON(data):
    return Response(json.dumps(data), content_type='application/json') 

@get("/serverstatus")
def serverstatus(req):
    try:
        host = req.GET.get('host', 'localhost')
        port = int(req.GET.get('port', '8080'))
        games = ServerAccessor.getStatus(host, port)
        return sendAsJSON(games)
    except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return 'Error %s, parameters were host %s, port %s' % (e, host, port)
        
@get("/mapFileName")
def mapFileName(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            return sendAsJSON({'fileName': clientHelpers[id].fname})
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were host %s, port %s' % (e, host, port) 
         
@get("/join")
def join(req):
    try:
        host = req.GET.get('host', None)
        port = req.GET.get('port', None)
        if(not host or not port):
            return 'Error host or port not set'
        else:
            id = str(uuid.uuid4())
            ch = ClientHelper(host, int(port))
            clientHelpers[id] = ch
            clientHelpers[id].start()
            return sendAsJSON({'id': id})
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were host %s, port %s' % (e, host, port)

@get("/map")
def map(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            time.sleep(3)
            print 'mm', clientHelpers[id].map
            return sendAsJSON(parseMap(clientHelpers[id].map))
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)     

def parseMap(map):
    print 'map', map
    lines = map.split("\n")
    for i in range(len(lines)):
        if(lines[i] == "" or ("Turn of" in lines[i])):
            del lines[i]
    numReg = int(lines[0])
    numCont = int(lines[numReg + 1])
    regions = []
    conts = []
    for i in range(numCont):
        (conname, bonus) = lines[numReg + 2 + i].split(",")
        cont = {'name': conname, 'bonus':bonus, 'regions': [], 'color' : continentColors[i]}
        conts.append(cont)
    for i in range(numReg):
        regStr = lines[i+1]
        [namecont,neighbours,points] = regStr.split(":")
        [name, contName] = namecont.split(',')
        neighbours = neighbours.split(',')[:-1]
        points = points.split(',')[:-1]
        region = {'name': name, 'continent': contName, 'neighbours': neighbours, 'points' : [], 'color' : '#FFFFFF'}
        regions.append(region)
        for p in points:
            point  = { 'x': (p.split('-')[0]), 'y': (p.split('-')[1])}
            region['points'].append(point)
    return {'regions' :  regions, 'continents': conts, 'colors': occupantColors}
        
@get("/worldMap")
def worldMap(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            print clientHelpers[id]
            print clientHelpers[id].worldMap
            wm = clientHelpers[id].worldMap
            if wm == '':
                return 'Error empty string'
            wmDict = {'regions':[]}
            regions = wm.split('\n')[:-1]
            for region in regions:
                [name, color, armyNum] = region.split(',')
                r={'name':name, 'occupant':color, 'armyNum':armyNum}
                wmDict['regions'].append(r)
            return sendAsJSON(wmDict)
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/log")
def log(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            return clientHelpers[id].logstr
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/state")
def state(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            return clientHelpers[id].currentState
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/placeSingle")
def placeSingle(req):
    try:
        id = req.GET.get('id', None)
        name = req.Get.get('name', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not name):
            return 'Error no name'
        else:
            clientHelpers[id].place(terr = name)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/placeArmy")
def placeArmy(req):
    try:
        id = req.GET.get('id', None)
        placeArmyStr = req.Get.get('placeArmyStr', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not placeArmyStr):
            return 'Error no place army string'
        else:
            [name, armyNum] = placeArmyStr.split(',')
            clientHelpers[id].place(terr = name, army = armyNum)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/placeIncome")
def placeIncome(req):
    try:
        id = req.GET.get('id', None)
        placeIncomeStr = req.Get.get('placeIncomeStr', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not placeIncomeStr):
            return 'Error no place income string'
        else:
            [name, armyNum] = placeIncomeStr.split(',')
            clientHelpers[id].place(terr = name, army = armyNum)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/trade")
def trade(req):
    try:
        id = req.GET.get('id', None)
        cardNums = req.Get.get('cardNums', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not cardNums):
            return 'Error no card nums string'
        else:
            cards = cardNums.split(',')
            clientHelpers[id].trade(cards)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/move")
def move(req):
    try:
        id = req.GET.get('id', None)
        moveStr = req.Get.get('moveStr', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not moveStr):
            return 'Error no move string'
        else:
            [fromTerr, toTerr, armyNum] = moveStr.split(',')
            clientHelpers[id].move(fromTerr, toTerr, armyNum)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/attack")
def attack(req):
    try:
        id = req.GET.get('id', None)
        attackStr = req.Get.get('attackStr', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not attackStr):
            return 'Error no attack string'
        else:
            [fromTerr, toTerr, armyNum] = attackStr.split(',')
            clientHelpers[id].attack(fromTerr, toTerr, armyNum)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/defend")
def defend(req):
    try:
        id = req.GET.get('id', None)
        diceNum = req.Get.get('diceNum', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not diceNum):
            return 'Error no dice number'
        else:
            clientHelpers[id].defend(diceNum)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/transfer")
def transfer(req):
    try:
        id = req.GET.get('id', None)
        armyNum = req.Get.get('armyNum', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        if(not diceNum):
            return 'Error no dice number'
        else:
            clientHelpers[id].place(army = armyNum, captured = True)
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

@get("/doPass")
def doPass(req):
    try:
        id = req.GET.get('id', None)
        if(not id or not id in clientHelpers):
            return 'Error no or wrong id'
        else:
            clientHelpers[id].doPass()
            return 'Success'
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)

run_itty(host='localhost', port=10000)
