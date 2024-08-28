import paramiko
import time
import os
from datetime import datetime

# List of switches with connection details
switches = [

# First Building Switches : 

    {"hostname": "switch ip ", "username": "switch username", "password": "switch password", "building": "building name", "floor": "DataCenter"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Basement"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Ground"},
   
  
# Second Building Switches : 

    {"hostname": "switch ip ", "username": "switch username", "password": "switch password", "building": "building name", "floor": "DataCenter"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Basement"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Ground"},
  
# Third Building Switches : 

    {"hostname": "switch ip ", "username": "switch username", "password": "switch password", "building": "building name", "floor": "DataCenter"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Basement"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Ground"},
 
# Fourth Building Switches : 

    {"hostname": "switch ip ", "username": "switch username", "password": "switch password", "building": "building name", "floor": "DataCenter"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Basement"},
    {"hostname": "switch ip", "username": "switch username", "password": "switch password", "building": "building name", "floor": "Ground"},
   
    # Add more switches as needed
]

def connect_and_backup(switch):
    hostname = switch["hostname"]
    username = switch["username"]
    password = switch["password"]
    building = switch["building"]
    floor = switch ["floor"]
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the switch
        ssh.connect(hostname, username=username, password=password)
        print(f"Successfully connected to {hostname}")

        # Open an interactive shell
        shell = ssh.invoke_shell()
        time.sleep(1)

        # Elevate the user's privilege to level 15
        shell.send('configure terminal\n')
        time.sleep(1)
        shell.send(f'username {username} privilege 15 password {password}\n')
        time.sleep(2)  # Wait for the command to process

        # Confirm the privilege elevation
        shell.send('end\n')
        time.sleep(1)
        shell.send(f'show running-config | include username {username}\n')
        time.sleep(2)

        # Read the output and print it
        output = shell.recv(10000).decode()
        print(output)

        # Generate timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        # Perform the backup command with a unique filename
        backup_filename = (f'backup_{building}_{floor}_'
                           f'{hostname.replace(".", "_")}_'
                           f'{timestamp}.cfg')
        #backup_filename = f'backup_{hostname.replace(".", "_")}.cfg' #egnore this line 

        #add your device ip after "tftp"
        shell.send(f'copy st tftp .... {backup_filename}\n')
        time.sleep(5)
        output = shell.recv(10000).decode()
        print(output)

    except Exception as e:
        print(f"Failed to connect to {hostname}. Error: {e}")

    finally:
        ssh.close()
        print(f"Connection to {hostname} closed.")

def main():
    for switch in switches:
        connect_and_backup(switch)

if __name__ == "__main__":
    main()
