from getpass import getpass
import netmiko
import re
import logging
import os
import datetime

#Logging File Information
logging.basicConfig(filename="log/logs.txt", level=logging.WARNING)

#Functions for Connecting
def make_connection (ip, username, password):
		return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)

#Regex to only read IP Addresses
def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

#Create List of IPs
def get_ips (file_name):
	for line in open(file_name, 'r').readlines():
		line = get_ip(line)
		for ip in line:
			ips.append(ip)

# Create a list for your commands, request input for commands to use
commands_list = []
comm_dir = os.listdir("commands/")
print(comm_dir)

commands_file = input("Please enter the name of the commands file to execute: ")
commands_file = "commands/" + commands_file

# Get the commands from the specified commands.txt and append to our list
with open(commands_file, 'r') as f:
	for line in f:
		commands_list.append(line)


def to_doc_a(file_name, varable):
	f=open(file_name, 'a')
	f.write(varable)
	f.write('\n')
	f.close()


def to_doc_w(file_name, varable):
	f=open(file_name, 'w')
	f.write(varable)
	f.close()

#This will be a list of the devices we want to SSH to
ips = []
host_dir = os.listdir("hosts/")
print(host_dir)
hosts_file = input("Please enter the name of the commands file to execute: ")
hosts_file = "hosts/" + hosts_file
#Pull the IPs.txt is a list of the IPs we want to connect to
#This function pulls those IPs out of the txt file and puts them into a list
get_ips(hosts_file)
print('#' * 50)
print('#' * 50, '\n HOSTS', ips, '\n', "COMMAND LIST", '\n')
for commands in commands_list:
	print(commands)
print("IF INCORRECT QUIT NOW CTRL^C ", '\n', '#' * 50)
print('#' * 50)

#Prompt user for account info
username = input("Username: ")
password = getpass()

#Specify Log File
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_')
file_name = "log/" + time_now + "Results.txt"


#Make a for loop to hit all the devices, for this we will be looking at the IOS it's running
for ip in ips:
	#Connect to a device
	try:
		net_connect = make_connection(ip, username, password)
		print("Connecting to " + ip)
		#Run all our commands and append to our file_name
		output = net_connect.send_config_set(commands_list)
		output2 = net_connect.save_config()
		results = ip + '\n' + output + '\n'+ output2
		logging.warning(time_now + "Completed " + ip )
		to_doc_w(file_name, results)
		print("Completed " + ip)
	except:
		print("Changes failed or unable to connect to " + ip )
		logging.error(time_now + ip + " Failed to connect")
