import random


usernames = ["Andy", "Fauston", "Jerome", "Logan"] #sample usernames
members = {}
player_decks = {}
player_point = {}
case_file = {}
common_cards = []



suspects = {1: "Colonel Mustard", 2: "Miss Scarlet", 3: "Professor Plum", 4: "Mr. Green", 5: "Mrs. White", 6: "Mrs. Peacock"}
rooms = {1: "Study", 2: "Hall", 3: "Lounge", 4: "Library", 5: "Billiard Room", 6: "Dining Room", 7: "Conservatory", 8: "Ballroom", 9: "Kitchen"}
weapons = {1: "Rope", 2: "Lead Pipe", 3: "Knife", 4: "Wrench", 5: "Candlestick", 6: "Revolver"}

playerlocations = {}

case_file = {}
player_decks = {}
common_cards = []

def deal_cards():
    #initialize empty decks
    for i in range(0, len(usernames)):
        player_decks.update({usernames[i]: []})

    cards = [[suspects[x] for x in suspects],[rooms[x] for x in rooms], [weapons[x] for x in weapons]]
    
    cardslength = sum([len(sublist) for sublist in cards])
    
    num_players = len(usernames)
    excess_cards = cardslength % num_players
    cards_per_player = int((cardslength - excess_cards) / num_players)
    
    params = ["Suspect", "Room", "Weapon"]
    
    # make casefile - shuffle each sublist and take top card
    for i in range(0, 3):
        random.shuffle(cards[i])
        case_file.update({params[i]: cards[i].pop(0)})
    
    cards = [card for sublist in cards for card in sublist] #flatten cards
    random.shuffle(cards) #shuffle all together
    
    #distribute cards to players
    for i in range(0, num_players):
        for j in range(1, cards_per_player):
            player_decks[usernames[i]].append(cards.pop(0))
            
    global common_cards
    common_cards= cards.copy()

deal_cards()
print(case_file)
print(player_decks)
print(common_cards)