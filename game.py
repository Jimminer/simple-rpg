import random
import time
import sys
import os
from colorama import Fore, Style
from operator import add, sub
import math
from console.utils import wait_key

def initialize():
    global debugPrints, player, operators, actions, shops, items, fishingRarities
    debugPrints = True
    player = {"name": "Fiko", "money": 1000, "level": 1, "experience": 0, "inventory": {}}

    operators = (add,sub)
    actions = {1: {"number": "1", "title": "Find available shops", "function": findShops}, 2: {"number": "2", "title": "See your stats", "function": seeStats}, 3: {"number": "3", "title": "Go fishing", "function": goFish}}
    shops = {"Gondola": {"items": {"fruit", "map"}}, "Pharmacy": {"items": {"painkiller", "medkit"}}, "Weaponsmith": {"items": {"sword", "crossbow", "shield"}}, "Mini Market": {"items": {"energydrink", "crackers"}}}
    items = {
        "sword": {"name": "Sword", "buyprice": 500, "sellprice": 100},
        "crossbow": {"name": "Crossbow", "buyprice": 1500, "sellprice": 600},
        "shield": {"name": "Shield", "buyprice": 500, "sellprice": 100},
        "fruit": {"name": "Fruit", "buyprice": 500, "sellprice": 50},
        "map": {"name": "Map", "buyprice": 2500, "sellprice": 750},
        "painkiller": {"name": "Painkiller", "buyprice": 650, "sellprice": 250},
        "medkit": {"name": "Medkit", "buyprice": 1500, "sellprice": 500},
        "energydrink": {"name": "Energy Drink", "buyprice": 350, "sellprice": 50},
        "crackers": {"name": "Crackers", "buyprice": 350, "sellprice": 50},
        "sardine": {"name": "Sardine", "buyprice": 800, "sellprice": 500},
        "boot": {"name": "Boot", "buyprice": 100, "sellprice": 10},
        "ancientbook": {"name": "Ancient Book", "buyprice": 1000000, "sellprice": 40000}
        }
    fishingRarities = {"Uncommon": {"range1": 0, "range2": 30, "color": Fore.LIGHTWHITE_EX, "items": ["boot", "energydrink"]}, "Common": {"range1": 30, "range2": 70, "color": Fore.LIGHTGREEN_EX, "items": ["sardine", "painkiller"]}, "Rare": {"range1": 70, "range2": 90, "color": Fore.BLUE, "items": ["map", "medkit"]}, "Ultra Rare": {"range1": 90, "range2": 100, "color": Fore.MAGENTA, "items": ["ancientbook"]}}


def welcome():
    player["name"] = input(Fore.LIGHTRED_EX + "Welcome brave fighter! Your journey starts here! How should I call you?\n" + Style.RESET_ALL)
    time.sleep(1)
    os.system('cls')
    print("Nice to meet you " + player["name"] + ", I'm Carl and I'll be following you on your mission to defeat Viktor.\n")
    time.sleep(5)
    print("Who's Viktor you ask?\n")
    time.sleep(3)
    print("Viktor is the guy that destroyed humanity. Don't you remember?\n")
    time.sleep(5)
    print("Argh, I guess I'll have to remind you of some things before we start.\n")
    time.sleep(5)
    os.system('cls')
    print("You see, a few million light years ago, Mars used to be the sickest place! Everyone would come here for their Glebsworth vacations.\n")
    time.sleep(10)
    print("You can't be serious! You don't know what Glebsworth is??\n")
    time.sleep(5)
    print("Well, it's like that Summer thing you Earth people have except is like a billion times better.\n")
    time.sleep(7)
    print("Anyways though, back to my lecture. As we were all having fun during our Glebsworth holidays, Viktor came and demanded to take ownership of the planet. As you would probably guess, we declined... And then.....\n")
    time.sleep(20)
    os.system('cls')
    print(Fore.RED  + "KAPOWWW!!!!!!\n" + Style.RESET_ALL)
    time.sleep(2)
    print("The whole planet was covered with fire.\n")
    time.sleep(5)
    print("Almost everyone died...\n")
    time.sleep(3)
    print("Except...\n")
    time.sleep(3)
    print("You and Me!!!!\n")
    time.sleep(3)
    os.system('cls')
    print("So what do you say. Are you ready for a real challenge " + player["name"] + "?\n")
    startDecision = input("(y/n): " + Fore.YELLOW)
    print(Style.RESET_ALL)
    if startDecision == "y":
        os.system('cls')
        print("That's the spirit!! Let's go then, hurry!! We have no time to lose!")
        time.sleep(5)
        start()
    else:
        os.system('cls')
        print("Good luck then. I guess I won't see you ever again....\n")
        time.sleep(5)
        print(Fore.YELLOW + "COWARD!!" + Style.RESET_ALL)

