import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from cards import Cards


class App(ctk.CTk):
 
    def __init__(self) -> None:
        self.cards = Cards()
        self.cards_iterator = self.cards.__iter__()
        self.frames = []
        self.root = ctk.CTk()
        self.root.title("FlashCards")
        self.root.minsize(400, 320)
        self.corner_radius = 3
        self.draw_home_screen()
        # ctk.set_appearance_mode("dark")
        self.root.mainloop()
        
        
    def create_popup(self, win_title, message):
        popup = tk.Toplevel()
        popup.title(win_title)
        label = tk.Label(popup, text=message)
        label.pack(pady=20, padx=20)
        button = tk.Button(popup, text="Close", command=popup.destroy)
        button.pack(pady=10) 
        
   
    
    def draw_home_screen(self):
        # Draws a new home frame
        if self.frames:
            self.frames[-1].destroy()
        self.home_frame = ctk.CTkFrame(self.root)
        self.home_frame.grid(sticky="nsew")
        
        # Draws logo and 2 buttons: "Start Learning" and "Add Card"
        title = ctk.CTkLabel(self.home_frame, text="FlashLearn", font=('Roboto', 60))
        title.grid(column=0, columnspan=2, row=0, pady=120, padx=200, sticky="nsew")
            
        start_btn = ctk.CTkButton(self.home_frame, text="Start learning", corner_radius=self.corner_radius, command=self.draw_learn_screen)
        start_btn.grid(column=0, row=4, pady=20)
        # have to implement add cards functionality
        add_card_btn = ctk.CTkButton(self.home_frame, text="Add new card", corner_radius=self.corner_radius, command=self.draw_add_screen)
        add_card_btn.grid(column=1, row=4, pady=20)
        # Updates a list of frames
        # self.frames.update(self.home_frame)
        self.frames.append(self.home_frame)
        
        
    def draw_add_screen(self):
        self.frames[-1].destroy()
        self.add_frame = ctk.CTkFrame(self.root)
        self.add_frame.grid(sticky="swen")
        
        
        label_front = ctk.CTkLabel(self.add_frame, text='Enter text on the front side:', font=('Roboto', 20))
        label_front.grid(padx=50, columnspan=2, pady=10)
        entry_front = ctk.CTkEntry(self.add_frame)
        entry_front.grid(pady=10, columnspan=2)
        
        label_back = ctk.CTkLabel(self.add_frame, text='Enter text on the back side:', font=('Roboto', 20))
        label_back.grid(padx=50, columnspan=2, pady=10)
        entry_back = ctk.CTkEntry(self.add_frame)
        entry_back.grid(pady=10, columnspan=2)
        
        def add_card():
            self.cards.add_card(entry_front.get(), entry_back.get())
            self.add_frame.destroy()
            self.create_popup("Success", "New card added!")
            self.draw_add_screen()
        
        add_btn = ctk.CTkButton(self.add_frame, text="Add", command=add_card)
        add_btn.grid(column=0, pady=50, row=6)
        cancel_btn = ctk.CTkButton(self.add_frame, text="Cancel", command=self.draw_home_screen)
        cancel_btn.grid(column=1, pady=50, row=6)
        self.frames.append(self.add_frame)
        
    
    def draw_learn_screen(self):
        self.current_card = next(self.cards_iterator)
        self.previous_card = None
        self.frames[-1].destroy()
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
        self.frames.append(self.learn_frame)
        


if __name__ == "__main__":
    app = App()