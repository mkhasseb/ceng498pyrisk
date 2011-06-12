from ClientHelper import ClientHelper
from itty import *
from serveraccessor import ServerAccessor
import json
import sys
import traceback
import uuid

COLOR_RED = "Red"
COLOR_LPINK = "Pink"
COLOR_GREEN = "Green"
COLOR_GRAY = "Gray"
COLOR_ORANGE = "Orange"
COLOR_YELLOW = "Yellow"
clientHelpers = {}
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
            print clientHelpers[id]
            print clientHelpers[id].map
            return clientHelpers[id].map
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return 'Error %s, parameters were id=%s' % (e, id)     




def parseMap(map):
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
            region['points'].add(point)
    return 
        

run_itty(host='localhost', port=10000)