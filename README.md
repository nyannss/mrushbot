# [The Avenger (mrush.net) Bot](https://github.com/nyannss/mrushbot)  &middot; [![GitHub license](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://github.com/nyannss/mrushbot/blob/main/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/nyannss/mrushbot/pulls)
Automation for mrush.net!
⭐ Star if you like this! ⭐

This content is provided for educational purposes only. It is not professional advice. The authors are not liable for any actions taken based on the information provided. Use at your own risk.

## Features
- Auto Battle (Lair and Arena)
- Auto clan lair
- Auto claim daily task reward
- Batch Account
- Use Proxy option

### Upcoming features
- Auto raid
- Auto claim story task reward

## Getting Started
To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Prequisites
Before you can set up a virtual environment, you'll need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Cloning the Repository
Run the following command to clone the repository:
```
git clone https://github.com/nyannss/mrushbot
```

### Instal Dependencies
Make sure to install all dependencies. To run the application, run the following command:
```
pip install -r requirements.txt
```

### Running the Application
Make sure to install all dependencies. To run the application, run the following command:
```
python main.py --username=YourUsername --password=YourPassword
```

### Running multi-account
Copy `accounts.csv.example` to `account.csv` and enter your username and password in there. Run this command:
```
python batch.py
```

### Running with proxy
Copy `proxies.csv.example` to `proxies.csv` and enter your username, password, host, and port in there. Run this command:
```
python main.py --username=YourUsername --password=YourPassword --proxy
```

OR if batch

```
python batch.py --proxy
```

## Contributing
Feel free to open issues for any suggestions, questions, or bug reports. Pull requests are also welcome for improvements or fixes.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.