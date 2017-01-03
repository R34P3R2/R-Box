############################
#                          #
############################





############################
#         Modules          #
############################

import os
import signal
import sys
import time

###########################
#      End Of Modules     #
###########################





###########################
#      Colour Codes       #
###########################
G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m' #white
###########################
#   End Of Colour Codes   #
###########################





############################
#      Variables List      #
############################




############################
#   End of Variables list  #
############################





############################
#       Exit Message       #
############################

def signal_handler(signal, frame):
        print('\nEXITING R-BOX')
        print('Bye!!!')
        time.sleep(2)
        os.system("clear")
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

############################
#    End of Exit Message   #
############################

############################
#     LOADING SCRIPT       #
############################


os.system("resize -s 14 81 > /dev/null")
os.system("python load.py")
os.system("resize -s 22 59 > /dev/null")
os.system("clear")

############################
#  END OF LOADING SCRIPT   #
############################



############################
#           Logo           #
############################
def logo():
	print(''+G+'')

	os.system("clear")

	print('''
        ---_ ...... _/_ -    
       /  .      ./ .'*\ \       +=======================+
       : '         /__-'   \.    |  OPEN IN FULL SCREEN  |
      /                      )   +=======================+
    _/                  >   .'   |    :QUICK MESSSAGE:   |
  /   '   .       _.-" /  .'     |  Dont Ask To Get New  | 
  \           __/"     /.'       |    The New Version    | 
    \ '--  .-" /     //'         |        Earlier.       | 
     \|  \ | /     //            |      Thank You :D     |
          \:     //              +=======================+
       `\/     //  
        \__`\/ /  
           \_|''')

	print('\n    +=========================+')
	print('    |    Welcome To'+R+' R-Box '+G+'    |')
	print('    |      '+B+'Version: '+Y+'1.0.3 '+G+'    |')
	print('    +=========================+')
	print('    |  Type '+R+'help Or Commands'+G+'  |')
	print('    +=========================+')


############################
#       End Of  Logo       #
############################


##################################
# Code For Installation programs #
##################################



def installcupp():
	print("Installing CUPP")
	os.system("wget https://gist.githubusercontent.com/R34P3R2/7b5cb7eb53e5f9242191e5a1e5700e33/raw/a96ce42a318043292f380ffc6d36c2d872e0bbdf/cupp.cfg")
	os.system("wget https://gist.githubusercontent.com/R34P3R2/93ddc906db0a65b886284d77f6a27f24/raw/1073a172ccc046aa161b84a7fbfbfb5645fa6711/cupp.py")
	os.system("clear")
	print("CUPP Is Ready For Use")
	time.sleep(1.5)
	os.system("python cupp.py -i")


################################
# End Of installation programs #
################################






############################
#        Help Menu         #
############################

