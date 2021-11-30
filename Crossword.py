import random

name=input("Enter your name:")
print(f"Hello {name}! Welcome to the guessing game!")

wordslist=["annaconda","navigator","python","apple","google","microsoft","starbucks","opensource","horizon","windows","linux","sublime","android","macbook"]

# get a random word from this list
index_of_words=random.randint(0, len(wordslist))
choosenword=wordslist[index_of_words]
indexes_choosen_before=random.sample(range(0, len(choosenword)),3)

#characters that the user has guessed so far
guesses=""

for i in indexes_choosen_before:
        guesses += choosenword[i]
        
chances = 10        
play = "Yes"        

def playagain():
    global play
    play = input("Do you want to play again?(Yes/No):")
    if play == "Yes":
        global chances,choosenword,guesses
       # global wordslist
        chances=10
       # wordslist=["annaconda","navigator","python","apple","google","microsoft","starbucks","opensource","horizon","windows","linux","sublime","android","macbook"]
        index_of_words = random.randint(0, len(wordslist))
        choosenword = wordslist[index_of_words]
        indexes_choosen_before = random.sample(range(0, len(choosenword)),3)
        guesses = ""
        for i in indexes_choosen_before:
            guesses += choosenword[i]
        
        
while play == "Yes":
    while chances > 0:
        won = True
        for ch in choosenword:
            if ch in guesses:
                print(ch,end=" ")
            else:
                print("_",end=" ")
                won=False

        if won:
            print("\nYou won!!")
            print(f"Your score is: {chances*10}")
            playagain()
            break

        guess = input("\nGuess a character:")  
        guesses += guess

        if guess not in choosenword:
            chances-=1
            print("\nWrong answer!!")
            print(f"You have {chances} chances left!!")

            if chances==0:
                print("You lose!!")
                playagain()
                break

print("\nThanks for playing!!")