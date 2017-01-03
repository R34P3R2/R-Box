#!/usr/bin/env python
from socket import * 
import os
import time

target = raw_input('Website: ')
print("")
targetIP = gethostbyname(target)
print targetIP
print("\n IT will return you to the R-Box Menu\n In 5 Seconds")
time.sleep(5)
os.system("python menu.py")