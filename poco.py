## IMPORTS 
from colorama import Fore
import time
from pystyle import Colorate, Colors, Center, Box
import pyautogui
import fade
import os
## 

## SIZE n TITLE
cmd = 'mode 49,31'
title = 'title Poco'
os.system(cmd)
os.system(title)
##

## ASCII LOGO
logo = """
        ██████╗  ██████╗  ██████╗ ██████╗ 
        ██╔══██╗██╔═══██╗██╔════╝██╔═══██╗
        ██████╔╝██║   ██║██║     ██║   ██║
        ██╔═══╝ ██║   ██║██║     ██║   ██║
        ██║     ╚██████╔╝╚██████╗╚██████╔╝
        ╚═╝      ╚═════╝  ╚═════╝ ╚═════╝"""

faded_text = fade.purplepink(logo)
print(faded_text)
print(Colorate.Vertical(Colors.white, Center.XCenter("────────────────────────────────────────")))
##

## MAIN FUNCTIONS
def main():
    def stats():
        print(Colorate.Vertical(Colors.white, Center.XCenter("       Made by " + Fore.MAGENTA + "levi " + Colors.white + "| discord: " + Fore.MAGENTA + "dsc.gg/discord" + Fore.RESET)))
        print("                                                  ")

    def spam():
        msg = input(Center.XCenter(Fore.WHITE + "Message: "))
        n = input(Center.XCenter(Fore.WHITE + "Times(x): "))

        count = 5
        while(count != 0):
            print(count)
            time.sleep(1)
            count -= 1

        for i in range(0,int(n)):
	        pyautogui.typewrite(msg + '\n')


    stats()
    spam()
     
## DOESNT KNOW WHAT IT DOES TBH
if __name__ == '__main__': 
    main()

## SO IT DOESNT STOP FROM CONSOLE (was a issue for me)
time.sleep(3600)