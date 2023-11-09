from src.bot_main import runBot
import argparse


# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Login.")

# Add the desired arguments
parser.add_argument("--username", required=True, help="Username for authentication")
parser.add_argument("--password", required=True, help="Password for authentication")

# Parse the arguments
args = parser.parse_args()

# Access the values
username = args.username
password = args.password

runBot(username, password)