def start():
    os.system('cls')
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Running start()")
    print("Available actions:\n\n" + "".join(Fore.LIGHTRED_EX + action["number"] + Style.RESET_ALL + ": " + Fore.CYAN + action["title"] + "\n" for action in actions.values()))
    selection = int(input(Fore.BLUE + "Please choose a number from the above" + Style.RESET_ALL + ":\n"))
    if selection in actions:
        time.sleep(1)
        os.system('cls')
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Running " + str(actions[selection]["function"].__name__) + "()")
        actions[selection]["function"]()

def findShops():
    print("Available shops:")
    shopIndexes = {}
    shopIndex = 0
    for shop in shops:
        shopIndexes[shopIndex] = shop
        print(Fore.LIGHTRED_EX + str(shopIndex) + Style.RESET_ALL + ": " + Fore.CYAN + shop + Style.RESET_ALL)
        shopIndex += 1
    selection = int(input(Fore.BLUE + "\nSelection" + Style.RESET_ALL + ":\n"))
    os.system('cls')
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Finding items using findShops()")
    print("Available items at " + shopIndexes[selection] + ":")
    itemIndexes = {}
    itemPrices = {}
    itemIndex = 0
    for itemCode in shops[shopIndexes[selection]]["items"]:
        item = items[itemCode]
        itemIndexes[itemIndex] = itemCode
        price = random.choice(operators)(item["buyprice"], random.randint(int(item["buyprice"]/100), int(item["buyprice"]/5)))
        itemPrices[itemIndex] = price
        print(Fore.LIGHTRED_EX + str(itemIndex) + Style.RESET_ALL + ": " + Fore.YELLOW + item["name"] + Style.RESET_ALL + ": " + Fore.GREEN + str(price) + Style.RESET_ALL)
        itemIndex += 1
    selection = int(input(Fore.BLUE + "\nSelection" + Style.RESET_ALL + ":\n"))
    if addItem(itemIndexes[selection], 1, itemPrices[selection]):
        print(Fore.LIGHTGREEN_EX + "Successfully " + Style.RESET_ALL + "bought " + Fore.LIGHTGREEN_EX + "1x " + Fore.YELLOW + items[itemIndexes[selection]]["name"] + Style.RESET_ALL + " for " + Fore.GREEN + str(itemPrices[selection]) + Style.RESET_ALL)
    else:
        print("You " + Fore.RED + "don't" + Style.RESET_ALL + " have enough money to buy this item!")
    print("\nPress any key to go back to the main menu.")
    wait_key()
    start()

def seeStats():
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Player: " + str(player) + "\n")
    inventory = "\n"
    for item, quantity in player["inventory"].items():
        inventory = inventory + "    " + Fore.LIGHTGREEN_EX + str(quantity) + "x " + Fore.YELLOW + items[item]["name"] + "\n" + Style.RESET_ALL
    if inventory == "\n":
        inventory = Fore.LIGHTRED_EX + "Empty" + Style.RESET_ALL
    print("Player Stats:\n")
    print(Fore.LIGHTYELLOW_EX + "Name: " + Fore.LIGHTRED_EX + player["name"] + Fore.LIGHTYELLOW_EX + "\nLevel: " + Fore.LIGHTRED_EX + str(player["level"]) + Fore.LIGHTYELLOW_EX + "\nMoney: " + Fore.LIGHTRED_EX + str(player["money"]) + Fore.LIGHTYELLOW_EX + "\nInventory: " + inventory + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "Level " + str(player["level"] + 1) + " Progress: " + Fore.LIGHTRED_EX + createProgressBar(player["experience"]/calculateExp(player["level"])*100, 1, 5) + Style.RESET_ALL)
    print("\nPress any key to go back to the main menu.")
    wait_key()
    start()

