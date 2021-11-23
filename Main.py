import random
from random import choice
import os, time


creditChoice = [100, 150, 200 , 250, 300, 350, 400, 450, 500]
rangeCredits = random.choice(creditChoice)
credits = rangeCredits
storeArray = []
count = 0
symbol = (" 🍒 "," 🔔 "," 🍋 "," 🍊 "," ⭐ "," 💀 ")

run = True

def wheel():
     return choice ([" 🍒 "," 🔔 "," 🍋 "," 🍊 "," ⭐ "," 💀 "])
def spin():
    arrayWheel = [f"|{wheel()}|{wheel()}|{wheel()}|"]
    for i in arrayWheel:
      storeArray.append(i)
      return i
def output_spin(count):
  print()
  print(f"Spin {count}: {spin()}")
  print()

while run:
  print()
  user = input("Type Y To Play Or N To Exit The Program,\nBeware This Will Cost You 20 Credits: ").lower()
  if user == "y":
      count += 1
      credits = credits - 20
      print()
      print(f"Credits: {credits}p")
      output_spin(count)
      print()
      for i in storeArray:
        if (
            i[2] == "🍒"
            and i[6] == "🍒"
            and i[10] != "🍒"
            or i[2] == "🍒"
            and i[6] != "🍒"
            and i[10] == "🍒"
            or i[2] != "🍒"
            and i[6] == "🍒"
            and i[10] == "🍒"
        ):
            credits = credits + 50
            print("Winner, You Won 50p")
            
        if (
            i[2] == "🍒"
            and i[6] == "🍒"
            and i[10] == "🍒"
        ):
            credits = credits + 100
            print("Winner, You Won £1")
            
        if (
            i[2] == "🔔"
            and i[6] == "🔔"
            and i[10] != "🔔"
            or i[2] == "🔔"
            and i[6] != "🔔"
            and i[10] == "🔔"
            or i[2] != "🔔"
            and i[6] == "🔔"
            and i[10] == "🔔"
        ):
            credits = credits + 100
            print("Winner, You Won £1")
        if (
            i[2] == "🔔"
            and i[6] == "🔔"
            and i[10] == "🔔"
        ):
            credits = credits + 500
            print("Jackpot, You Won £5")
            
        if (
            i[2] == "🍋"
            and i[6] == "🍋"
            and i[10] != "🍋"
            or i[2] == "🍋"
            and i[6] != "🍋"
            and i[10] == "🍋"
            or i[2] != "🍋"
            and i[6] == "🍋"
            and i[10] == "🍋"
        ):
            credits = credits + 50
            print("Winner, You Won 50p")
        if (
            i[2] == "🍋"
            and i[6] == "🍋"
            and i[10] == "🍋"
        ):
            credits = credits + 100
            print("Winner, You Won £1")
        if (
            i[2] == "🍊"
            and i[6] == "🍊"
            and i[10] != "🍊"
            or i[2] == "🍊"
            and i[6] != "🍊"
            and i[10] == "🍊"
            or i[2] != "🍊"
            and i[6] == "🍊"
            and i[10] == "🍊"
        ):
            credits = credits + 50
            print("Winner, You Won 50p")
        if (
            i[2] == "🍊"
            and i[6] == "🍊"
            and i[10] == "🍊"
        ):
            credits = credits + 100
            print("Winner, You Won £1")
        if (
            i[2] == "⭐"
            and i[6] == "⭐"
            and i[10] != "⭐"
            or i[2] == "⭐"
            and i[6] != "⭐"
            and i[10] == "⭐"
            or i[2] != "⭐"
            and i[6] == "⭐"
            and i[10] == "⭐"
        ):
            credits = credits + 50
            print("Winner, You Won 50p")
            
        if (
            i[2] == "⭐"
            and i[6] == "⭐"
            and i[10] == "⭐"
        ):
            credits = credits + 100
            print("Winner, You Won £1")
        if (
            i[2] == "💀"
            and i[6] == "💀"
            and i[10] != "💀"
            or i[2] == "💀"
            and i[6] != "💀"
            and i[10] == "💀"
            or i[2] != "💀"
            and i[6] == "💀"
            and i[10] == "💀"
        ):
            credits = credits - 100
            print("Loser, You Lost £1")
       
        if (
            i[2] == "💀"
            and i[6] == "💀"
            and i[10] == "💀"
        ):
            credits = credits - credits
            print(f"Credits: {credits}, GAME OVER!!! YOU HAVE NO CREDITS")
    
      storeArray.clear()
      #time.sleep(4)
      #os.system("clear")
  elif user == "n":
    print()
    os.system("clear")
    print(f"You Spun The Wheel {count} Times!!!")
    print(f"You Have {credits}p Left!!!")
    time.sleep(5)
    os.system("clear")
    run = False
  if(credits <= 0):
    print()
    print(f"You Spun The Wheel {count} Times!!!")
    print("You Have No Credits Left You Noob!!!!")
    time.sleep(5)
    os.system("clear")
    run = False
  elif(credits < 20):
    print()
    print(f"You Spun The Wheel {count} Times!!!")
    print("You Have No Credits Left To Spin Again!!")
    time.sleep(5)
    os.system("clear")
    run = False
