#  Daily-Horoscope
## About
A simple program that takes the inputs of a user to output their daily horoscope. Using basic python functions such as IF statements, boolean logic. As well as, integrating the 'BeautifulSoup', 'datetime' and 'requests' libraries to allow the program to scrape the horoscope from a url.

## Prerequisites
To use this program effectively make sure you have installed:
* Python 3.12.2
* bash or zsh
* pip
* BeautifulSoup library
* requests library

## Installing WSL (Windows Subsystem for Linux)

1. Open PowerShell as administrator.

2. Copy and paste the code below and hit enter.
```
wsl --install
```
3. Wait for the downloads to be complete, then restart your computer.

4. After restarting your computer, you should see an "Ubuntu" Window open automatically once you log back in. If you don't, search for the "Ubuntu" or "WSL" program in the start menu and launch it.

5. The window will prompt you to enter a username and password. Make sure you remember these! These are the credentials for your Linux user.

## Installing python 3.12.2
If you're on Linux, there are some dependencies you'll need before installing pyenv. Run these commands to install them:

1. Only run these if you're using a Linux System.
```
sudo apt update
sudo apt install -y build-essential zlib1g-dev libssl-dev
sudo apt install -y libreadline-dev libbz2-dev libsqlite3-dev libffi-dev
```
2. Run this to install pyenv with webi.
```
curl -sS https://webi.sh/pyenv | sh
```
3. Open your ~/.bashrc file in VS Code. You can do so by typing:
```
code ~/.bashrc
```
If you're using a Mac.
```
code ~/.zshrc
```
4. Add these lines to the bottom of the file in this order:
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

5. Finally close and reopen your terminal.

## Installing pip
1. First you have to update the repository package. Run the following command for it.
```
sudo apt update
```
2. Simply run the command.
```
sudo apt install python3-pip
```
## Installing beautifulsoup4
1. All you need to do is run the command below and wait for completion.
```
sudo pip3 install beautifulsoup4
```
or
```
sudo apt-get install python3-bs4
```
## Installing requests
1. All you need to do is run the command below and wait for completion.
```
sudo pip3 install requests
```


## Usage
To use this simple tool simply follow the instructions below:

1. Change into the repository directory in your shell.

2. Run the program by typing **python main.py** and hitting enter, if an error occurs run **python3 main.py** instead.

3. Follow the prompts on screen to recieve your daily horoscope.

4. If you are getting an error, try entering one of the following prompts:
* Scorpio
* Aries
* Cancer
* Capricorn
* Gemini
* Libra
* Taurus
* Virgo
* Aquarius
* Pisces
* Leo
* Sagittarius
