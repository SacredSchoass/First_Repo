guess = 0
tries = 0

while guess != 6 and tries <3:
  guess = int(input("Guess the number:  "))
  tries +=1

  if tries == 3:
    print("You failed!")
    break
  elif guess == 6:
    print("You guessed it!")
    break  

