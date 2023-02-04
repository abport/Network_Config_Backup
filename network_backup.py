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
