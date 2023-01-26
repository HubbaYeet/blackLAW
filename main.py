'''

██████  ██       █████   ██████ ██   ██ ██       █████  ██     ██ 
██   ██ ██      ██   ██ ██      ██  ██  ██      ██   ██ ██     ██ 
██████  ██      ███████ ██      █████   ██      ███████ ██  █  ██ 
██   ██ ██      ██   ██ ██      ██  ██  ██      ██   ██ ██ ███ ██ 
██████  ███████ ██   ██  ██████ ██   ██ ███████ ██   ██  ███ ███  
automated pentesting toolkit
                                                                  
'''

'''
___  _______ _______ 
\  \/ /\__  \\_  __ \
 \   /  / __ \|  | \/
  \_/  (____  /__|   
            \/      
'''
# import
import sys # <- gets sys info for os
import os # <- for terminal commands
import random # <- for random ascii
# from termcolor import colored, cprint # <- for colored text
# from getpass import getpass # <- for secret password

# color caller
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# funny error messages
error_message = ["Nope, that's a trap door to nowhere.","Sorry, but that's a unicorn in a field of horses.","I'm afraid that's a red herring.","That's a dead end, my friend.","I'm sorry, but that's a ghost town.","I'm afraid that's a wild goose chase.","That's a non-starter, I'm afraid.","I'm sorry, but that's a pipe dream.","That's a road to nowhere, my dear.","I'm afraid that's a fool's errand.","That's a long shot, if you ask me.","I'm afraid that's a recipe for disaster.","That's a bridge too far.","I'm sorry, but that's a train wreck waiting to happen.","That's a lost cause, if you ask me.","I'm afraid that's a hard pass.","That's a no-go, my friend.","I'm sorry, but that's a dead end street.","That's a false alarm.","That's a syntax error.","That's a bug, not a feature.","I'm sorry, but that's a 404 error.","Hard drive crash :/","Computer virus?","Blocked by a firewall.","There's a memory leak!","software glitch? pfft...","I'm afraid that's a keyboard shortcut to nowhere.","[insert blue screen of death here]"]

def ran_err_msg():
  random_error_message = random.choice(error_message)
  return random_error_message

# blacklaw ascii
class ascii:
  bunny = ' ()_()\n (._.)\no((")(")'
  bear = '───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n───█▒▒░░░░░░░░░▒▒█───\n────█░░█░░░░░█░░█────\n─▄▄──█░░░▀█▀░░░█──▄▄─\n█░░█─▀▄░░░░░░░▄▀─█░░█'
  cat = '──────▄▀▄─────▄▀▄\n─────▄█░░▀▀▀▀▀░░█▄\n─▄▄──█░░░░░░░░░░░█──▄▄\n█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█'
  zombie = '▒▒▒▒▒▒▐███████▌\n▒▒▒▒▒▒▐░▀░▀░▀░▌\n▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌\n▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄\n▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐'
  alien = '▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒'
  biker = '───────▄██████▄───────\n──────▐▀▀▀▀▀▀▀▀▌──────\n──────▌▌▀▀▌▐▀▀▐▐──────\n──────▐──▄▄▄▄──▌──────\n───────▌▐▌──▐▌▐───────'
  hacker = '─────█─▄▀█──█▀▄─█─────\n────▐▌──────────▐▌────\n────█▌▀▄──▄▄──▄▀▐█────\n───▐██──▀▀──▀▀──██▌───\n──▄████▄──▐▌──▄████▄──'
  scream = '───▄█▌─▄─▄─▐█▄\n───██▌▀▀▄▀▀▐██\n───██▌─▄▄▄─▐██\n───▀██▌▐█▌▐██▀\n▄██████─▀─██████▄'
  skull = '──▄────▄▄▄▄▄▄▄────▄───\n─▀▀▄─▄█████████▄─▄▀▀──\n─────██─▀███▀─██──────\n───▄─▀████▀████▀─▄────\n─▀█────██▀█▀██────█▀──'
  luck = '█▄████─█▄████─█▄████\n▀▀─▄█▀─▀▀─▄█▀─▀▀─▄█▀\n──▄██────▄██────▄██\n─▄██▀───▄██▀───▄██▀\n─███────███────███'
  smile = '╔══╗░░░░╔╦╗░░╔═════╗\n║╚═╬════╬╣╠═╗║░▀░▀░║\n╠═╗║╔╗╔╗║║║╩╣║╚═══╝║\n╚══╩╝╚╝╚╩╩╩═╝╚═════╝'
  eyes = '█▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█\n█▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█\n█▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█'
  bull = '▄█▀─▄▄▄▄▄▄▄─▀█▄\n▀█████████████▀\n────█▄███▄█\n─────█████\n─────█▀█▀█'
  failwhale = '▄██████████████▄▐█▄▄▄▄█▌\n██████▌▄▌▄▐▐▌███▌▀▀██▀▀\n████▄█▌▄▌▄▐▐▌▀███▄▄█▌\n▄▄▄▄▄██████████████▀'
  needle = '────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀'
  computer = '▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░\n▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░\n▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░\n▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░\n░░░░▄▄███▄▄░░░░░█████░'
  evolution = '───────────────▄▄───▐█\n───▄▄▄───▄██▄──█▀───█─▄\n─▄██▀█▌─██▄▄──▐█▀▄─▐█▀\n▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌\n▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄'

