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