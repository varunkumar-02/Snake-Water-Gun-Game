import random  # Importing the random module to let the computer make a random choice

# Snake , Water , Gun Game

Computer = random.choice([-1, 0, 1])
gameDict = {1: "Water", -1: "Snake", 0: "Gun"}

# Show the user the options they can choose from
print("choose one : \nS for snake\nW for water\nG for Gun")

# Take input from user
user = input("Enter your choice : ")
youDict = {"s": -1, "w": 1, "g": 0}
user_choose = youDict[user]

# shows Computer and user choice
print(f"computer choose : {gameDict[Computer]}")
print(f"User choose : {gameDict[user_choose]}")


if Computer == user_choose:
    print("It's draw!")
else:
    if Computer == 1 and user_choose == 0:
        print("You lose!")
    elif Computer == 1 and user_choose == -1:
        print("You Win!")
    elif Computer == -1 and user_choose == 0:
        print("You Win!")
    elif Computer == -1 and user_choose == 1:
        print("You lose!")
    elif Computer == 0 and user_choose == 1:
        print("You win!")
    elif Computer == 0 and user_choose == -1:
        print("You lose!")
    else:
        print("something wrong.")

