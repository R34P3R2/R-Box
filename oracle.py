#!/usr/bin/python

import os
import re
import sys
import random
import string
import itertools
from collections import Counter
from datetime import datetime
wordList = []
diag=0
num80=4
num90=4
charz="0123456789"
t7=datetime.now()
t10=t7-t7
num99=xrange(num80, num90+1)
for namber in num99:
	for cs in itertools.product(charz, repeat=namber):
		t8=datetime.now()
		#print"Running system diagnostics..."
		world = ''.join(cs)
		#os.system("clear")
		t9=datetime.now()
		t10=t10+(t9-t8)
di=t10/110
	
loop=True
while loop == True:
	outcome=0
	

	randint = random.randrange(1, 10+1)
	
	if randint == 1:
		strings = '''
    )                                  
 ( /(                       (          
 )\())   (        )         )\     (   
((_)\    )(    ( /(    (   ((_)   ))\  
  ((_)  (()\   )(_))   )\   _    /((_) 
 / _ \   ((_) ((_)_   ((_) | |  (_))   
| (_) | | '_| / _` | / _|  | |  / -_)  
 \___/  |_|   \__,_| \__|  |_|  \___|
'''
	elif randint == 2:
		strings = '''
     /\  \         /\  \         /\  \         /\  \         /\__\     /\  \    
    /::\  \       /::\  \       /::\  \       /::\  \       /:/  /    /::\  \   
   /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \  
  /:/  \:\  \   /::\~\:\  \   /::\~\:\  \   /:/  \:\  \   /:/  /    /::\~\:\  \ 
 /:/__/ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/\:\ \:\__\
 \:\  \ /:/  / \/_|::\/:/  / \/__\:\/:/  / \:\  \  \/__/ \:\  \    \:\~\:\ \/__/
  \:\  /:/  /     |:|::/  /       \::/  /   \:\  \        \:\  \    \:\ \:\__\  
   \:\/:/  /      |:|\/__/        /:/  /     \:\  \        \:\  \    \:\ \/__/  
    \::/  /       |:|  |         /:/  /       \:\__\        \:\__\    \:\__\    
     \/__/         \|__|         \/__/         \/__/         \/__/     \/__/    
'''
	elif randint == 3:
		strings = '''
                                                                                                 _____   
       ____      ___________           _____                 _____     _____                _____\    \  
   ____\_  \__   \          \        /      |_          _____\    \_  |\    \              /    / |    | 
  /     /     \   \    /\    \      /         \        /     /|     |  \\    \            /    /  /___/| 
 /     /\      |   |   \_\    |    |     /\    \      /     / /____/|   \\    \          |    |__ |___|/ 
|     |  |     |   |      ___/     |    |  |    \    |     | |____|/     \|    | ______  |       \       
|     |  |     |   |      \  ____  |     \/      \   |     |  _____       |    |/      \ |     __/ __    
|     | /     /|  /     /\ \/    \ |\      /\     \  |\     \|\    \      /            | |\    \  /  \   
|\     \_____/ | /_____/ |\______| | \_____\ \_____\ | \_____\|    |     /_____/\_____/| | \____\/    |  
| \_____\   | /  |     | | |     | | |     | |     | | |     /____/|    |      | |    || | |    |____/|  
 \ |    |___|/   |_____|/ \|_____|  \|_____|\|_____|  \|_____|    ||    |______|/|____|/  \|____|   | |  
  \|____|                                                    |____|/                            |___|/  
'''
	elif randint == 4:
		strings = '''
  ______   .______           ___        ______  __       _______ 
 /  __  \  |   _  \         /   \      /      ||  |     |   ____|
|  |  |  | |  |_)  |       /  ^  \    |  ,----'|  |     |  |__   
|  |  |  | |      /       /  /_\  \   |  |     |  |     |   __|  
|  `--'  | |  |\  \----. /  _____  \  |  `----.|  `----.|  |____ 
 \______/  | _| `._____|/__/     \__\  \______||_______||_______|
'''
	elif randint == 5:
		strings = '''
________                           .__           
\_____  \  _______ _____     ____  |  |    ____  
 /   |   \ \_  __ \\__  \  _/ ___\ |  |  _/ __ \ 
/    |    \ |  | \/ / __ \_\  \___ |  |__\  ___/ 
\_______  / |__|   (____  / \___  >|____/ \___  >
        \/              \/      \/            \/ 
'''
	elif randint == 6:
		strings = '''
    ,o888888o.     8 888888888o.            .8.              ,o888888o.    8 8888         8 8888888888   
 . 8888     `88.   8 8888    `88.          .888.            8888     `88.  8 8888         8 8888         
,8 8888       `8b  8 8888     `88         :88888.        ,8 8888       `8. 8 8888         8 8888         
88 8888        `8b 8 8888     ,88        . `88888.       88 8888           8 8888         8 8888         
88 8888         88 8 8888.   ,88'       .8. `88888.      88 8888           8 8888         8 888888888888 
88 8888         88 8 888888888P'       .8`8. `88888.     88 8888           8 8888         8 8888         
88 8888        ,8P 8 8888`8b          .8' `8. `88888.    88 8888           8 8888         8 8888         
`8 8888       ,8P  8 8888 `8b.       .8'   `8. `88888.   `8 8888       .8' 8 8888         8 8888         
 ` 8888     ,88'   8 8888   `8b.    .888888888. `88888.     8888     ,88'  8 8888         8 8888         
    `8888888P'     8 8888     `88. .8'       `8. `88888.     `8888888P'    8 888888888888 8 888888888888 
'''
	elif randint == 7:
		strings = '''

 .d88888b.                            888          
d88P" "Y88b                           888          
888     888                           888          
888     888 888d888  8888b.   .d8888b 888  .d88b.  
888     888 888P"       "88b d88P"    888 d8P  Y8b 
888     888 888     .d888888 888      888 88888888 
Y88b. .d88P 888     888  888 Y88b.    888 Y8b.     
 "Y88888P"  888     "Y888888  "Y8888P 888  "Y8888  
'''
	elif randint == 8:
		strings = '''
        ....                                                  ..            
    .x~X88888Hx.                                        x .d88"             
   H8X 888888888h.      .u    .                          5888R              
  8888:`*888888888:   .d88B :@8c        u           .    '888R        .u    
  88888:        `%8  ="8888f8888r    us888u.   .udR88N    888R     ud8888.  
. `88888          ?>   4888>'88"  .@88 "8888" <888'888k   888R   :888'8888. 
`. ?888%           X   4888> '    9888  9888  9888 'Y"    888R   d888 '88%" 
  ~*??.            >   4888>      9888  9888  9888        888R   8888.+"    
 .x88888h.        <   .d888L .+   9888  9888  9888        888R   8888L      
:"""8888888x..  .x    ^"8888*"    9888  9888  ?8888u../  .888B . '8888c. .+ 
`    `*888888888"        "Y"      "888*""888"  "8888P'   ^*888%   "88888%   
        ""***""                    ^Y"   ^Y'     "P'       "%       "YP'    

'''
	elif randint == 9:
		strings = '''

   _ \                          |        
  |   |    __|    _` |    __|   |    _ \ 
  |   |   |      (   |   (      |    __/ 
 \___/   _|     \__,_|  \___|  _|  \___|
'''
	elif randint == 10:
		strings = '''
 ________      ________      ________      ________      ___           _______      
|\   __  \    |\   __  \    |\   __  \    |\   ____\    |\  \         |\  ___ \     
\ \  \|\  \   \ \  \|\  \   \ \  \|\  \   \ \  \___|    \ \  \        \ \   __/|    
 \ \  \\\  \   \ \   _  _\   \ \   __  \   \ \  \        \ \  \        \ \  \_|/__  
  \ \  \\\  \   \ \  \\  \|   \ \  \ \  \   \ \  \____    \ \  \____    \ \  \_|\ \ 
   \ \_______\   \ \__\\ _\    \ \__\ \__\   \ \_______\   \ \_______\   \ \_______\
    \|_______|    \|__|\|__|    \|__|\|__|    \|_______|    \|_______|    \|_______|
'''
	os.system("clear")
	print"Developed By: @the.red.team"
	print"Press 'return' to load new banner"
	print strings
	print"Oracle - password dictionary file generator"
	print"v2.2\n"
	count=1
	
	lines=0
	try:
		chars=raw_input("Enter characters and numbers to use\n>>> ")
		if chars=="":
			loop=True
			continue
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	os.system("clear")
	try:
		num1=input("Enter minimum length of string\nDefault is '1'\n>>> ")
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	except SyntaxError:
		num1=1
	except ValueError:
		num1=1
	os.system("clear")
	try:
		num2=input("Enter maximum length of string\nDefault is '16'\n>>> ")
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	except SyntaxError:
		num2=16
	except ValueError:
		num2=16
	os.system("clear")
	try:
		interval=input("Enter the interval to display progress(1000 = Display every 1000 lines)\n>>> ")
		repeat = False
	except SyntaxError:
		interval = 1000
		repeat=False
		pass
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	except ValueError:
		repeat=False
	os.system("clear")
	keyword=True
	try:
		extra = ""
		while extra != "?":
			extra=raw_input("Enter static key word\nDefault is no word(Enter a ? when finished)\n>>> ")
			if extra=="":
				keyword=False
				#extra = "?"
				break
			else:
				if extra != "?":
					wordList.append(extra)
				keyword = True
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	os.system("clear")
	try:
		file=raw_input("Enter name of output file\nFile extension will be added automatically\n>>> ")
		if file == "":
			file="Oracle.txt"
		else:
			file=file + ".txt"
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	os.system("clear")
	if keyword==True:
		try:
			choice=raw_input("1) Keyword before random string \n2) Keyword after random string \n>>> ")
			if choice=="1":
				order=str(wordList)+" : "+chars
			elif choice=="2":
				order= chars+" : "+str(wordList)
			else:
				os.system("clear")
				print"That is not an option"
				order=str(wordList)+" : "+chars
				print("Default is: %s" %(order))
				choice="1"
			os.system("clear")
		except KeyboardInterrupt:
			os.system("clear")
			print"Exiting"
			sys.exit()
	elif keyword==False:
		choice="1"
	num3=xrange(num1, num2+1)
	count=len(chars)
	for num in num3:
		if keyword == True:
			for extra in wordList:
				outcome=outcome+(count**num)
		else:
			outcome=outcome+(count**num)
	if outcome < repeat:
		data=outcome
	elif repeat==False:
		data=outcome
	elif repeat < outcome:
		data = repeat
	else:
		data=outcome
	bytes=0
	show=True
	if keyword==True:
		for extra in wordList:
			os.system("clear")
			#print('Keyword is true')
			#print wordList
			if data==outcome:
				for numt in num3:
					bytes=bytes+((len(chars)**numt)*numt)
					#bytes=bytes+((len(chars)*numt)*(len(chars)*numt))
					#bytes=bytes+(data*numt)
				big=bytes+data
				if keyword==True:
					big=big+(len(extra)*data)
			#byte=bytes/10
			#big=byte+bytes
			elif data==repeat:
				bin=0
				ball=0
				boots=0
				bun=0
				num4=xrange(num1, num2+1)
				for jag in num4:
					boots=boots+(len(chars)**jag)
					if boots<data:
						bun=boots
						while bin < bun:
							bin=bin+1
							ball=ball+jag
					elif data<boots:
						bun=data
						while bin < bun:
							bin=bin+1
							ball=ball+jag
					#while bin < data & bun:
					#	bin=bin+1
					#	ball=ball+jag
				big=ball+data
				if keyword==True:
					big=big+(len(extra)*data)
				#show=False
			print ("Parameters\n****************************\nCharacters:       %s \nLength of string: %d - %d \nLines:            %d \nKeyword:          %s \nFile name:        %s" %(chars, num1, num2, data, wordList, file))
			if keyword==True:
				print("String order:     %s" %(order))
			if show!=False:
				if big<1000000:
					kill=big/1000
					ter=("%d kilobytes" %(kill))
				elif big >= 1000000:
					if big < 999999999:
						kill=big/1000000
						ter=("%d megabytes" %(kill))
					elif big >= 1000000000:
						if big < 999999999999:
							kill=big/1000000000
							ter=("%d gigabytes" %(kill))
						elif big >= 1000000000000:
							kill=big/1000000000000
							ter=("%d terabytes" %(kill))
				print("Output size:      %d Bytes   /   %s" %(big, ter))
			try:
				hurry=di*data
				good=True
			except OverflowError:
				print"***WARNING***\nThe time predicted to complete to file based\non the parameters set is too long to\npredict\n"
				good=False
			if good==True:
				print("Estimated time:   %s" %(hurry))
			elif good==False:
				print("Estimated time:   >999999999 days")
			print"****************************\n"
	else:
		if data==outcome:
			for numt in num3:
				bytes=bytes+((len(chars)**numt)*numt)
				#bytes=bytes+((len(chars)*numt)*(len(chars)*numt))
				#bytes=bytes+(data*numt)
			big=bytes+data
			if keyword==True:
				big=big+(len(extra)*data)
		#byte=bytes/10
		#big=byte+bytes
		elif data==repeat:
			bin=0
			ball=0
			boots=0
			bun=0
			num4=xrange(num1, num2+1)
			for jag in num4:
				boots=boots+(len(chars)**jag)
				if boots<data:
					bun=boots
					while bin < bun:
						bin=bin+1
						ball=ball+jag
				elif data<boots:
					bun=data
					while bin < bun:
						bin=bin+1
						ball=ball+jag
				#while bin < data & bun:
				#	bin=bin+1
				#	ball=ball+jag
			big=ball+data
			if keyword==True:
				big=big+(len(extra)*data)
			#show=False
		print ("Parameters\n****************************\nCharacters:       %s \nLength of string: %d - %d \nLines:            %d \nKeyword:          %s \nFile name:        %s" %(chars, num1, num2, data, extra, file))
		if keyword==True:
			print("String order:     %s" %(order))
		if show!=False:
			if big<1000000:
				kill=big/1000
				ter=("%d kilobytes" %(kill))
			elif big >= 1000000:
				if big < 999999999:
					kill=big/1000000
					ter=("%d megabytes" %(kill))
				elif big >= 1000000000:
					if big < 999999999999:
						kill=big/1000000000
						ter=("%d gigabytes" %(kill))
					elif big >= 1000000000000:
						kill=big/1000000000000
						ter=("%d terabytes" %(kill))
			print("Output size:      %d Bytes   /   %s" %(big, ter))
		try:
			hurry=di*data
			good=True
		except OverflowError:
			print"***WARNING***\nThe time predicted to complete to file based\non the parameters set is too long to\npredict\n"
			good=False
		if good==True:
			print("Estimated time:   %s" %(hurry))
		elif good==False:
			print("Estimated time:   >999999999 days")
		print"****************************\n"
	try:
		go=raw_input("Press 'return' to begin...")
	except KeyboardInterrupt:
		os.system("clear")
		print"Exiting"
		sys.exit()
	t1 = datetime.now()
	t12 = datetime.now()
	monitor = 0
	inc = 0
	disp = 0
	perc = 0
	for number in num3:
		if keyword == True:
			for extra in wordList:
				for xs in itertools.product(chars, repeat=number):
					#t4=datetime.now()
					if choice=="1":
						word = extra + ''.join(xs)
					elif choice=="2":
						word = ''.join(xs) + extra 
					#os.system("clear")
					#print ("Creating string: %s" %(word))
					#print ("Progress: %d / %d" %(lines, data))
					lines=lines+1
					monitor = monitor + 1
					if monitor == interval:
						#tmon = datetime.now()
						#tall = tmon - t12
						
						inc = inc + 1
						disp = interval * inc
						perc = (disp * 100) / data
						per = data - disp
						#var = data / disp
						#tall = tall * var
						#tall = tall / disp
						print(str(disp) + '/' + str(data) + ' Lines generated | ' + str(perc) + '% Complete')
						monitor = 0
						#t12 = datetime.now()
					#t5=datetime.now()
					#try:
					#	t6=(t5-t4)*(data-lines)
					#	poo = 0
					#	for extra in wordList:
					#		poo = poo + 1
					#	t6 = t6 * poo
					#except OverflowError:
					#	t6=">999999999 days"
					#print("Estimated time remaining: %s" %(t6))
					if lines >= data+1:
						t2 = datetime.now()
						total =  t2 - t1
						os.system("clear")
						print("******************************************\nComplete\nGenerated %d possible passcodes\nDictionary file has been created/updated: %s \nTime taken: %s" %(data, file, total))
						#loop=False
						#break
						#sys.exit
					try:
						writeFile = open(file , 'a')
						writeFile.write( word + "\n")
						writeFile.close()
					except IOError:
						print "File will not open"
		else:
			for xs in itertools.product(chars, repeat=number):
				#t4=datetime.now()
				if choice=="1":
					word = extra + ''.join(xs)
				elif choice=="2":
					word = ''.join(xs) + extra 
				#os.system("clear")
				#print ("Creating string: %s" %(word))
				#print ("Progress: %d / %d" %(lines, data))
				lines=lines+1
				monitor = monitor + 1
				if monitor == interval:
					inc = inc + 1
					disp = interval * inc
					perc = (disp * 100) / data
					print(str(disp) + '/' + str(data) + ' Lines generated | ' + str(perc) + '% Complete')
					monitor = 0
				#t5=datetime.now()
				#try:
				#	t6=(t5-t4)*(data-lines)
				#except OverflowError:
				#	t6=">999999999 days"
				#print("Estimated time remaining: %s" %(t6))
				if lines >= data+1:
					t2 = datetime.now()
					total =  t2 - t1
					os.system("clear")
					print("******************************************\nComplete\nGenerated %d possible passcodes\nDictionary file has been created/updated: %s \nTime taken: %s" %(data, file, total))
					#loop=False
					#break
					#sys.exit
				try:
					writeFile = open(file , 'a')
					writeFile.write( word + "\n")
					writeFile.close()
				except IOError:
					print "File will not open"
	if lines != repeat:
		t2 = datetime.now()
		total =  t2 - t1
		os.system("clear")
		print("******************************************\nComplete\nGenerated %d possible passcodes\nDictionary file has been created/updated: %s \nTime taken: %s" %(data, file, total))
		loop=False
