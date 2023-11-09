import csv
import subprocess
from src.colors import Colors
import argparse


print(f"{Colors.OKBLUE}ℹ️ MRUSH.NET BOT, BY:NYANNSS\n")

parser = argparse.ArgumentParser()
parser.add_argument('--proxy', action='store_true', help='Use a proxy')
args = parser.parse_args()

# Jika argumen --proxy diberikan, gunakan proxy
use_proxy = args.proxy


# Read the CSV file
with open('accounts.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if present

    for row in reader:
        # remove whitespace
        username, password = [item.strip() for item in row]
        print(f'Executing main.py with username: {username}')

        arguments = ['py', 'main.py', f'--username={username}', f'--password={password}']
        
        # If use_proxy is True, add --proxy
        if use_proxy:
            arguments.append('--proxy')

        # Execute main.py with username and password as arguments
        subprocess.run(arguments)
