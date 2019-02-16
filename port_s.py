import time 
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)
port = 1000
for  portx in  range(1,100):
    try:
       # s = input('enter your ip target:')
        s.connect(('www.arewablog.com',portx))
        r = s,recv(1024)
        if  'congratulations' in r.decode('utf8'):
            print('[I] hidden server found :  %s ~ %s' % (port,r.decode('utf8')))
            s.close()
            t = time.time()
            break
        else:
            print(' %s ~ %s ' % (port.r.decode('utf8')))
            s.close()
    except socket.error as  err:
        print('%s ~ %s' % (port,err))
    port +=  1000
