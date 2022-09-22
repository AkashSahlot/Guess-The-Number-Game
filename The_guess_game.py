from cgi import print_directory
import random
randNumber = random.randint(1,100)
#print(randNumber)
userGuess= None
guesses=0


while(userGuess!= randNumber):
     userGuess = int(input("Please Enter a Number to Guess Between 1 to 100 :"))
     guesses += 1
     if (userGuess==randNumber):
       print("you guessed it  right")
     else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller Number.")
        else:
            print("you guessed it wrong!! Enter a larger Number")
        



print(f" You guesses the number in {guesses} guesses")  


with open("hiscore.txt", "r") as f:
    hiscore= int(f.read())
if (guesses<hiscore):
 print("you have just broken the high score")
 with open("hiscore.txt","w") as f:
    f.write(str(guesses))
