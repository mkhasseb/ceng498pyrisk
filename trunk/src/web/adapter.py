from mod_python import  Session,util,psp
from httplib import HTTPConnection
import traceback
import sys
def serverstatus(req, host='localhost', port='8090'):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/serverstatus?host=%s&port=%s" % (host, port))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def join(req, host='localhost', port='8090'):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/join?host=%s&port=%s" % (host, port))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def mapFileName(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/mapFileName?id=%s" % id)
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def map(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/map?id=%s" % id)
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def worldMap(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/worldMap?id=%s" % id)
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e
    
def log(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/log?id=%s" % id)
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e
    
def state(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/state?id=%s" % id)
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def placeSingle(req, id=None, name=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/placeSingle?id=%s&name=%s" % (id, name))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def placeArmy(req, id=None, placeArmyStr=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/placeArmy?id=%s&placeArmyStr=%s" % (id, placeArmyStr))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def placeIncome(req, id=None, placeIncomeStr=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/placeIncome?id=%s&placeIncomeStr=%s" % (id, placeIncomeStr))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def trade(req, id=None, cardNums=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/trade?id=%s&cardNums=%s" % (id, cardNums))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def move(req, id=None, moveStr=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/move?id=%s&moveStr=%s" % (id, moveStr))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def attack(req, id=None, attackStr=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/attack?id=%s&attackStr=%s" % (id, attackStr))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def defend(req, id=None, diceNum=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/defend?id=%s&diceNum=%s" % (id, diceNum))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def transfer(req, id=None, armyNum=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/transfer?id=%s&armyNum=%s" % (id, armyNum))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e

def doPass(req, id=None):
    try:
        conn = HTTPConnection("localhost:10000")
        conn.request("GET", "/doPass?id=%s" % (id))
        r = conn.getresponse()
        data = r.read()
        conn.close()
        if data.startswith('Error'):
            return 'Error %s' % data
        return data
    except Exception as e:
        print traceback.print_exc(file=sys.stdout)
        return 'Error %s' % e


