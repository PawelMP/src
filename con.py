import os

###system("sudo ifconfig eth0 192.168.1.120 netmask 255.255.255.0")
##.system("sudo route add default gw 192.168.1.1 eth0")
#s.system("source devel/setup.bash")
#s.system("roslaunch vc200_controller vc200_controller.launch")
#os.system("sudo /etc/init.d/networking restart")
os.system("sudo ifconfig eth0 192.168.1.120 netmask 255.255.255.0")#bylo 192.68.1.120
os.system("sudo chmod 666 /dev/ttyUSB0")
#os.system("sudo ifconfig wlan0 192.168.1.44 netmask 255.255.255.0")
#os.system("sudo route add default gw 192.168.1.1 eth0")
##os.system("source devel/setup.bash")nmcli
