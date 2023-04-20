import paramiko

# Define the host information
host = 'example.com'
username = 'myusername'
password = 'mypassword'
port = 22

# Define the path to the binary and any arguments
binary_path = r'C:\path\to\my\binary.exe'
args = '--option1 value1 --option2 value2'

# Define the PowerShell script to upload the binary and execute it as a background task
powershell_script = r'''
$source = '{}'
$destination = '{}'
Copy-Item $source $destination
$command = "C:\PsTools\PsExec.exe -d -s $destination {}"
Invoke-Expression $command
'''.format(binary_path, binary_path.split('\\')[-1], args)

# Establish an SSH connection to the remote host
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, port=port)

# Transfer the PowerShell script to the remote host
sftp = client.open_sftp()
with sftp.open('upload.ps1', 'w') as f:
    f.write(powershell_script)
sftp.close()

# Execute the PowerShell script on the remote host
stdin, stdout, stderr = client.exec_command('powershell.exe -File upload.ps1')

# Monitor the progress of the background task
# ...

# Close the SSH connection
client.close()
