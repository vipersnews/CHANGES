# Py-tvt
Python Config Command Sender


## Installation

Requires the following libraries
getpass
netmiko
re
difflib

Use the package manager pip to install 
```bash
pip install getpass
pip install netmiko
pip install difflib
pip install re
```

## Usage

```python
Edit the IPs.txt file to have a host on each line with just their IP
Edit the change_commands.txt file with your CLI command on each line

To execute: python3 Changes.py

You will be shown the list of commands this script is going to execute, if there is an issue, exit the script.

You will be prompted for your username and password

The script will run through each host and run each of the commands on each host.

Upon completion it will write the config to start-up and print the status.

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
