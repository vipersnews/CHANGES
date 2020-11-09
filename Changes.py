from getpass import getpass
import netmiko
import re
import difflib

def make_connection (ip, username, password):
		return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)

def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

def get_ips (file_name):
	for line in open(file_name, 'r').readlines():
		line = get_ip(line)
		for ip in line:
			ips.append(ip)
# This will be the list of commands we will use
commands_list = []

commands_file = input("Please enter the name of the commands file to execute: ")

# Get the commands from commands.txt and append to our list
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

#Pull the IPs.txt is a list of the IPs we want to connect to
#This function pulls those IPs out of the txt file and puts them into a list
get_ips("IPs.txt")
print('#' * 50)
print('#' * 50, '\n HOSTS', ips, '\n', "COMMAND LIST", '\n')
for commands in commands_list:
	print(commands)
print("IF INCORRECT QUIT NOW CTRL^C ", '\n', '#' * 50)
print('#' * 50)

#Prompt user for account info
username = input("Username: ")
password = getpass()



#Make a for loop to hit all the devices, for this we will be looking at the IOS it's running
for ip in ips:
	#Connect to a device
	net_connect = make_connection(ip, username, password)
	#Run all our commands and append to our file_name
	output = net_connect.send_config_set(commands_list)
	output2 = net_connect.save_config()
	results = output + '\n'+ output2
	print(results)
