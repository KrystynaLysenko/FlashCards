class Card:
    
    def __init__(self, front, back):
        self.front = front
        self.back = back
        
    def get_front(self):
        return self.front
    
    def get_back(self):
        return self.back