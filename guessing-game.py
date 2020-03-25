# In case you are too bored hanging out with yourself, here is how you can hang out with your computer...

import random
help(random) #I have no clue how to use this thing... Gotta look it up!

secret = random.randrange(1000)

while True:
    guess = input("Guess what number your cute PC is having in mind, please [q to quit]: ")
    if guess == 'q':
        break
    number = int(guess)
    if number < secret:
        print("Too low!")
    elif number > secret:
        print("Too high!")
    else:
        print("Yay! You got it!!")
 
#Fastest way is to start at n/2 (n = 1000 in this case)?
