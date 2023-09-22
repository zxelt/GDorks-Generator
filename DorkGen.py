# Imports
import os, time, colorama
from colorama import Fore


# VARIABLES
banner = Fore.YELLOW + """
██████╗░░█████╗░██████╗░██╗░░██╗░██████╗░███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝░██╔════╝████╗░██║
██║░░██║██║░░██║██████╔╝█████═╝░██║░░██╗░█████╗░░██╔██╗██║
██║░░██║██║░░██║██╔══██╗██╔═██╗░██║░░╚██╗██╔══╝░░██║╚████║
██████╔╝╚█████╔╝██║░░██║██║░╚██╗╚██████╔╝███████╗██║░╚███║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝
"""


def dork():
    print(banner)
    world = input("Entre ton mot pour le dork: ")
    resultfile = open(f"Dork_Result_{world}.txt", "w")
    resultfile.write(f"""--------------------
Fichier générer par DORKGEN par Xltec | Zxelt

Liste des dorks:

0: "{world}"
1: intitle:"{world}"
2: intitle:"index of" "{world}"
3: inurl:/{world}
4: filetype:txt "{world}"
5: filetype:db "{world}"
6: filetype:mysql "{world}"
7: filetype:png | "{world}"
8: "{world}" filetype:yml "config/parameters.yml"
9: "{world}" filetype:env
10: "{world}" inurl:"/etc/main.cfg"
11: Vous pouvez modifier le script pour en ajouter.
--------------------
                     """)
    resultfile.close()
    print(Fore.GREEN + "Le fichier à bien été créer !")
    time.sleep(1)  # import time
    os.system('cls')
    dork()
    



if __name__ == "__main__":
    dork()
