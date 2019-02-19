import time
lock = True

while lock:
    number = int(input("please select a number to countdown from:  "))
    if number > 20:
        print ("Please select an number 20 or less.")
    else :
        lock = False
while number > 0:
    time.sleep(1)
    number = number - 1
    print(number)
print("Gotta blast!")
