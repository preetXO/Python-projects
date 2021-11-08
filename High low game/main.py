from game_data import data
import random
from art import logo, vs
from replit import clear

#Generates random options, which can be used to play the game
def generate_options(n  = 1):
  if n == 1:
    return random.choice(data)
  else:
    return [random.choice(data) for i in range(n)]
  
#def shuffle():

#a function to compare both the options
def compare(user, opt1, opt2):
  #if use chose option a and he was right then:
  if user == 'a' and (opt1['follower_count'] > opt2['follower_count']):
    return True
  #else if user chose b and was right then:
  elif user == 'b' and (opt2['follower_count'] > opt1['follower_count']):
    return True
  #if he was incorrect then smiply return false
  else:
    return False

score = 0

def update_score():
  global score
  score += 1
  return " "
# a function that is sed to play the game using above two functions
opt1 = generate_options()
opt2 = generate_options()
continue_game = True
print(logo)
while continue_game and score < len(data):
  # this below line is for testing purpose if A is bigger then b it prints true
  #print("test: ", opt1['follower_count'] > opt2['follower_count']
  print(f"Compare A: {opt1['name']}, a {opt1['description']} from {opt1['country']}")
  print(vs)
  print(f"Compare B: {opt2['name']}, a {opt2['description']} from {opt2['country']}")
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if compare(choice, opt1, opt2):
    update_score()

    opt1 = random.choice([opt1, opt2])
    opt2 = generate_options()
    clear()
    print(logo)
    print(f"You're right! current score: {score}")
  else:
    continue_game = False
    clear()
if score == len(data):
    print(f"😯😯Are you a human? wha---, you got the maximum score {score}")
else:
  print(f"😥 your winning streak just got ended")
  print(f"Your score: {score}")
