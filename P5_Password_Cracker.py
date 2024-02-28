import string
import random

user_password = input("Enter a random password")

password = list(string.ascii_letters + string.ascii_digits + string.ascii_punctuation )

guess = ""

while guess != user_password:
    guess = ""

    for letter in range(len(user_password)):
        guess_letter = password[random.randint(0,6)]
        guess = str(guess_letter) + str(guess)

print("your password is ", guess)
