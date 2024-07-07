import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from cards import Cards


class App(ctk.CTk):
 
    def __init__(self) -> None:
        cards = Cards()
        self.cards_iterator = cards.__iter__()
        self.frames = {}
        self.root = ctk.CTk()
        self.root.minsize(400, 320)
        self.corner_radius = 3
        self.draw_home_screen()
        # ctk.set_appearance_mode("dark")
        self.root.mainloop()
        
        
   
    
    def draw_home_screen(self):
        # Draws a new home frame
        self.home_frame = ctk.CTkFrame(self.root)
        self.home_frame.grid(sticky="nsew")
        # Draws logo and 2 buttons: "Start Learning" and "Add Card"
        title = ctk.CTkLabel(self.home_frame, text="FlashLearn", font=('Roboto', 60))
        title.grid(column=0, columnspan=2, row=0, pady=120, padx=200, sticky="nsew")
        start_btn = ctk.CTkButton(self.home_frame, text="Start learning", corner_radius=self.corner_radius, command=self.draw_learn_screen)
        start_btn.grid(column=0, row=4, pady=20)
        # have to implement add cards functionality
        add_btn = ctk.CTkButton(self.home_frame, text="Add new card", corner_radius=self.corner_radius)
        add_btn.grid(column=1, row=4, pady=20)
        # Updates a list of frames
        self.frames.update(self.home_frame)
    
    def draw_learn_screen(self):
        self.current_card = next(self.cards_iterator)
        self.previous_card = None
        self.home_frame.destroy()
        self.learn_frame = ctk.CTkFrame(self.root)
        self.learn_frame.grid(sticky="swen")
        
        self.side_label = ctk.CTkLabel(self.learn_frame, text="", font=('CTkFont', 20))
        self.side_label.grid(column=1, pady=10)
        
        self.card_label = ctk.CTkLabel(self.learn_frame, text=self.current_card.get_front(), font=('CTkFont', 30))
        self.card_label.grid(column=1, pady=130, rowspan=6, columnspan=3)
                
        def next_card():
            self.previous_card = self.current_card
            self.current_card = next(self.cards_iterator)
            self.side_label.configure(text='')
            self.card_label.configure(text=self.current_card.get_front())
            self.previous_btn.configure(state='normal', fg_color='red')
        
        def previous_card():
            self.current_card = self.previous_card
            self.previous_btn.configure(state='disabled', fg_color='grey') 
            self.card_label.configure(text=self.previous_card.get_front()) 
                

        def flip_card():
            flipped_text = self.current_card.get_back()
            self.card_label.configure(text=flipped_text)
            self.side_label.configure(text='Translation:')
            
        flip_btn = ctk.CTkButton(self.learn_frame, text="Flip", corner_radius= self.corner_radius, fg_color='yellow', text_color='black', command=flip_card)
        flip_btn.grid(columnspan=1, column=2, row=6, padx=50)
        
        next_btn = ctk.CTkButton(self.learn_frame, text='Next', corner_radius= self.corner_radius, command=next_card)
        next_btn.grid(pady=15, padx=10, column=3, row=6)
        
        self.previous_btn = ctk.CTkButton(self.learn_frame, text='Previous', corner_radius= self.corner_radius, state='disabled', fg_color='grey', command=previous_card)
        self.previous_btn.grid(pady=10, padx=10, column=1, row=6)
        


if __name__ == "__main__":
    app = App()