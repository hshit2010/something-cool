import time

first = input("enter the time intervals first digit :")
second = input("enter the time intervals second digit :")
first = int(first)
second = int(second)
def count(start , end):
    for x in range(start, end+1 , -1):
        print(x)
        time.sleep(1)
    print("done!!")

time_clock = count(second,first)
print(f"{time_clock}")

