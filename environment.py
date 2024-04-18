import time

seconds = time.time()

def print_seconds(hours, minutes, seconds):
    print(3600*hours+60*minutes+seconds)


print_seconds(1,2,3)
def environment():
    while True:
        player = input("ON/OFF): ").upper()
        if player == 'ON':
            print("You have spawned in your last saved position. Press enter to continue with your journey.", seconds)
            print("You are forest right now. Try obtaining wood and creating a weapon just in case you come across enemies", seconds)
        else:
            print("Enjoy your day... for now...",seconds)
environment()
        
