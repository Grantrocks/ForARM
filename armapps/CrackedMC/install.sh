cd /home/$USER/
if [ ! -z "$(file "$(readlink -f "/sbin/init")" | grep 64)" ];then
  MACHINE='aarch64'
elif [ ! -z "$(file "$(readlink -f "/sbin/init")" | grep 32)" ];then
  MACHINE='armv7l'
else
  echo "Failed to detect OS CPU architecture! Something is very wrong."
fi
mkdir Cracked-Minecraft
cd Cracked-Minecraft
if [ "$MACHINE" = "aarch64" ]; then
    if [ ! -d ~/lwjgl3arm64 ]; then
        mkdir ~/lwjgl3arm64
    fi
else
    if [ ! -d ~/lwjgl3arm32 ]; then
        mkdir ~/lwjgl3arm32
    fi
    if [ ! -d ~/lwjgl2arm32 ]; then
        mkdir ~/lwjgl2arm32
    fi
fi
if [ "$MACHINE" = "aarch64" ]; then
    if [ ! -f jdk-8u251-linux-arm64-vfp-hflt.tar.gz ]; then
        wget https://github.com/mikehooper/Minecraft/raw/main/jdk-8u251-linux-arm64-vfp-hflt.tar.gz
    fi
else
    if [ ! -f jdk-8u251-linux-arm32-vfp-hflt.tar.gz ]; then
        wget https://github.com/mikehooper/Minecraft/raw/main/jdk-8u251-linux-arm32-vfp-hflt.tar.gz
    fi
fi
if [ "$MACHINE" = "aarch64" ]; then
    if [ ! -f lwjgl3arm64.tar.gz ]; then
        wget https://github.com/mikehooper/Minecraft/raw/main/lwjgl3arm64.tar.gz
    fi
else
    if [ ! -f lwjgl3arm32.tar.gz ]; then
        wget https://github.com/mikehooper/Minecraft/raw/main/lwjgl3arm32.tar.gz
    fi
    if [ ! -f lwjgl2arm32.tar.gz ]; then
        wget https://github.com/mikehooper/Minecraft/raw/main/lwjgl2arm32.tar.gz
    fi
fi
if [ "$MACHINE" = "aarch64" ]; then
    sudo tar -zxf jdk-8u251-linux-arm64-vfp-hflt.tar.gz -C /opt/jdk
    # install opnjdk for launcher.jar and optifine install
    sudo apt install openjdk-11-jdk -y
else
    sudo tar -zxf jdk-8u251-linux-arm32-vfp-hflt.tar.gz -C /opt/jdk
fi
if [ "$MACHINE" = "aarch64" ]; then
    tar -zxf lwjgl3arm64.tar.gz -C ~/lwjgl3arm64
else
    tar -zxf lwjgl3arm32.tar.gz -C ~/lwjgl3arm32
    tar -zxf lwjgl2arm32.tar.gz -C ~/lwjgl2arm32
fi
sudo update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_251/bin/java 0
sudo update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_251/bin/javac 0
if [ "$MACHINE" = "aarch64" ]; then
    sudo update-alternatives --set java /usr/lib/jvm/java-11-openjdk-arm64/bin/java
    sudo update-alternatives --set javac /usr/lib/jvm/java-11-openjdk-arm64/bin/javac
else
    sudo update-alternatives --set java /opt/jdk/jdk1.8.0_251/bin/java
    sudo update-alternatives --set javac /opt/jdk/jdk1.8.0_251/bin/javac
fi
cd /home/$USER/Cracked-Minecraft/
echo "[Desktop Entry]
Name=Cracked Minecraft
Comment=Cracked version of minecraft
Exec=java -jar /home/$USER/Cracked-Minecraft/crackedlauncher.jar
Icon=/home/$USER/Cracked-Minecraft/minecraft-logo-1022.png
Terminal=false
Type=Application
Categories=Games;
StartupNotify=true" > ~/.local/share/applications/cracked-minecraft.desktop
wget https://onedrive.live.com/download?cid=7BEF2F746D350F5E&resid=7BEF2F746D350F5E%214529&authkey=ANu-NbknMtQ76UM
wget https://www.freepnglogos.com/download/1022
mv /home/$USER/ForARM/armapps/CrackedMC/instructions.txt /home/$USER/Cracked-Minecraft/instructions.txt