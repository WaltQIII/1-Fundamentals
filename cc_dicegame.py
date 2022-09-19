import random

high_score = 0


def dice_game():
    global high_score
    print("Current High Score: ")
    print("1) Roll Dice")
    print("2) Leave Game\n")


while True:
    dice_game()
    player = int(input("Enter your choice: "))
    if player == 1:
        result_one = random.randint(1, 6)
        print(f"You roll a ... ", {result_one})
        result_two = random.randint(1, 6)
        print(f"You roll a ... ", {result_two},"\n")
        total_score = result_one + result_two
        print("You have rolled a total of: ", str(total_score) + "\n")

        if total_score > high_score:
            high_score = total_score
            print("New high score!\n")
    else:
        print("Goodby!")
        break
