import random
status = "happy"
hunger = 0
tired = 0

print("welcome to the virtaul pet game")
print("keep your pet happy by feeding it...")
print("play with it...")
print("make it rest...")
print("and buy it toys")
print("enjoy this simple command line game by Alter Net codes!")
input("Press Enter to continue...")
for i in range(20):
    print(" ")
while True:
    print("looks like your dog is", status)
    print("you can FEED, PLAY, REST, BUY TOYS, EXIT")
    if tired < 4:
        print("your dog is tired.")
    if hunger < 4:
        print("your dog is hungry.")
    task = input("what would you like to do? ")
    if task == "play":
        hunger = hunger + 2
        tired = tired + 2
        print("you go to the park to play with your dog!")
        status = "excited"
        print("your dog is", status,"to be at the park")
        number = random.randint(0,100)
        numberpicked = input("pick a number from 1-100: ")
        if numberpicked < number:
            print("oh not quite! the number that was right was:", number)
            print("you throw the ball about 20 feet!")
            print("nice throw!")
            print(" ")
            status = "satisfied"
        else:
            if numberpicked > number:
                print("NOT quite! still good!")
                print("nice! you the throw the ball about 20 feet")
                print("nice throw!")
                print(" ")
                status = "satisfied"
            else:
                if numberpicked == number:
                    print("YES! YOU GOT IT!!!")
                    print("you throw the ball 50 feet!")
                    print("ELEGANT!!!!!!!!")
                    print("")
                    status = "VERY happy"
    elif task == "feed":
        print("good idea to feed him he was at", hunger,"hunger points!")
        print("you feed your dog")
        print("your dog is now cured of its hunger")
        hunger = 0
        print(hunger)
    elif task == "rest":
        print("good idea your dog was at:", tired,"tired points")
        print("you put your dog to sleep")
        print("your dog is now cured of its tiredness.")
    elif task == "buy toys":
        print("you buy a few toys for your dog.")
        status = "playful"
    elif task == "exit":
        print("goodbye!")
        print("see you later")
        print("saving and quiting...")
        break
    else:
        print("that is not a thing you can do!")
