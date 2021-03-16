# Py-tvt
Python Cisco IOS Changes Script


## Installation

Requires the following libraries
getpass
netmiko
re
logging
os
datetime

Use the package manager pip to install
```bash
pip install getpass
pip install netmiko
pip install re

```

## Usage

```python
The Hosts you wish to make changes to, need to be store in a text file under the /hosts folder.
Create a file, eg routers.txt,  have a host on each line with their IP address, you can add hostsnames but they will be ignored.

The Commands you wish to exectute need to be store in a text file under the /commands folder.
Create a file, eg hostname.txt, with a Cisco Cli compatible line on each line of the file. 

NOTE: You do not require a conf t at the beginning or an end/exit statement at the end, the script will put itself into config mode automatically and it exit to write the configuration

To execute: python3 changes.py

You will be asked for the file name of your commands file, eg hostname.txt
You will be asked for the file name of your hosts file, eg routers.txt

You will be shown the list of commands this script is going to execute, if there is an issue, exit the script using Ctrl c

You will be prompted for your username and password

The script will run through each host and run each of the commands on each host, saving the output to the log folder. There is an individual log file for each time the script is run, plus a global log file that is always appended to.

If a host fails to connect, you will be be given an error for that host and the script will continue


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
Copyright (c) [2020] [Doran McGregor]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
