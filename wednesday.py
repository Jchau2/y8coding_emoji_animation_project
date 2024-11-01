from os import system
clear = lambda:system("clear")

from time import sleep


print("NOW WE HAVE A 50M DASH!")
sleep(1.5)

print("OUR FIRST CONTESTANT IS OUR WORLD CHAMPION, THE TIGER!")
sleep(1.5)

print("on your marks...")
sleep(1.5)
print("get set...")
sleep(1.5)
print("GO!🔫💥")
sleep(1.5)

clear()
x = chr(128047)

for i in range(20):
    print(" " * i, x)
    sleep(0.25)
    clear()

print(" " * i, x)