import random

usernames = ["Andy", "Fauston", "Jerome", "Logan"] #sample usernames
player_decks = {}
player_location = {}
case_file = {}
common_cards = []

suspects = {1: "Colonel Mustard", 2: "Miss Scarlet", 3: "Professor Plum", 4: "Mr. Green", 5: "Mrs. White", 6: "Mrs. Peacock"}
rooms = {1: "Study", 2: "Hall", 3: "Lounge", 4: "Library", 5: "Billiard Room", 6: "Dining Room", 7: "Conservatory", 
         8: "Ballroom", 9: "Kitchen"}
weapons = {1: "Rope", 2: "Lead Pipe", 3: "Knife", 4: "Wrench", 5: "Candlestick", 6: "Revolver"}

player_characters = {usernames[0]: suspects[4], usernames[1]: suspects[1], usernames[2]: suspects[2], usernames[3]: suspects[3]}


hallways = {1: [rooms[1], rooms[2]], 
           2: [rooms[2], rooms[3]], 
           3: [rooms[1], rooms[4]], 
           4: [rooms[2], rooms[5]], 
           5: [rooms[3], rooms[6]], 
           6: [rooms[4], rooms[5]],
           7: [rooms[5], rooms[6]],
           8: [rooms[4], rooms[7]], 
           9: [rooms[5], rooms[8]], 
           10: [rooms[6], rooms[9]],
           11: [rooms[7], rooms[8]], 
           12: [rooms[8], rooms[9]]}

room_connections = {rooms[1]: [hallways[1], hallways[3], rooms[9]],
                    rooms[2]: [hallways[1], hallways[2], hallways[4]], 
                    rooms[3]: [hallways[2], hallways[5], rooms[7]], 
                    rooms[4]: [hallways[3], hallways[6], hallways[8]],
                    rooms[5]: [hallways[4], hallways[6], hallways[7], hallways[9]],
                    rooms[6]: [hallways[5], hallways[7], hallways[10]],
                    rooms[7]: [hallways[8], hallways[11], rooms[3]],
                    rooms[8]: [hallways[9], hallways[11], hallways[12]], 
                    rooms[9]: [hallways[10], hallways[12], rooms[1]],
                   }


suspect_start_location = {suspects[1]: hallways[5], suspects[2]: hallways[2], suspects[3]: hallways[3],
                         suspects[4]: hallways[11], suspects[5]: hallways[12], suspects[6]: hallways[8]}

gameboard = {rooms[1]: [rooms[2], rooms[3]]}

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
    
    common_cards= cards.copy()
    return player_decks, common_cards, case_file

def initialize_game():
    global player_decks, common_cards, case_file, player_location
    player_decks, common_cards, case_file = deal_cards()
    
    for username, character in player_characters.items():
        player_location.update({username: suspect_start_location[character]})
        
def main_game():
    initialize_game()
    #while player hasn't won:
        #next players turn

print(map)
