from socket import *
import optparse
from threading import *

def connScan(Host, Port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((Host, Port))
        print('[+] %d/tcp Open' %Port)
    except:
        print('[+] %d/tcp Closed' % Port)
    finally:
        sock.close()

def portScan(Host, Ports):
    try:
        tgtIP = gethostbyname(Host)
    except:
        print('Unknown Host %s ' %Host)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan result for: ' + tgtName[0])
    except:
        print('[+] Scan result for: ' + tgtIP)
    setdefaulttimeout(1)
    for Port in Ports:
        t = Thread(target=connScan, args=(Host, int(Port)))
        t.start()

def main():
    parser = optparse.OptionParser("Usage of program: " + "-H <target_host> -p <target_port>")
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target ports separeted by comma")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPort == None):
        print(parser.usage)
        exit(0)
    else:
        portScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()