asciilist = [ascii.bear, ascii.cat, ascii.zombie, ascii.alien, ascii.biker, ascii.hacker, ascii.scream, ascii.skull, ascii.luck, ascii.smile, ascii.eyes, ascii.bull, ascii.failwhale, ascii.needle, ascii.computer, ascii.evolution]
def randomascii():
  randomascii = random.choice(asciilist)
  return randomascii
# menu
def _menu_():
    # change directory to home
    os.path.expanduser('~')
    # print pentest text & list of commands
    print(color.BOLD+color.UNDERLINE+'blackLAW - Python Penetration Testing Toolkit'+color.END)
    print('\n'+randomascii())
    print("1. Help ~ for a list of commands")
    print("2. Documentation ~ for a list of helpful documents")
    print("3. Install ~ to begin installing tools")
    print("4. Deploy ~ to enter an installed tool")
    print("5. Exit ~ quit the program")

    # user choice
    choice = input("$> ")

    # help
    if choice == '1':
      _menu_()
    
    # docs
    elif choice == '2':
      _menu_()

    # install  
    elif choice == '3':
      print('\ninstall',color.BOLD+'OPTIONS:\n'+color.END+'#'*40+'\nI. scapy\nII. sherlock')
      to_install = input('#> ')
      if to_install == '1':
        # check for scapy
        if os.path.isdir("scapy"):
                # scapy folder already exists
                print('\n'+color.YELLOW+"scapy already installed, skipping download."+color.END)
                _menu_()
        else:
            # scapy folder does not exist then install scapy
            os.system("git clone https://github.com/secdev/scapy")
            os.chdir("scapy")
            os.system('pip install .')
            os.system('clear')
            # success
            print(color.GREEN+'scapy successfully installed.'+color.END)
            _menu_()
      elif to_install == '2':
        # check for sherlock
        if os.path.isdir("sherlock"):
          # sherlock folder already exists
          print('\n'+color.YELLOW+"sherlock already installed, skipping download."+color.END)
          _menu_()
        else:
          # sherlock folder does not exist then install sherlock
          os.system('git clone https://github.com/sherlock-project/sherlock.git')
          os.chdir('sherlock')
          os.system('python3 -m pip install -r requirements.txt')
          # success
          print(color.GREEN+'sherlock successfully installed.'+color.END)
          _menu_()
    # deploy / use
    elif choice == '4':
      print('\ndeploy',color.BOLD+'OPTIONS:\n'+color.END+'#'*40+'\nI. scapy\nII. sherlock')
      choice = input('%>')
      if choice == '1':
        if os.path.isdir("scapy"):
                os.chdir('scapy')
                os.system('scapy')
                _menu_()
        else:
          os.system('clear')
          print(color.RED+"\nscapy is not installed; Please install via the Install tab in the menu. [3]"+color.END+'\n')
          _menu_()
      elif choice =='2':
        if os.path.isdir("sherlock"):
          user = input('username: ')
          to_find = f'python3 sherlock --print-all --timeout 1 {user}'
          _menu_()
        else:
          print(color.RED+"\nsherlock is not installed; Please install via the Install tab in the menu. [3]"+color.END+'\n')
          _menu_()
     # exit 
    elif choice == '5':
      os.system('clear')
      print('goodbye.\n')
      exit()
    else:
      print('\n'+ran_err_msg()+'\n')
      _menu_()


'''
_____________  ____   ________________    _____  
\____ \_  __ \/  _ \ / ___\_  __ \__  \  /     \ 
|  |_> >  | \(  <_> ) /_/  >  | \// __ \|  Y Y  \
|   __/|__|   \____/\___  /|__|  (____  /__|_|  /
|__|               /_____/            \/      \/ 

'''
# program start
os.system('clear')
_menu_()

'''
               __                 
  ____   _____/  |_  ____   ______
 /    \ /  _ \   __\/ __ \ /  ___/
|   |  (  <_> )  | \  ___/ \___ \ 
|___|  /\____/|__|  \___  >____  >
     \/                 \/     \/ 
'''
# v.0.6.0
# major.minor.patch

# to-do:
'''
add autofill options
'''

# rip blackLAW bunny 
'''
 ()_()
 (._.)
o((")(")

'''

# skull ascii cuz fun
'''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`     ZEUS
'''