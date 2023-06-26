import os

money = 10000000

def menu():
  print("Welcome to my shop!")
  print("1. Shop\n2. ATM\n3. Quit")
  print()
  print("=" * 20, "Your money", "=" * 20)
  print("=" * 20, "{:^10}".format(f"{money:,d}"), "=" * 20)
  print()
  choice = input("Choose a number from above: ")

  if choice == "1":
    os.system("clear")
    shop()
  elif choice == "2":
    os.system("clear")
    atm()
  elif choice == "3":
    os.system("clear")

def shop():
  while True:
    global money
    # global nintendo
    # global Ps5
    # global java
    # global animal
    # global xbox
    print("Things i sell in my shop:")
    print()
    print("=" * 42)
    print("|1.|{:<20}|{:^16}|".format(" Nintendo Switch", "Rp 4.000.000"))
    print("=" * 42)
    print("|2.|{:<20}|{:^16}|".format(" PlayStation 5", "Rp 10.000.000"))
    print("=" * 42)
    print("|3.|{:<20}|{:^16}|".format(" Minecraft Java PC", "Rp 200.000"))
    print("=" * 42)
    print("|4.|{:<20}|{:^16}|".format(" Animal Crossing", "Rp 540.000"))
    print("=" * 42)
    print("|5.|{:<20}|{:^16}|".format(" Xbox 360 w/ kinect", "Rp 2.155.000"))
    print("=" * 42)
    print()
    print("=" * 10, "Your money", "=" * 10)
    print("=" * 10, "{:^10}".format(f"{money:,d}"), "=" * 10)
    print()
  
    ye = input("Select the number from above (0 to go back): ")
   
    if ye == "1":
      nintendo = 4000000
      if money <= nintendo:
        print("You don't have enough money!\n1. ATM\n2. Stay in the shop")
        print()
        choice = input("Your choice? ")
        if choice == "1":
          os.system("clear")
          atm()
        elif choice == "2":
          os.system("clear")
          shop()
        
      elif ye =="1":
        input("Thanks for buying! Press enter to continue: ")
        os.system("clear")
        money-= nintendo
        
    elif ye == "2":
      Ps5 = 10000000
      if money < Ps5:
        print("You don't have enough money!\n1. ATM\n2. Stay in the shop")
        print()
        choice = input("Your choice? ")
        if choice == "1":
          os.system("clear")
          atm()
        elif choice == "2":
          os.system("clear")
          shop()
        
      elif ye =="2":
        input("Thanks for buying! Press enter to continue: ")
        os.system("clear")
        money-= Ps5
        
    elif ye == "3":
      java = 200000
      if money <= java:
        print("You don't have enough money!\n1. ATM\n2. Stay in the shop")
        print()
        choice = input("Your choice? ")
        if choice == "1":
          os.system("clear")
          atm()
        elif choice == "2":
          os.system("clear")
          shop()
        
      elif ye =="3":
        input("Thanks for buying! Press enter to continue: ")
        os.system("clear")
        money -= java  
    elif ye == "4":
      animal = 540000
      if money <= animal:
        print("You don't have enough money!\n1. ATM\n2. Stay in the shop")
        print()
        choice = input("Your choice? ")
        if choice == "1":
          os.system("clear")
          atm()
        elif choice == "2":
          os.system("clear")
          shop()
        
      elif ye =="4":
        input("Thanks for buying! Press enter to continue: ")
        os.system("clear")
        money-= animal
    elif ye == "5":
      xbox = 2155000
      if money <= xbox:
        print("You don't have enough money!\n1. ATM\n2. Stay in the shop")
        print()
        choice = ("Your choice? ")
        choice = input("Your choice? ")
        if choice == "1":
          os.system("clear")
          atm()
        elif choice == "2":
          os.system("clear")
          shop()
        
      elif ye =="5":
        input("Thanks for buying! Press enter to continue: ")
        os.system("clear")
        money -= xbox
    elif ye == "0":
        os.system("clear")
        menu()
      
    continue

def atm():
  global money
  print("Welcome to ATM!")
  money+= int(input("How much money would you like to withdraw? "))
  print()
  print("Success!")
  print()
  print("=" * 10, "Your money", "=" * 10)
  print("=" * 10, "{:^10}".format(f"{money:,d}"), "=" * 10)
  print()
  input("Press enter to go back to main page ")
  os.system("clear")
  menu()

menu()