def com():

	choice = raw_input(''+Y+'{'+R+'Re4per'+B+'@'+W+'R-Box'+Y+'}'+W+'>>> ')

	if choice == ("help"):
		print('\n   '+W+'['+R+'==========================='+W+']')
		print('    [1]: Information Gathering')
		print('    [2]: Password Profiling')
		print('    [3]: Exploitation Tools')
		print('    [4]: Vulnerability Scanner')
		choice = raw_input(''+Y+'{'+R+'Re4per'+B+'@'+W+'R-Box'+Y+'}'+W+'>>> ')
	if choice == ('1'):
		print('\n'+R+'   +============================+')
		print('   | ['+W+'1'+R+']:'+W+' PORT SCANNER '+R+'         |')
		print('   | ['+W+'2'+R+']:'+W+' URL TO IP    '+R+'         |')
		print('   +============================+')



		ig = raw_input(''+Y+'{'+R+'Re4per'+B+'@'+W+'IG'+Y+'}'+W+'>>> ')

		if ig == ("1"):
			print('[1]: All Ports Scanned ')
			print('[2]: One Port Scanned')
			pc = raw_input(''+Y+'{'+R+'Re4per'+B+'@'+W+'Ports'+Y+'}'+W+'>>> ')

			if pc == ("1"):
				os.system("sh nport.sh")

			if pc == ("2"):
				os.system("sh cport.sh")


		if ig == ("back"):
			main()


		if ig == ("2"):
			print("Loading Script....\n")
			os.system("python UTI.py")
			banner()


	if choice == ("commands"):
		print(" COMMAND             INFO  ")
		print("\n  Help          Show Tools ")
		print("  credits   Show People who Helped")
		print("  contact       Ways To Contact Us")




	if choice == ("credits"):
		os.system("clear")
		print(''+R+'Coders:')
		print(''+G+'Main Coder: '+B+'Kamil Urbanski')
		print('\n'+R+'Special Thanks To: ')
		print(''+B+'Instagram: the.read.team')
		time.sleep(5)
		main()

	if choice == ("2"):
		print('\n'+R+'   +============================+')
		print('   | ['+W+'1'+R+']: '+W+'CUPP              '+R+'    |')
		print('   | ['+W+'2'+R+']: '+W+'Crunch            '+R+'    |')
		print('   | ['+W+'3'+R+']: '+W+'Oracle '+R+'  |')
		pp = raw_input(''+Y+'{'+R+'Re4per'+B+'@'+W+'IG'+Y+'}'+W+'>>> ')

		if pp == ("back"):
			main()

		if pp == ("1"):
			print('Have you Got Cupp.py in this directory\n'+R+'')
			os.system("ls")
			cuppin = raw_input(''+G+'Y/'+R+'N'+W+'? ')
			if cuppin == ("N"):
				installcupp()

			if cuppin == ("n"):
				installcupp()

			if cuppin == ("y"):
				os.system("python cupp.py -i")
				print("If the program hasnt started\n go back and install cupp :D")
				main()

			if cuppin == ("Y"):
				os.system("python cupp.py -i")
				print("If the program hasnt started\n go back and install cupp :D")
				main()

		if pp == ("2"):
			print("Crunch Will be Automatic in the next version")
			os.system("crunch")
			time.sleep(1.5)
			main()

		if pp == ("3"):
			print("[*]   Special Thanks To IG:The.Red.Team   [*]")
			print("[*]    For Letting Me Use Their Script    [*]")
			os.system("resize -s 26 84 > /dev/null")
			os.system("python oracle.py")

	if choice == ("3"):
		print('\n'+R+'   +============================+')
		print('   | ['+W+'1'+R+']: '+W+'SQL INJECTION     '+R+'    |')
		print('   | ['+W+'2'+R+']: '+W+'XXS TRACER        '+R+'    |')
		et = raw_input('{'+R+'Re4per'+B+'@'+W+'IG'+Y+'}'+W+'>>> ')
        



		if et == ("1"):
			sqlmapin = raw_input('Have You Got Sqlmap installed? '+G+'y'+B+'/'+R+'n'+G+'? '+Y+'')

			if sqlmapin == ("y"):
				os.system("sudo ./sqlauto && python menu.py")
	

			if sqlmapin == ("n"):
				os.system("sudo apt-get install sqlmap && cd sqlmap && chmod 777 sqlauto && ./sqlauto && python menu.py")



     		if et == ("2"):
     			xsstraccerin = raw_input('Have You Installed XSS TRACER BEFORE? '+G+'y/'+R+'n? ')
     			if xsstraccerin == ("n"):
     				os.system("git clone https://github.com/1N3/XSSTracer.git")
     				xsstraccertarget = raw_input("Target: ")
     				os.system("cd XSSTracer/ && python xsstracer.py %s 80"%xsstraccertarget)
     				os.system("cd .. && python menu.py")
     		
     		if xsstraccerin == ("y"):
     			xsstraccertarget = raw_input("Target: ")
     			os.system("cd XSSTracer/ && python xsstracer.py %s 80"%xsstraccertarget)
                os.system("cd .. && python menu.py")


	if choice == ("4"):
		print('\n'+R+'   +============================+')
		print('   | ['+W+'1'+R+']: '+W+'D-TECT (XSS & SQLi Scanncer)   |')        





	if choice == ("back"):
		main()










############################
#     End Of Help Menu     #
############################













############################
#     Start Of Program     #
############################

def main():
	logo()
	com()
	

main()
############################
# End Of Start Of Program  #
############################