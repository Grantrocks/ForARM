from colorama import init,Style,Fore,Back
import os
import animation
import json
init(autoreset=True)
logo="""
███████╗ ██████╗ ██████╗  █████╗ ██████╗ ███╗   ███╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║
█████╗  ██║   ██║██████╔╝███████║██████╔╝██╔████╔██║
██╔══╝  ██║   ██║██╔══██╗██╔══██║██╔══██╗██║╚██╔╝██║
██║     ╚██████╔╝██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
print(logo)
def games():
  print("""
        Avaiable games for install
        1: Cracked Minecraft
        """)
  choice=input("Choice: ")
  if choice=="1":
    os.system("clear")
    print("Installing Cracked Minecraft")
    os.system("chmod a+x /home/$USER/ForARM/armapps/CrackedMC/install.sh")
    os.system("cd /home/$USER/ForARM/armapps/CrackedMC")
    os.system("./install.sh")
def main():
  print("""
        Find amazing apps and install them in 1 click.
        1: Games
        2: Office
        """)
  choice=input("Choice: ")
  if choice=="1":
    os.system('clear')
    games()
while True:
  main()