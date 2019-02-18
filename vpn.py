#/usr/bin/env python3
'''
__author__ = ' abba y abdullahi , lastloaded@gmail.com'
__copyright__ = ' copyright (c) 2019 by A  Y A  '
# its simple vpn which connect with tor its double vpn for any anonymous user
'''
import os
import time
def name():
    oper = os.system('sudo anonsurf start')
    if oper == ' Linux':
        print(' its working')
    elif (oper == 'Window'):
        pass
    else:
        print(' its not connect')

name()
