import random
import time
import sys
import os
from colorama import Fore, Style
from operator import add, sub

operators = (add,sub)
money = 5000
shops = {"Gondola": {"items": {"fruit", "map"}}, "Pharmacy": {"items": {"painkiller", "medkit"}}, "Weaponsmith": {"items": {"sword", "crossbow", "shield"}}, "Mini Market": {"items": {"energydrink", "crackers"}}}
items = {
    "sword": {"name": "Sword", "buyprice": 500, "sellprice": 100},
    "crossbow": {"name": "Crossbow", "buyprice": 1500, "sellprice": 600},
    "shield": {"name": "Shield", "buyprice": 500, "sellprice": 100},
    "fruit": {"name": "Fruit", "buyprice": 500, "sellprice": 50},
    "map": {"name": "Map", "buyprice": 2500, "sellprice": 750},
    "painkiller": {"name": "Painkiller", "buyprice": 650, "sellprice": 50},
    "medkit": {"name": "Medkit", "buyprice": 1500, "sellprice": 500},
    "energydrink": {"name": "Energy Drink", "buyprice": 350, "sellprice": 50},
    "crackers": {"name": "Crackers", "buyprice": 350, "sellprice": 50}
    }

print(Fore.LIGHTRED_EX + "Welcome brave fighter! Your journey starts here!\n" + Style.RESET_ALL)

def start():
    os.system('cls')
    print("Available actions:\n" + Fore.LIGHTRED_EX + "1" + Style.RESET_ALL + ": " + Fore.CYAN + "Find available shops\n" + Fore.LIGHTRED_EX + "2" + Style.RESET_ALL + ": " + Fore.CYAN + "See your character\n")
    selection = int(input(Fore.BLUE + "Please choose a number from the above" + Style.RESET_ALL + ":\n"))
    if selection == 1:
        findShops()
    elif selection == 2:
        findShops()

def findShops():
    os.system('cls')
    print("Available shops:")
    shopIndexes = {}
    shopIndex = 0
    for shop in shops:
        shopIndexes[shopIndex] = shop
        print(Fore.LIGHTRED_EX + str(shopIndex) + Style.RESET_ALL + ": " + Fore.CYAN + shop + Style.RESET_ALL)
        shopIndex += 1
    selection = int(input(Fore.BLUE + "\nSelection" + Style.RESET_ALL + ":\n"))
    os.system('cls')
    print("Available items at " + shopIndexes[selection] + ":")
    itemIndexes = {}
    itemPrices = {}
    itemIndex = 0
    for itemCode in shops[shopIndexes[selection]]["items"]:
        item = items[itemCode]
        itemIndexes[itemIndex] = itemCode
        price = random.choice(operators)(item["buyprice"], random.randint(item["buyprice"]/10, item["buyprice"]/5))
        itemPrices[itemIndex] = price
        print(Fore.LIGHTRED_EX + str(itemIndex) + Style.RESET_ALL + ": " + Fore.YELLOW + item["name"] + Style.RESET_ALL + ": " + Fore.GREEN + str(price) + Style.RESET_ALL)
        itemIndex += 1
    selection = int(input(Fore.BLUE + "\nSelection" + Style.RESET_ALL + ":\n"))
    print(Fore.LIGHTGREEN_EX + "Successfully bought " + Fore.YELLOW + items[itemIndexes[selection]]["name"] + Style.RESET_ALL + " for " + Fore.GREEN + str(itemPrices[selection]) + Style.RESET_ALL)
    time.sleep(3)
    start()

time.sleep(3)
start()