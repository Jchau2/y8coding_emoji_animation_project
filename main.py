from time import sleep

from os import system
clear = lambda : system("clear")

print("WELCOME TO THE ANNUAL PET OLYMPICS MAYHEM!!!")
print("THIS EXCITING CONTEST WILL HAVE 3 EVENTS")
print("""THE EVENTS ARE:
      1. 100M DASH
      2. LONG JUMP
      3. 50M FREESTYLE""")


event = input("What event do you want to see first?")
if event == "100m dash":
    print("NOW WE ARE UNDERWAY ON THE 100M DASH!")
    sleep(2)
    print("OUR CONTESTANTS ARE:")
    sleep(2)
    print("🦁THE LION!")
    sleep(2)
    print("🐯OUR WORLD CHAMPION, THE TIGER!")
    sleep(2)
    print("🦊THE DARK HORSE OF THE TOURNAMENT, THE FOX!")
    sleep(2)
    print("🐶THE SPEEDY YOUNGSTER, THE DOG!")
    sleep(2)
    print("🐱THE TITLE CONTENDER, THE CAT!")
    sleep(2)
    print("🐮THE VETERAN COW!")
    sleep(2)
    print("🐵THE NEWLY DEBUTED ROOKIE, THE MONKEY!")
    
    clear(100)
