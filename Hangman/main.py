import random
from replit import clear
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Importing he logo from hangman_art.py and printing it at the start of the game.
logo = hangman_art.logo
#Testing code
#print(f'Pssst, (testing code)the solution is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"
  
print(logo)

while not end_of_game :
    guess = input("Guess a letter: ").lower()
    clear()
    #If the user has entered a letter they've already guessed, printing the letter and letting them know.
    if guess in display:
      print(f"You've already chosen {guess}, please enter a different letter")
    #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
        
    #Checking if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, printing out the letter and letting them know it's not in the word.
        lives -= 1
        print(f"You chose '{guess}' which is not in the word, You've lost one life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"Congratulations you win")
    print(hangman_art.stages[lives])