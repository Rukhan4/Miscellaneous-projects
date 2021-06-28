import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

playing = True

# A SIMPLE CARD CLASS, WITH RESPECT TO A STANDARD DECK OF CARDS (ONE CARD)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

# A STANDARD DECK OF 52 PLAYING CARDS IS GENERATED AND SHUFFLED IN LINE


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# INITIALIZES THE HAND THAT THE PLAYER AND DEALER RECEIVE
# CONTAINS THE ADJUST_FOR_ACE FUNCTION TO ACCOMODATE AN ACE BEING 1 OR 11 DEPENDING ON WHICH BENEFITS THE PLAYERS


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# ASSESSES THE INITIAL VALUE OF 100 CHIPS FOR THE PLAYER AND ADJUSTS ACCORDING TO IF THEY WIN OR LOSE


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """[summary: function for the total amount of chips a player
    starts with. It is initialized to 100 each round]

    Args:
        chips ([integer]): [accepts how much the player chooses to bet
        in a predefined range]
    """
    while True:
        try:
            chips.bet = int(input("Please place your bet:"))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet cannot exceed", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """decides whether a player wants to hit or stand

    Args:
        deck ([list]): [52 playing cards in a standard deck]
        hand ([class]): [the cards a player currently holds]
    """

    global playing 

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")

        if x[0].lower() == "h":
            hit(deck, hand)

        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing...")
            playing = False

        else:
            print("Please try again")
            continue
        break

# SHOWING EITHER SOME OR ALL OF THE PLAYER AND DEALER'S CARDS WITH RESPECT TO THE POINT OF THE GAME


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card_hidden> ")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


# WIN OR LOSE SCENARIOS


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push!")


# GAME STARTS

while True:

    print('\n')
    print('\n')
    print(
        "Welcome to BlackJack! Get as close to 21 as you can without going over, else you BUST!"
    )
    print(
        "Dealer hits until they beat the player or bust. Aces count as 1 or 11, depending on which benefit either side"
    )

    # CREATE AND SHUFFLE THE DECK
    deck = Deck()
    deck.shuffle()

    # INITIALIZES THE PLAYER'S 2 DEALT CARDS AT RANDOM
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # INITIALIZES THE DEALER'S 2 DEALT CARDS AT RANDOM
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # SET UP THE PLAYER'S CHIPS --EVERY SUCCESSIVE ROUND, THE PLAYER STARTS WITH 100 CHIPS AND THEIR PREVIOUS WIN/LOSS, CANNOT GO TO 0
    player_chips = Chips()

    # ASK FOR THE PLAYER'S BET
    take_bet(player_chips)

    # SHOWS CARDS, BUT KEEPS 1 OF THE DEALER'S CARDS HIDDEN
    show_some(player_hand, dealer_hand)

    while playing:  

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # SHOWS CARDS, BUT KEEPS 1 OF THE DEALER'S CARDS HIDDEN
        show_some(player_hand, dealer_hand)

        # IF PLAYER HAND > 21, BUST
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # IF PLAYER HAS NOT BUSTED, RUNS WHILE THE DEALER'S HAND IS LESS THAN THE PLAYER HAND'S VALUE TO TRY AND BEAT THE PLAYER
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # SHOW ALL CARDS
        show_all(player_hand, dealer_hand)

        # ALL THE DIFFERENT OUTCOMES
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # INFORM THE PLAYER OF THE AMOUNT OF CHIPS THEY HAVE
    print("\nPlayer's total stands at:", player_chips.total)

    # ASK TO PLAY AGAIN
    new_game = input("Would you like to play another hand? Enter 'y' or 'n'")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
