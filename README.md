
# Network Configuration Backup Script

This script allows you to automate the process of backing up the configuration of multiple network devices, such as routers and switches.

## Requirements

-   Python 3 installed on your computer
-   Paramiko library installed (run `pip install paramiko` to install it)
-   Access to the network devices you want to back up, including their hostname, username, and password

## How the script works

The script connects to each network device in a list using the Secure Shell (SSH) protocol, retrieves its current configuration by running the appropriate command (such as `show running-config`), and saves the configuration to a local file. The filename of each backup file includes the hostname of the device and the current date and time.

## How to use the script

1.  Open a text editor and copy the code from the code section of this documentation into a new file. Save the file with a `.py` extension, for example `network_backup.py`.
2.  Open the terminal or command prompt on your computer.
3.  Navigate to the directory where you saved the script file.
4.  Edit the list of network devices in the code to include the hostnames, usernames, and passwords of the devices you want to back up.
5.  Run the script by typing `python network_backup.py` in the terminal or command prompt and pressing enter.
6.  The script will connect to each network device, retrieve its configuration, and save it to a local file.
7.  After the script has run, you will find the backup files in the same directory where you saved the script file.

## Code
```python
import paramiko
import datetime

# List of network devices to be backed up
devices = [
    {'hostname': 'device1.example.com', 'username': 'admin', 'password': 'secret1'},
    {'hostname': 'device2.example.com', 'username': 'admin', 'password': 'secret2'},
    {'hostname': 'device3.example.com', 'username': 'admin', 'password': 'secret3'}
]

# Connect to each network device and retrieve its configuration
for device in devices:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device['hostname'], username=device['username'], password=device['password'])
    stdin, stdout, stderr = ssh.exec_command('show running-config')
    config = stdout.read().decode()

    # Generate a filename for the backup file with the current date and time
    filename = f"{device['hostname']}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.cfg"

    # Write the configuration to a local file
    with open(filename, 'w') as f:
        f.write(config)

    # Close the SSH connection
    ssh.close()

# Print a message indicating that the backup process is complete
print("Network device configuration backup complete.")
```
