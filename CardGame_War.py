from random import shuffle
# splitting the suites and cards lists into singles
SUITE = "H D S C".split()
CARDS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

# list comprehension, tupil for loop for 2 parameters, Putting s for SUITES and c for CARDS
# mycards = [(s,c) for s SUITE for c in CARDS]

# Same thing as:
# mycards = []
# for c in CARDS:
#     for s in SUITE:
#         mycards.append((s,c))


class Deck:
    def __init__(self):
        print("creating new deck")
        # list comprehension example above:
        self.allcards = [(s,c) for s in SUITE for c in CARDS] 

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        # from before 26 to after 26
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        

    def still_has_cards(self):
        return len(self.hand.cards) != 0

##############
####PLAY######
##############

print("Welcome to War! Let's begin...")

d = Deck()
d.shuffle()

# tupil unpacking:
half1,half2 = d.split_in_half()

# Create both players!
comp = Player("Computer", Hand(half1))

name = input("What is your name?:  ")
user = Player(name,Hand(half2))

# Auto Play
total_rounds = 0 
war_count = 0

#while both the computer and user have cards continue to draw/play:
while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")

    # turning the number of cards into a string and outputting the length
    print(user.name+ "has the count: "+str(len(user.hand.cards)))
    print(comp.name+ "has the count: "+str(len(comp.hand.cards)))
    print("Play a card!")
    print("\n")

    # ---------------
    # logic for showing and checking the users/computers cards
    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    # indexing 1 becuase 0 = suites, and 1 = cards, which is what we want to compare
    if c_card[1] == p_card[1]:
        war_count += 1

        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if CARDS.index(c_card[1]) < CARDS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if CARDS.index(c_card[1]) < CARDS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over, number of rounds:"+str(total_rounds))
print("a war happend "+str(war_count)+" times")
print("Computer has cards? : "+ str(comp.still_has_cards()))
print("Human Player has cards? : "+ str(user.still_has_cards()).format(name))
# if(str(comp.still_has_cards())) == False:
#     print("Computer has won!")
# else:
#     print("{} has won!".format(name))

