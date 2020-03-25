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
        if secret - number < 100: #Making the game more complicated and probably less efficient but worth the practice...
            print("Low but almost there!")
        else:
            print("Too low! Long way to go!")
    elif number > secret:
        if number - secret < 100:
            print("High but almost there!")
        else:
            print("Too high! Long way to go!")
    else:
        print("Yay! You got it!!")

 
#Fastest way is to start at n/2 (n = 1000 in this case)?
