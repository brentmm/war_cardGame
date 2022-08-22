#function to display rules
def warGame_rules():
    print("")
    print("The goal is to be the first player to win all 52 cards")
    print("")
    print("THE DEAL")
    print("")
    print(
        "The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them."
    )
    print("")
    print("THE PLAY")
    print("")
    print(
        "Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack."
    )
    print("")
    print(
        "If the cards are the same rank, it is War. Each player turns up three cards face down and one card face up. The player with the higher cards takes both piles (six cards)."
    )
    print(
        "If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on."
    )
    print("")
    print("HOW TO KEEP SCORE")
    print("")
    print("The game ends when one player has won all the cards.")
    print("")
    print("")
    print("")
  
#fucntion to shuffle card_deck
def shuffling_deck(shuffle):
    import random
    for i in range(len(shuffle)):
        NumGenerator = random.randint(0, (len(shuffle) - 1))
        shuffle[i], shuffle[NumGenerator] = shuffle[NumGenerator], shuffle[i]
    return shuffle


#spliting deck
def split_list(playerD1,playerD2):
  playerD1,playerD2 =card_deck[:len(card_deck)//2],card_deck[len(card_deck)//2:]
  return playerD1,playerD2


#assigning card values
def cardValue(card):
    card = card.split()[0]
    if card == "Ace":
      return 1
    elif card == "Two":
      return 2
    elif card == "Three":
      return 3
    elif card == "Four":
      return 4
    elif card == "Five":
      return 5
    elif card == "Six":
      return 6
    elif card == "Seven":
      return 7
    elif card == "Eight":
      return 8
    elif card == "Nine":
      return 9
    elif card == "Ten":
      return 10
    elif card == "Jack":
      return 11
    elif card == "Queen":
      return 12
    elif card == "King":
      return 13

#gameplay
def war():
  count = 0
  while len(playerD1) > 0 and len(playerD2) > 0:
      count +=1
      if cardValue(playerD1[0]) > cardValue(playerD2[0]):
        if showRounds == "yes":
          print("Player One Won The Round.")
        for i in range(len(tieDeck)):
          playerD1.append(tieDeck.pop(0))
        playerD1.append(playerD2.pop(0))
        playerD1.append(playerD1.pop(0))
      elif cardValue(playerD1[0]) < cardValue(playerD2[0]):
        if showRounds == "yes":
          print("Player Two Won The Round.")
        for i in range(len(tieDeck)):
          playerD2.append(tieDeck.pop(0))
        playerD2.append(playerD1.pop(0))
        playerD2.append(playerD2.pop(0))
      elif cardValue(playerD1[0]) == cardValue(playerD2[0]):
          if showRounds == "yes":
            print("Tie")
          if len(playerD1) > 4 and len(playerD2) > 4 : 
            for i in range(0,4):
              tieDeck.append(playerD2.pop(0))
              tieDeck.append(playerD1.pop(0))
          elif len(playerD1) == 4 or len(playerD2) == 4: 
            for i in range(0,3):
              tieDeck.append(playerD2.pop(0))
              tieDeck.append(playerD1.pop(0))
          elif len(playerD1) == 3 or len(playerD2) == 3:
            for i in range(0,2):
              tieDeck.append(playerD2.pop(0))
              tieDeck.append(playerD1.pop(0))
          elif len(playerD1) == 2 or len(playerD2) == 2:
            for i in range(0,1):
              tieDeck.append(playerD2.pop(0))
              tieDeck.append(playerD1.pop(0))
          elif len(playerD1) == 1:
              tieDeck.append(playerD1.pop(0)) 
          elif len(playerD2) == 1:
              tieDeck.append(playerD2.pop(0)) 
  return(playerD1, playerD2, count)

#anncouncing winner
def winner(playerD1, playerD2, count):
  if len(playerD2) == 0:
    print("")
    print("Player One Won The Game in " + str(count) + " rounds.")
  elif len(playerD1) == 0:
    print("")
    print("Player Two Won The Game in " + str(count) + " rounds.")

#function to quit program
def quit(action):
    print("Thanks for playing")


#intro
print("Welcome to the War Card Game Program.")
print("")
print("")
print("You can learn the rules, play the game, and quit the program.")
print("")
print(" (1) Learn The Rules \n (2) Play The Game \n (3) Quit Progam")
print("")
action = "no"
while action == "no":
    #creating list
    numberDeck = [
        'Ace ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ',
        'Nine ', 'Ten ', 'Jack ', 'Queen ', 'King '
    ]
    suitDeck = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    card_deck = []
    playerD1 = []
    playerD2 = []
    tieDeck = []

    for x in numberDeck:
        for y in suitDeck:
            card_deck.append(x + "of " + y)
    
    card_deck = shuffling_deck(card_deck)
    playerD1,playerD2 = split_list(playerD1,playerD2)

    #asking user what they want to do
    choice = input("What action would you like to preform?: ")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("What would you like to do? (Select a #) ")
        print("")

    #checking users input and steps into required function function
    showRounds = input("Would you like to see each round? (Yes or No): ").lower()

    if choice == ("1"):
        warGame_rules()
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("2"):
        count = 0
        shuffling_deck(card_deck)
        split_list(playerD1,playerD2)
        playerD1, playerD2,count = war()
        winner(playerD1, playerD2, count)
        print("")
        action = input("Would you like to quit? (yes or no): ").lower()
        if action == "yes":
          choice = "Brent"
          quit(action)
    elif choice == ("3"):
        action = input("Would you like to quit? (yes or no): ").lower()
        if action == ("yes"):
            quit(action)
            print("")
            choice = "Brent"
        else:
            choice = input("What would you like to do? (Select a #) ")

    #asking user what they wanna do if choice was not valid
        while choice != "Brent" and choice != "1" and choice != "2" and choice != "3":
            choice = input("What would you like to do? (Select a #) ")
