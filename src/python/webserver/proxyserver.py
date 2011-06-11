from itty import *
from serveraccessor import ServerAccessor
import json
import sys
import traceback
@get("/serverstatus")
def serverstatus(req):
    try:
        host = req.GET.get('host', 'localhost')
        port = int(req.GET.get('port', '8080'))
        games = ServerAccessor.getStatus(host, port)
        return Response(json.dump(games), content_type='application/json')
    except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return 'Error %s, parameters were host %s, port %s' % (e, host, port)
    
run_itty(host='localhost', port=10000)