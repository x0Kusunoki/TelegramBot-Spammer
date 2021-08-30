
#LIBS


import time
import sys
import colorama
import os
import requests
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
correct_answers = 0

point = 0
#COLORS

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT





messages = 0


#SCRIPT

print(fg+"""
 _       ____________  __  ______  ____  __ __    ________  __________ __ ____________ 
| |     / / ____/ __ )/ / / / __ \/ __ \/ //_/   / ____/ / / / ____/ //_// ____/ __ \/
| | /| / / __/ / __  / /_/ / / / / / / / ,<     / /_  / / / / /   / ,<  / __/ / /_/ /
| |/ |/ / /___/ /_/ / __  / /_/ / /_/ / /| |   / __/ / /_/ / /___/ /| |/ /___/ _, _/ 
|__/|__/_____/_____/_/ /_/\____/\____/_/ |_|  /_/    \____/\____/_/ |_/_____/_/ |_|  
                                                                                     
"""+fw+"""                         [+]TELEGRAM WEBHOOK FUCKER
                         [+]USE IT FOR FUCK THE BOTS OF THE BACKDOORED SCAMAPAGES OR CONFIGS

 """)



time.sleep(2)

bot_tk = input("> Enter The Bot Token : ")
chat_id = input("> Enter Enter The Chat Id : ")
lettre = input("> Enter The Message   : ")
msg = input("> Enter The Number Of messages : ")

print("\n\n\n")



for i in range (1,int(msg)):
    send_text = 'https://api.telegram.org/bot' + bot_tk + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + lettre
    response = requests.get(send_text)
    messages = messages + 1
    print(fy+ str(messages)+ ">>>" +fc+"[ x0Kusunoki ] " + fg + """SENT SECCUSSFULU
-----------------------------------------""")
    
    




