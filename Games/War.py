
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# CREATING THE CARDS CLASS


class Card:
    """[summary: creates the Card class which 
    initializes the attributes of a standard deck
    of cards which are the suits, ranks and values]
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# CREATING THE DECK CLASS


class Deck:
    """[summary: creates the Deck class for all 52
    cards in a standard deck and shuffling them. The 
    class further deals one card to the player]
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create cards
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffledeck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# CREATING THE PLAYER CLASS


class Player:
    """[summary: creates the Player class containing
    functions for removing or adding a card]
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} is the war chief!"


# GAMEPLAY

# INPUT THE NAMES OF THE PLAYERS


player_one = Player(input("Who is player 1?:"))
player_two = Player(input("Who is player 2?:"))

# SHUFFLE THE DECK FOR A NEW GAME

new_deck = Deck()
new_deck.shuffledeck()

# SPLIT THE DECK BETWEEN EACH PLAYER

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# GAME STARTS

game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One is out of cards!")
        print(f"{player_two} He wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards!")
        print(f"{player_one} He wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            # Rules of war
            print("WAR HAS BEGUN!")

            if len(player_one.all_cards) < 5:
                print("Player one cannot declare war")
                print(f"{player_two} He wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two cannot declare war")
                print(f"{player_one} He wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

# %%
