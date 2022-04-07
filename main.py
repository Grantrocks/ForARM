from colorama import init,Style,Fore,Back
import os
import animation
import json
init(autoreset=True)
logo=Fore.BLUE+"""
███████╗ ██████╗ ██████╗  █████╗ ██████╗ ███╗   ███╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║
█████╗  ██║   ██║██████╔╝███████║██████╔╝██╔████╔██║
██╔══╝  ██║   ██║██╔══██╗██╔══██║██╔══██╗██║╚██╔╝██║
██║     ╚██████╔╝██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
print(logo)
def games():
  try:
    installedf=open("armapps/installed.json","r+")
    istalledd=json.load(installedf)
    installed=istalledd['installed']
    print(Fore.GREEN+"""
          Avaiable games for install
          q: Back to Main
          1: Cracked Minecraft
          2: Minecraft
          """)
    choice=input(Fore.CYAN+"Choice: ")
    os.system('clear')
    if choice=="1":
      for i in installed:
        if i['app']=="Cracked Minecraft":
          print(Fore.RED+"Minecraft is alreay installed")
          installed=True
          pass
      if not installed:
        os.system("clear")
        print(Fore.GREEN+"Installing Cracked Minecraft")
        clock = ['-','\\','|','/']
        animation.wait(clock)
        os.system("chmod a+x /home/$USER/ForARM/armapps/CrackedMC/install.sh")
        os.system("cd /home/$USER/ForARM/armapps/CrackedMC")
        os.system("./install.sh")
        newdata={'app':"Cracked Minecraft"}
        installedf.truncate(0)
        installedf.close()
        installedf=open("armapps/installed.json","r+")
        istalledd['installed'].append(newdata)
        installedf.seek(0)
        json.dump(istalledd,installedf,indent=2)
    elif choice=="q":
      return
  except:
    print(Fore.RED+"Something went wrong!")
    installedf.close()
    exit()
  finally:
    installedf.close()
    return
def main():
  print(Fore.GREEN+"""
        Find amazing apps and install them in 1 click.
        i: Installed
        u: Remove
        1: Games
        2: Office
        """)
  choice=input(Fore.CYAN+"Choice: ")
  os.system('clear')
  if choice=="1":
    games()
  elif choice=="i":
    print(Fore.BLUE+"Installed Apps")
    f=open("armapps/installed.json")
    jdata=json.load(f)
    f.close()
    for i in jdata['installed']:
      print(i['app'])
  elif choice=="u":
    print(Fore.BLUE+"Installed Apps")
    f=open("armapps/installed.json")
    jdata=json.load(f)
    f.close()
    num=1
    for i in jdata['installed']:
      print(str(num)+": "+i['app'])
      num+=1
    choice=input(Fore.CYAN+"Which app to remove?(Enter app name exactly as you see it): ")
    if choice=="q":
      print(Fore.RED+"Cancelled")
      return
    for i in jdata['installed']:
      if i['app']==choice:
        f=open('armapps/installed.json','r+')
        dataf=json.load(f)
        f.truncate(0)
        f.close()
        f=open('armapps/installed.json','r+')
        dataf['installed'].remove(i)
        json.dump(dataf,f,indent=1)
        f.close()
        print(Fore.GREEN+f"Removed {choice}")
        if choice=="Cracked Minecraft":
          os.system("chmod /home/$USER/ForARM/armapps/CrackedMC/uninstall.sh")
          os.system("cd /home/$USER/ForARM/armapps/CrackedMC")
          os.system("./uninstall.sh")
while True:
  main()