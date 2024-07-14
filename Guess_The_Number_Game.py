import random

# Introduction
print("Welcome to my guess the number game."
      "\nWin this game by guessing the correct number from 0-5."
      "\nGood luck and have fun! :)")

while True:
    guess_number = int(input("Enter a number from 0-5: "))
    correct_number = random.randrange(0, 6)

    if guess_number > 5:
        print("Invalid! Please try again.")
        continue

    if guess_number == correct_number:
        print("Congratulations! You guessed the correct number. The correct number is " + str(correct_number))
        try_again_prompt = input("Would you like to play again? Press Y for Yes"
                                 " and press N for No. ")
        if try_again_prompt.upper() == 'Y':
            continue
        if try_again_prompt.upper() != 'Y' or 'N':
            print("You pressed the wrong key.")
            break
        if try_again_prompt.upper() == 'N':
            print("Thank you for playing! Play again next time!")
            break
    else:
        print("Sorry. You guessed the wrong number.")
        try_again_prompt = input("Would you like to play again? Press Y/y for Yes"
                                 "and press N/n for No. ")
        if try_again_prompt.upper() == 'Y':
            continue
        if try_again_prompt.upper() != 'Y' or 'N':
            print("You pressed the wrong key.")
            break
        if try_again_prompt.upper() == 'N':
            print("Thank you for playing! Play again next time!")
            break
