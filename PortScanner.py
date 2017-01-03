import optparse
from socket import * 
from threading import *
import os 
import time
screenLock = Semaphore(value=1)

def connscan(tgtHost, tgtport):
	try:
			connSkt = socket(AF_INET, SOCK_STREAM)
			connSkt.connect((tgtHost, tgtport))
			connSkt.send("hello")

			result = connSkt.recv(100)
			screenLock.acquire()
			print "PORT    STATE"
			print str(tgtport) + "/tcp  Open"
	except:
			screenLock.acquire()
			print "PORT    STATE"
			print str(tgtport) + "/tcp Closed"
	finally:
			screenLock.acquire()
			connSkt.close()

def portscan(tgtHost, tgtports):
	try:

			tgtIP = gethostbyname(tgtHost)
	except:
			print "[ Website/IP Might Not accept the packet or its down! ]"
			return

	try:

			tgtName = gethostbyname(tgtIP)
			print "\nScan Results For: " + tgtHost
	except:
			print ("\nScan Results For: " + tgtHost)

	setdefaulttimeout(2)

	for tgtport in tgtports:
			t = Thread(target=connscan, args=(tgtHost, int(tgtport)))
			t.start()

def Main():
	parser = optparse.OptionParser('PortScanner.py -T <Target Host>'+\
			' -p <Target Ports>')
	parser.add_option('-T', dest = 'tgtHost', type='string', \
			help='specify target host')
	parser.add_option('-p', dest='tgtport', type='string', \
			help='Specify Target Port[%] seperated by a comma')
	(options, args) = parser.parse_args()
	if (options.tgtHost == None) | (options.tgtport == None):
		print parser.usage
		exit(1)
	else:
			tgtHost = options.tgtHost
			tgtports = str(options.tgtport).split('_')

	portscan(tgtHost, tgtports)


if __name__ == '__main__':
	Main()


print("Going To R-BOX In 5 Seconds")
time.sleep(5)
os.system("python menu.py")
