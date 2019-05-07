import time

def sleeper():
    while True:
        num = input("please enter how long to wait: -> ")

        try:
            num = float(num)
        except:
            print("please enter in a number. \n")
            continue
        print('Before: {}'.format( time.ctime()))
        time.sleep(num)
        print("After: {}\n".format(time.ctime()))

try:
    sleeper()
except:
    print("\n\n\Keyboard exception received. Exiting.")
    exit()