import os
import time

os.system("clear")

def nonhackingos():
  print("[1]: Ubuntu, Debain, linux mint(Distros like that)")
  print("[2]: Arch")
  oschoice = input("WHAT OS? ")
  if oschoice == ("1"):
    print("still being made Sorry!")
    exit(0)
  if oschoice == ("2"):
    print("Still being made Sorry!")
    exit(0)

def hackingos():
  os.system("clear")
  os.system("sudo apt-get install git")
  print("You Are Ready To Use R-BOX!")
  time.sleep(1)
  os.system("python menu.py")


print('''
        ---_ ...... _/_ -    
       /  .      ./ .'*\ \    
       : '         /__-'   \. 
      /                      )
    _/                  >   .' 
  /   '   .       _.-" /  .'   
  \           __/"     /.'    
    \ '--  .-" /     //'      
     \|  \ | /     //    
          \:     //
       `\/     // MADE BY KAMIL 
        \__`\/ /       URBANSKI
           \_|''')

print("[*]    WELCOME TO R-BOX INSTALLER     [*]")
print("[*]  YOU ARE SO CLOSE TO GET R-BOX    [*]")
print("[*]  R-BOX IS ONLY AVAIABLE FOR LINUX [*]")
print("[*]  R-BOX IS MIGHT BE AVAIABLE FOR   [*]")
print("[*]          WINDOWS SOON!!           [*]")
print("[*] If you have this now you must be  [*]")
print("[*]  a Tester or you have found an    [*]")
print("[*]       Old Version Of R-BOX        [*]")
print("\n")
print("Examples: Kali Linux, Parrot Os and Cyborg?")
choice = input("Are You Using a Hacking Os?\nY/N?")
if choice == ("Y"):
  hackingos()
if choice == ("y"):
  hackingos()

if choice == ("n"):
  nonhackingos()

if choice == ("N"):
  nonhackingos()

