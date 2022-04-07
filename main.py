from colorama import init,Style,Fore,Back
import os
import animation
import json
init(autoreset=True)
logo="""

           1µ 1µ 1H 1▒ 1ß [ß [ß ]ß ]ß
       ▄▄▄▄▓▓▄▓▓▄▓▓▄▓▓▄▓▓▄▓▓▄▓▓▄▓▓▄▓▓▄▄▄▄
       ██████████████████████████████████⌐
    ╔µµ████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒µµ
    ,,,████▒▒▒å▄▄▄▄▄▄▄▄▄▄▄▄ñ▒▒▒▒▒▒▒▒▒████µ,,
    ```████▒▒▒║▒▒▒▒▒▒▒▒▒▒▒▒H▒▒▒▒▒▒▒▒▒████```
    ╚¼▒████▒▒▒åååååååååååååH▒▒▒▒▒▒▒▒▒████▒¼¼
    ╔╔╔████▒▒@@@@@@@@@@@@@@@@@@@@@@▒▒████w╔╔
       ████▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╣▒▒████⌐
    ººº████▒▒▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▒▒████Mºº
    1▒▒████▒▒▒Ñ▓@@▓╫@Ñ▓@@▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒
    ╓╓╓████▒▒▒▒▌║║@▒║▒▌╫║▒▒▒▒▒▒▒▒▒▒▒▒████╥╓╓
    ```████▒▒▒@@@@@▒@@@@@▒▒▒▒▒▒▒▒▒▒▒▒████⌐``
    ╙╜╜████▒▓@▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒████▒╜╜
    ╔µµ████▒╖╓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄╓▒████Wµµ
       ██████████████████████████████████⌐
       ██████████████████████████████████
           ║µ ╠▒ ╠▒ ╠▒ ╚▒ 1▒ 1▒ ]▒ ]▒


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
    os.system("chmod a+x /home/$USER/ForARM/armapps/CrackedMC/install")
    os.system("./home/$USER/ForARM/armapps/CrackedMC/install")
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