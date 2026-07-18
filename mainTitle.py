from colorGradient import gradient
from darwinGame import gameAttention
import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('')

if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)

if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Цвета

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
gray = "\033[90m"
blue = "\033[94m"
reset = "\033[0m"

# Титул

title = f'''
██████╗  █████╗ ██████╗ ██╗    ██╗██╗███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║██║████╗  ██║ 
██║  ██║███████║██████╔╝██║ █╗ ██║██║██╔██╗ ██║ 
██║  ██║██╔══██║██╔══██╗██║███╗██║██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝

1. New game (Darwin waiting you)

0. Exit
'''

nums = [0, 1]

while True:
    clear()
    gradient(title)
    
    select = input()

    # Проверка на число
    try:
        sel = int(select)

        if sel in nums:
            pass
        
        else:
            clear()
            continue

    except ValueError:
        clear()
        continue
    
    # Выход
    if sel == 0:
        clear()
        sys.exit()
    
    # Вызов игры через darwinGame
    if sel == 1:
        clear()
        gameAttention()
    

# Подсчет строчек кода всего (для себя)
# Get-ChildItem -Recurse -Filter *.py | ForEach-Object { [PSCustomObject]@{ Файл = $_.Name; Строк = (Get-Content $_.FullName | Measure-Object -Line).Lines } } | Format-Table -AutoSize