def goFish():
    print("You attach a bait onto your fishing rod and you throw it deep into the sea.\n")
    time.sleep(3)
    if random.randint(0,10) != 0:
        print("Oh?? You caught something!!\n")
        time.sleep(2)
        chance = random.randint(0, 100000)/1000
        chosenRarity = None
        for rarity, content in fishingRarities.items():
            if chance >= content["range1"] and chance <= content["range2"]:
                chosenRarity = rarity
                break
        fish = random.choice(fishingRarities[chosenRarity]["items"])
        addExp(random.randint(int(player["level"]/2) + 1, player["level"]*10), player["experience"])
        addItem(fish, 1)
        print("[" + fishingRarities[chosenRarity]["color"] + chosenRarity + Style.RESET_ALL + "] You found " + Fore.LIGHTGREEN_EX + "1x " + Fore.YELLOW + items[fish]["name"] + Style.RESET_ALL)
        selection = input("\nWould you like to sell it?\n(y/n): " + Fore.YELLOW)
        print(Style.RESET_ALL)
        if selection == "y":
            price = random.choice(operators)(items[fish]["sellprice"], random.randint(int(items[fish]["sellprice"]/100), int(items[fish]["sellprice"]/5)))
            removeItem(fish, 1, price)
            print(Fore.LIGHTGREEN_EX + "Successfully " + Style.RESET_ALL + "sold " + Fore.LIGHTGREEN_EX + "1x " + Fore.YELLOW + items[fish]["name"] + Style.RESET_ALL + " for " + Fore.GREEN + str(price) + Style.RESET_ALL)
    else:
        print("You unfortunately couldn't catch something. Better luck next time.")
    print("\nPress any key to go back to the main menu.")
    wait_key()
    start()

def addItem(item, quantity=1, money=0):
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Adding " + str(quantity) + " " + item + " for a price of " + str(money) + "\n")
    if money > 0:
        if player["money"] >= money:
            player["money"] -= money
            if item in player["inventory"]:
                player["inventory"][item] += quantity
            else:
                player["inventory"][item] = quantity
            return True
        else:
            return False
    else:
        if item in player["inventory"]:
            player["inventory"][item] += quantity
        else:
            player["inventory"][item] = quantity
        return True

def removeItem(item, quantity=1, money=0):
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Removing " + str(quantity) + " " + item + " for a price of " + str(money) + "\n")
    if item in player["inventory"]:
        if player["inventory"][item] > quantity:
            player["inventory"][item] -= quantity
            player["money"] += money
            return True
        elif player["inventory"][item] == quantity:
            del player["inventory"][item]
            player["money"] += money
            return True
        else:
            return False
    else:
        return False

def createProgressBar(value, roundNum=1, progressMin=1):
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Creating a progress bar with values: value=" + str(value) + " roundNum=" + str(roundNum) + " progressMin=" + str(progressMin) + "\n")
    value = int(roundNum * round(value/roundNum))
    progressBar = str(value) + "% ["
    for i in range(int(value/progressMin)):
        progressBar = progressBar + "⣿"
    if value != 0 and value != 100:
        progressBar = progressBar + "⣦"
    for i in range(int(100/progressMin - value/progressMin)):
        progressBar = progressBar + "⣀"
    progressBar = progressBar + " ]"
    return progressBar

def addExp(exp, curExp=0):
    if debugPrints:
        print(Fore.RED + "DEBUG: " + Style.RESET_ALL + "Adding " + str(exp) + " exp (current exp is " + str(curExp) + ")\n")
    maxExp = calculateExp(player["level"])
    if (curExp + exp) >= maxExp:
        player["level"] += 1
        print(Fore.YELLOW + "\nYou leveled up! You're now level " + Fore.LIGHTGREEN_EX + str(player["level"]) + "\n" + Style.RESET_ALL)
        addExp(curExp + exp - maxExp, 0)
    else:
        player["experience"] = curExp + exp

def calculateExp(level):
    return int(level*8.35 + level**2 + 10)

initialize()
time.sleep(1)
newCheck = input("Are you experienced with simple RPG?\n(y/n): " + Fore.YELLOW)
print(Style.RESET_ALL)
if newCheck == "y":
    start()
else:
    welcome()