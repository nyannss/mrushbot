import csv
import subprocess
from src.colors import Colors
from src.bot_main import runBot


print(f"{Colors.OKBLUE}ℹ️ MRUSH.NET BOT, BY:NYANNSS\n")



# Read the CSV file
with open('accounts.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if present

    for row in reader:
        # remove whitespace
        username, password = [item.strip() for item in row]
        print(f'Executing main.py with username: {username}, password: {password}')


        # Execute main.py with username and password as arguments
        subprocess.run(['py', 'main.py', f'--username={username}', f'--password={password}'])
