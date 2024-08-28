Aruba Switches Backup Tool

Overview :
This Python script automates the creation of a structured backup directory system. It’s designed to organize and store backups for multiple buildings and floors, each categorized by date. The tool is particularly useful for network engineers and IT professionals who need a systematic way to manage and store configuration backups from multiple network devices.

Features :
Automated Folder Creation: The script creates a top-level backup directory named with the current date.
Hierarchical Structure: Inside the dated backup folder, subfolders are created for each building, and within those, additional subfolders for each floor.
Customizable: Easily adjust the building names, floor names, and base directory according to your specific environment.


Requirements:
Python 3.x
TFTP Server such as "solar winds TFTP server"
Compatible with Windows operating systems


Usage :

Clone the Repository: Download the script to your local machine.

Customize this code with your switch details
{"hostname": "switch ip ", "username": "switch username", "password": "switch password", "building": "building name", "floor": "DataCenter"},
 
then # Add more switches as needed

 #add your device ip after "tftp"
        shell.send(f'copy st tftp your ip {backup_filename}\n')


Run the Script: Execute the Python script to generate the backup folder structure:
open cmd 
navigate to the file path : cd path/to/your/project
Copy code : python aruba-switches-backup-tool.py
Find Your Backups: The script will generate a folder named Backup_<YYYYMMDD> inside your specified directory (e.g., D:\backups). Inside this folder, you will find subdirectories for each building and floor.


