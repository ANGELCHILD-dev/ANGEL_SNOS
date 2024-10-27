import subprocess
import sys
import time
import os
import random

RESET = "\033[0m"
BOLD = "\033[1m"
BLACK_BG = "\033[48;5;55m"

required_modules = [
"webbrowser",
"telethon",
"requests",
"pyfiglet",
"fake_useragent",
"logging",
"lambda",
"telegram",
"pystyle",
"string",
"termcolor",
"asyncio",
"datetime",
"platform"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    for module in required_modules:
        try:
            __import__(module)
            print_with_delay(BOLD + f"{module}")
        except ImportError:
            print(f" {module}...")
            install(module)
            print_with_delay(BOLD + f" {module}" + RESET)


check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')
