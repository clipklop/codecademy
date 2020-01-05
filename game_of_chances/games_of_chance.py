import random

money = 100

#Write your game of chance functions here
def can_bet(bet, money):
  return bet if bet <= money else "Not enough money"

def withdraw(bet):
  global money
  if type(can_bet(bet, money)) == int:
    money -= bet
    return money
  else:
    print('Not enough money')

def add(bet):
  global money
  money += bet
  return money

def count_roll(guess, rnd, bet):
  print("You picked {} and betted {}$. Meanwhile I flipped for {}".format(guess, bet, rnd))  
  if guess == rnd:
    add(bet)
    print("***")
    print("Gratz you've won. Your current balance is {}$".format(money))
    print("***")
  else:
    withdraw(bet)
    print("***")
    print("Soz you lose. Your current balance is {}$".format(money))
    print("***")

def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


def flip_coin(bet, side):
  sides = ["Heads", "Tails"]
  rnd = random.choice(sides)
  
  count_roll(side, rnd, bet)


def cho_han(guess, bet):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  sum_dice = dice1 + dice2
  rnd = even_odd(sum_dice)
  
  count_roll(guess, rnd, bet)


def two_cards(guess, bet):
  card1 = random.randint(2, 21)
  card2 = random.randint(2, 21)
  player1 = print("Player 1 picks {}".format(card1))
  player2 = print("Player 2 picks {}".format(card2))

  rnd = (card1, "Player 1") if card1 > card2 else (card2, "Player 2") if card2 > card1 else 0
  
  if rnd == 0:
      print("Wow! It's a tie!")
      return
  
  count_roll(guess, rnd[1], bet)


def roulette(bet, guess_color='', guess_group='', guess_number=''):
    wheel = list(range(0, 37))
    range1 = [
        [(x, "Black") if x % 2 == 0 else (x, "Red") for x in wheel[0:11]+wheel[19:29]]
    ]
    range2 = [
        [(x, "Red") if x % 2 == 0 else (x, "Black") for x in wheel[11:19]+wheel[29:37]]
    ]
    
    layout = range1[0][:10]+range2[0][:8]+range1[0][10:21]+range2[0][8:]
    layout[0] = (0, "Green")
    
    ball = random.choice(layout)
    evenodd = even_odd(ball[0])
    
    # ball = (6, "Green") # for checking number guess

    if guess_number == ball[0]:
        print("Wow, what a luck! You've guessed a number {}! $$$".format(ball[0]))
        bet *= 35
        add(bet)
        print("Your current balance is {}$".format(money))
        return True
    elif guess_color == "Green" and guess_color == ball[1]:
        print("Wow, what a luck! You've guessed a 'Green' slot! $$$")
        bet *= 35
        add(bet)
        print("Your current balance is {}$".format(money))
        return True
    elif guess_color == ball[1]:
        print("Gratz! You've guess a color!")
        add(bet)
        print("Your current balance is {}$".format(money))
        return True
    elif guess_group == evenodd:
        print("Nice! You've guessed an {} number!".format(evenodd))
        add(bet)
        print("Your current balance is {}$".format(money))
        return True
    else:
        print("Oh, no! You lose. Come again next time...")
        withdraw(bet)
        print("Your current balance is {}$".format(money))
        return False


    # add(bet)
    # withdraw(bet)
    # print(len([x[1] for x in layout]))
    print(ball)
    return


#Call your game of chance functions here
# roulette(20, guess_color='Black')
# roulette(20, guess_group='Even')
roulette(20, guess_number=6)

# two_cards("Player 1", 20)
# two_cards("Player 1", 20)
# two_cards("Player 1", 20)
# two_cards("Player 1", 20)
# two_cards("Player 1", 20)
# two_cards("Player 1", 20)
# two_cards("Player 1", 20)

# cho_han("Even", 15)
# cho_han("Even", 15)
# cho_han("Even", 15)
# cho_han("Even", 15)
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Tails')
# flip_coin(10, 'Heads')
# flip_coin(10, 'Tails')
