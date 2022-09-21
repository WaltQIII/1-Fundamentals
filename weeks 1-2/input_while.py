while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Break out of infinite loop")
    option = input("Pick an option: ")
    if option == "1":
        print("You choose 1")
    elif option == "2":
        print("You choose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop.")
