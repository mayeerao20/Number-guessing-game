import random

def user_guesses_number():
    print("Welcome to the Number Guessing Game!")
    print("You have 8 chances to guess the number.")
    print("Think of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 8:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it right!")
            break

    if guess != secret_number:
        print(f"Sorry, you ran out of attempts. The number was {secret_number}.")

    return attempts

def system_guesses_number():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("You have to tell me if my guess is too high (H), too low (L), or correct (C).")

    lower_bound = 1
    upper_bound = 100
    attempts = 0

    while attempts < 8:
        guess = random.randint(lower_bound, upper_bound)
        print(f"My guess is: {guess}")
        response = input("Is it too high (H), too low (L), or correct (C)? ").upper()
        attempts += 1

        if response == "C":
            print("Hooray! I guessed it right!")
            break
        elif response == "H":
            upper_bound = guess - 1
        elif response == "L":
            lower_bound = guess + 1
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

    if response != "C":
        print(f"Sorry, I couldn't guess the number in 8 attempts. The number was {guess}.")

    return attempts

def main():
    while True:
        user_choice = input("Do you want the system to guess the number (S) or do you want to guess the number yourself (U)? ").upper()

        if user_choice == "S":
            attempts = system_guesses_number()
            print(f"The system guessed the number in {attempts} attempts.")
        elif user_choice == "U":
            attempts = user_guesses_number()
            print(f"You guessed the number in {attempts} attempts.")
        else:
            print("Invalid choice. Please enter 'S' or 'U'.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
