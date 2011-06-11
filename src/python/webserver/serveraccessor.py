import socket
import time

class ServerAccessor:
    @staticmethod
    def getStatus(host, port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            time.sleep(1)
            buf = s.recv(1).encode()
            ddd = ''
            ddd += buf
            while (not 'EOF' in ddd):
                print 'buf:', buf
                print 'ddd:', ddd
                buf=s.recv(1).encode()
                ddd = ddd + '%s' % buf
            s.close()
            games = {}
            print ddd
            gds = ddd.split('\n')[-1]
            for gs in gds: 
                print gs
                g = gs.split(',')
                games[g[0]] = {'name': g[0], 'address': g[1], 'players': g[2]}
            return games
        