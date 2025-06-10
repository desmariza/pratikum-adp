import os
import time
from termcolor import colored

os.system('cls')  

print(colored(r"""
  _______ _  _     _______  ___  _     
 |__   __(_)| |   |__   __||   || |    
    | |   _ | | __   | |   |   || | __
    | |  | || |/ /   | |   |   || |/ /
    | |  | ||   <    | |   |   || | < 
    |_|  |_||_|\_\   |_|   |___||_|\_\
    """, 'cyan'))
print(colored("="*40, 'blue'))
print(colored("  PREMIUM LEVEL UP! v2.0", 'yellow', attrs=['bold']))
print(colored("="*40, 'blue'))

for i in range(1,101):
    time.sleep(0.03)
    print(colored(f"\rLoading [{'||'*(i//5):<20s}] {i}%", 
        ['red','yellow','green'][(i>=50)+(i>=80)]), end='')   

print("\n" + colored("Aplikasi siap digunakan!", 'green', attrs=['bold']))
time.sleep(1)
os.system('cls')
print(colored("Menu Utama:", 'cyan', attrs=['bold']))
print(colored("- Pembuatan konten video pendek", 'light_red'))
print(colored("- live streaming", 'light_magenta'))
print(colored("- Algoritma rekomendasi cerdas", 'light_blue'))