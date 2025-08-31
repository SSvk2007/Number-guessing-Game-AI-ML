import random

print("\nWelcome to the Number Guessing Game!")
print("\nThe computer picks a random number and you try to guess it. "
      "After each guess, you'll be told if it's too high or too low, "
      "and the game will track your attempts and high score.")
high_score = None
round_number = 1

while True:
    print("\nChoose Difficulty Level:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 500)")

    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        max_range = 50
    elif level == "2":
        max_range = 100
    elif level == "3":
        max_range = 500
    else:
        print("Please enter 1, 2 or 3 only.")
        continue

    number = random.randint(1, max_range)
    attempts = 0
    print(f"\nI picked a number between 1 and {max_range}. Try to guess it!")

    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ")

        if guess.lower() == "exit":
            print("\nYou left the game. Thanks for playing!")
            if high_score:
                print(f"Your best score was: {high_score} attempts")
            quit()

        if not guess.isdigit():
            print("That doesn’t look like a number. Try again.")
            continue

        guess, attempts = int(guess), attempts + 1

        if guess < 1 or guess > max_range:
            print(f"Stay in the range 1 to {max_range}.")
        elif guess == number:
            print(f"\nYou got it! The number was {number}. Attempts: {attempts}")


            if attempts == 1:
                print("Wow, first try! That’s rare.")
            elif attempts <= 5:
                print("Great job, that was quick.")
            elif attempts <= 10:
                print("Good work, you figured it out.")
            else:
                print("Finally got it. Better late than never!")

            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"New high score: {high_score} attempts.")
            break
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

    print(f"\nRound {round_number} finished. Attempts: {attempts}")
    if high_score:
        print(f"Current High Score: {high_score} attempts")
    round_number += 1

    again = input("Do you want to play again? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        print("\nThanks for playing. See you next time!")
        if high_score:
            print(f"Your best score was: {high_score} attempts")
        break
#THIS GAME IS MADE BY SHAURYA SINGH (RA2511026010078), COURSE- CSE(AI/ML)
#REFERENCES-
#https://youtu.be/jcKe13D6bao
#HELP FROM CHATGPT/DEEPSHEEK (THIS WAS MY FIRST PROJECT, I NEEDED HELP WITH PYTHON SYNTAX AND LOGIC)
#https://www.geeksforgeeks.org/python-random-module/
#CODED ON VS CODE
#HOPE THIS GAME WAS FUN
#THANK YOU