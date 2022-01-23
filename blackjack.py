import random
import time
import sys


class Card:
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit

        if self.value > 1 and self.value < 11:
            self.face = str(self.value)

        elif self.value == 1:
            self.face = "Ace"
            self.value = 11

        elif self.value == 11:
            self.face = "Jack"
            self.value = 10

        elif self.value == 12:
            self.face = "Queen"
            self.value = 10

        else:
            self.face = "King"
            self.value = 10

class Hand:
    def __init__(self, name):
        self.hand = []
        self.cnt = 0
        self.name = name
        self.draw()
        self.draw()

    def draw(self):
        self.hand.append(deck.pop(0))
        self.count()

    def count(self):
        self.cnt = 0

        for card in self.hand:
            self.cnt += card.value

        for card in self.hand:
            if self.cnt > 21:
                if card.face == "Ace":
                    if card.value == 11:
                        card.value = 1
                        self.cnt -= 10
                        break

        return self.cnt

    def show_hand(self):
        print()
        print(f"{self.name} has the following")
        for card in self.hand:
            print(card.face + " of " + card.suit)

suits = ['spades', 'clubs', 'hearts', 'diamonds']

#create deck of cards and shuffle
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
random.shuffle(deck)

dealer_hand = Hand("Dealer")
player_hand = Hand("Player")

def dealer_stays():
    print()
    print(f"Dealer has {dealer_hand.cnt}, Dealer stays")

dealer_hand.show_hand()
player_hand.show_hand()

if player_hand.cnt == 21:
    print()
    print("Blackjack!, you win!")
    sys.exit()

#player hit or stay loop
while player_hand.cnt < 21:
    choice = input("hit or stay? > ")
    if choice == "hit":
        player_hand.draw()
        player_hand.show_hand()
        print()
        print(f"Player has {player_hand.cnt}")
    elif choice == "stay":
        player_hand.show_hand()
        print()
        print(f"Player has {player_hand.cnt}")
        break
    else:
        print()
        print("That's not a valid input")

if player_hand.cnt > 21:
    print()
    print("You bust, try again!")
    sys.exit()

#dealer
while dealer_hand.cnt < 17:
    print()
    print(f"Dealer has {dealer_hand.cnt}, Dealer hits")
    time.sleep(3)
    dealer_hand.draw()
    dealer_hand.show_hand()
    time.sleep(3)

#results
if dealer_hand.cnt > 21:
    print()
    print(f"Dealer has {dealer_hand.cnt}")
    print()
    print("The Dealer busts. You win!")
    sys.exit()

if dealer_hand.cnt > player_hand.cnt:
    dealer_stays()
    print()
    print("The dealer wins this hand")
    sys.exit()

elif dealer_hand.cnt < player_hand.cnt:
    dealer_stays()
    print()
    print("You win this hand!")
    sys.exit()

else:
    dealer_stays()
    print()
    print("It's a push")
    sys.exit()
