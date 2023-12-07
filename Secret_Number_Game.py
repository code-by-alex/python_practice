secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won! Great Job! :D")
        break
    if guess != secret_number:
        print("Try Again")
    if guess != secret_number and guess_count == 3:
        print("You Lose :( But don't give up, you'll win one day BELIEVE IT!")



