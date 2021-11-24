# Guess the number between 1-30

import random
n = 20
guessing = int(n * random.random()) + 1
guess = 0
while guess != guessing:
      guess = int(input("New number: "))
      if guess > 0:
          if guess > guessing:
              print("Number is too large")
          elif guess < guessing:
              print("Number is too small")
      else:
              print("Sorry on that you're giving up")
              break
else:
        print("Congrats, You made it!")
