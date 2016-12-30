import os
import signal
import sys
import time
yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n','N','NO'])


ws = set(['ws', 'WS', 'Ws'])

G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m' #white

def choose():
	choice = raw_input("R-BOX >>>")

	if choice == ("help"):
		os.system("cat help.txt")
	
	if choice == ('1'):
		print('    ['+G+'ws'+B+']: Wireshark '+Y+' ('+R+'Sniffs packets on your LAN GUI'+Y+')'+B+'')
		print('    ['+G+'ns'+B+']: NetSniff'+Y+'   ('+R+'Sniffs packets on your LAN Not GUI'+Y+')'+B+'')
		print('    ['+G+'ec'+B+']: ettercap'+Y+'   ('+R+'spoofing & sniffing GUI'+Y+')'+B+'')
		print('    ['+G+'dn'+B+']: Driftnet'+Y+'   ('+R+'Sniffers for pictures on your LAN GUI'+Y+')'+B+'')


		print('			     Type Back to go to the main menu')
		sas = raw_input("[S&S]>>>")

		if choice == ("back"):
			os.system("clear")
			banner()
		if choice == ('dn'):
			os.system("sudo driftnet")
			print("Run the Requirements install program\n if the program doesnt work ")
			time.sleep(4)

		if choice == ('ws'):
			print('Starting....')
			os.system("sudo wireshark")
			print("Run the Requirements install program\n if the program doesnt work ")
			time.sleep(6)
			banner()

		if choice == ('ns'):
			print("Starting....")
			os.system("sudo netsniff-ng")
			print("Run the Requirements install program\n If the program didnt work ")
			banner()

		if choice == ('mac'):
			print("Setting a Random Mac Address")
			os.system("sudo macchanger -r wlan0")
			time.sleep(2)
			banner()

		else:
			print("Incorrect Choice!")
			time.sleep(2)
			clear
			banner()


	if choice == ('2'):
		print('    ['+G+'CP'+B+']: CUPP '+Y+' ('+R+'Create password list on a Target'+Y+')'+B+'')
		print('    ['+G+'CH'+B+']: Crunch '+Y+' ('+R+'Create password from set charcters'+Y+')'+B+'')
		pp = raw_input("[PP]>>> ")
		if pp == ("cp"):
			print('Starting....')
			os.system("python cupp.py -i ")
		if pp == ("CH"):
			print('Still trying to be fixed')
			time.sleep(3)
			banner()

	if choice == ("clear"):
		os.system("clear")


	if choice == ('6'):
		print(''+R+'TOOLS TO SQL INJECT:')
		print('   '+B+' ['+G+'SQ'+B+']: SQLMAP '+Y+' ('+R+'Sql Injection Not Gui '+Y+')'+B+'')
		print('   '+B+' ['+G+'JQ'+B+']: jsql '+Y+' ('+R+'Sql Injection GUI'+Y+')'+B+'')
		exotool = raw_input("[ET]>>> ")
		if exotool == ('SQ'):
			os.system("sudo ./automaticsql")
			banner()

		if exotool == ('JQ'):
			os.system("jsql")
			banner()
		banner()





def banner():
	(G,W,R,B)
	print(''+R+'')
	print("""
 _______         ______   _______          
(  ____ )       (  ___ \ (  ___  )|\     /|
| (    )|       | (   ) )| (   ) |( \   / )
| (____)| _____ | (__/ / | |   | | \ (_) / 
|     __)(_____)|  __ (  | |   | |  ) _ (  
| (\ (          | (  \ \ | |   | | / ( ) \ 
| ) \ \__       | )___) )| (___) |( /   \ )
|/   \__/       |/ \___/ (_______)|/     \|""")
	print(' \n                                 '+G+' {'+R+'Version '+B+'1.0.0'+G+'}   ')
	print('\n'+B+'['+R+'|||'+B+']'+R+'===================================='+B+'['+R+'|||'+B+']') 
	print(''+B+'['+R+'|||'+B+']  '+Y+'    Coded By: '+R+'Kamil Urbanski   '+B+'   ['+R+'|||'+B+']')                                             
	print(''+B+'['+R+'|||'+B+']  '+Y+' www.facebook.com/RBOX.FRAMEWORK  '+B+'['+R+'|||'+B+']')                                             
	print(''+B+'['+R+'|||'+B+']  '+Y+'        Enjoy Hacking!!           '+B+'['+R+'|||'+B+']')  
	print('['+R+'|||'+B+']'+R+'===================================='+B+'['+R+'|||'+B+']') 
	print '['+R+'|||'+B+']'+R+'               Type ''help''            '+B+'['+R+'|||'+B+']' 
	print('['+R+'|||'+B+']'+R+'===================================='+B+'['+R+'|||'+B+']') 
	choose()


def signal_handler(signal, frame):
        print('\nEXITING!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)




def main():
	os.system("resize -s 14 81 > /dev/null")
	os.system("python load.py")
	os.system("resize -s 28 57 > /dev/null")
	os.system("clear")
	banner()
	choose()




main()


