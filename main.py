import random

def guess_number():
    lowest = 1
    highest = 100
    attempts = 0

    x = random.randint(lowest, highest)

    print(f"Guess the secret number between {lowest} and {highest}")

    while True:
        try:
            player = int(input("Enter your number: "))
            attempts += 1

            if player < x:
                print("Too low!")
            elif player > x:
                print("Too high!")
            elif player > highest or player < lowest:
                print("Please guess the number between {lowest} and {highest} only!")
            else:
                print(f"Congrats ngabss!")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()