from colorGradient import gradient
import time
import os
import sys
from everyoneStats import DarwinStats

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
gray = "\033[90m"
blue = "\033[94m"
reset = "\033[0m"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gameAttention():
    clear()

    print('''
    Дарвин был великим героем, чьё имя гремело повсюду. 
    
    В один прекрасный день он бросил вызов тьме, 
    решив раз и навсегда избавить мир от зла.
    ''', flush=True)
    
    time.sleep(2)
    clear()

    