import json
from card import Card

class Cards:
    
    def __init__(self) -> None:
        self.cards = []
        self.load_cards()
        

    def load_cards(self):
        with open('cards.json', 'r') as cards_file:
            cards = json.load(cards_file)
        for key in cards.keys():
            # print(f"Key: {key}, Value: {cards[key]}") 
            new_card = Card(key, cards[key])
            self.cards.append(new_card)


    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        self.index += 1
        if self.index > len(self.cards):
            raise StopIteration
        return self.cards[self.index - 1]
    
    def __len__(self):
        return len(self.cards)
    
    # Not functional, need to come up with better solution, maybe nodes
    def __previous__(self):
        self.index -=1
        return self

        
        
        

