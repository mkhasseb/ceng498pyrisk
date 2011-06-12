import socket
import time

class ServerAccessor:
    @staticmethod
    def getStatus(host, port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            ddd = s.recv(10000)
            
            #while (not 'EOF' in ddd):
            #    print 'buf:', buf
            #    print 'ddd:', ddd
            #    buf=s.recv(1).encode()
            #    ddd = ddd + '%s' % buf
            s.close()
            games = {}
            print ddd
            gds = ddd.split('*')[:-1]
            print gds
            for gs in gds: 
                print 'gs:', gs
                g = gs.split(',')
                games[g[0]] = {'name': g[0].encode(), 'address': g[1].encode(), 'players': g[2].encode()}
            return games
        