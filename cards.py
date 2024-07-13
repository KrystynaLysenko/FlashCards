import json

class Card:
    
    def __init__(self, value, next_card=None, prev_card=None):
        self.value=value
        self.next_card = next_card
        self.prev_card = prev_card
        
    def get_value(self):
        return self.value
    
    def get_front_value(self):
        return self.value[0]
    
    def get_back_value(self):
        return self.value[1]
    
    def get_next_card(self):
        return self.next_card
    
    def get_prev_card(self):
        return self.prev_card
    
    def set_value(self):
        pass
    
    def set_next_card(self, next_card):
        self.next_card = next_card
        
    def set_prev_card(self, prev_card):
        self.prev_card = prev_card
        
        

class CardList:
    
    def __init__(self) -> None:
        self.first_card = None
        self.last_card = None
        self.current_card = self.first_card
        
        
    def set_first_card(self, new_first_card):
        self.first_card = new_first_card
        
        
    def get_first_card(self):
        return self.first_card
    
    
    def set_last_card(self, new_last_card):
        self.last_card = new_last_card
        
        
    def get_last_card(self):
        return self.last_card
    
    
    def add_to_beginning(self, value_to_add):
        new_card = Card(value_to_add)
        current_card = self.first_card
        
        if current_card is not None:
            self.first_card = new_card
            current_card.set_prev_card(new_card)
            new_card.set_next_card(current_card)
            
        self.first_card = new_card
        
        if self.last_card is None:
            self.last_card = new_card
            
            
    def add_to_end(self, value_to_add):
        new_card = Card(value_to_add)
        current_card = self.last_card
        
        if current_card is not None:
            current_card.set_next_card(new_card)
            new_card.set_prev_card(current_card)
        
        self.last_card = new_card
        
        if self.first_card is None:
            self.first_card = new_card
            
    
    def traverse_forward(self):
        if self.current_card is None:
            self.current_card = self.first_card
        else:
            self.current_card = self.current_card.get_next_card()
        print("Current card is: " + str(self.current_card))   
        return self.current_card
            
            
    def traverse_backward(self):
        if self.current_card is None:
            self.current_card = self.last_card
        else:
            self.current_card = self.current_card.get_prev_card()
        print("Current card is: " + str(self.current_card))
        return self.current_card
            
            
    def load_cards(self):
        with open('cards.json', 'r') as card_file:
            self.card_dict = json.load(card_file)
        for key in self.card_dict:
            self.add_to_end((key, self.card_dict[key]))
            
     
    # This method does not work!!!
    def stringify_all_cards(self):
        card_string = ""
        while self.current_card:
            self.traverse_forward()
            card_string += str(self.current_card.get_value()) + "\n"
        
        return card_string