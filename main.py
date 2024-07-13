import tkinter as tk
import customtkinter as ctk

from cards import CardList

FG_COLOR = "#37474F"
FG_TEXT = "#D8ECC3"

BTN_DARK = "#4CAF50"
BTN_DARK_HOVER = "#388E3C"
BTN_DARK_TEXT = "#FFFFFF"

BTN_LIGHT = "#D8ECC3"
BTN_LIGHT_TEXT = "#37474F"
BTN_LIGHT_HOVER = "#C1E5B8"


class App(ctk.CTk):
 
    def __init__(self) -> None:
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
        self.home_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR, corner_radius=0)
        self.home_frame.grid(sticky="swen")
        
        # Draws logo and 2 buttons: "Start Learning" and "Add Card"
        title = ctk.CTkLabel(self.home_frame, text="FlashLearn", font=('Roboto', 60), text_color=FG_TEXT)
        title.grid(column=0, columnspan=2, row=0, pady=120, padx=200, sticky="nsew")
            
        start_btn = ctk.CTkButton(self.home_frame, text="Start learning", corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.draw_learn_screen)
        start_btn.grid(column=0, row=4, pady=20)
        # have to implement add cards functionality
        add_card_btn = ctk.CTkButton(self.home_frame, text="Add new card", corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.draw_add_screen)
        add_card_btn.grid(column=1, row=4, pady=20)
        # Updates a list of frames
        # self.frames.update(self.home_frame)
        self.frames.append(self.home_frame)
        
        
    def draw_add_screen(self):
        self.frames[-1].destroy()
        self.add_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR)
        self.add_frame.grid(sticky="swen")
        
        
        label_front = ctk.CTkLabel(self.add_frame, text='Enter text on the front side:', font=('Roboto', 20), text_color=FG_TEXT)
        label_front.grid(padx=50, columnspan=2, pady=10)
        entry_front = ctk.CTkEntry(self.add_frame)
        entry_front.grid(pady=10, columnspan=2)
        
        label_back = ctk.CTkLabel(self.add_frame, text='Enter text on the back side:', font=('Roboto', 20), text_color=FG_TEXT)
        label_back.grid(padx=50, columnspan=2, pady=10)
        entry_back = ctk.CTkEntry(self.add_frame)
        entry_back.grid(pady=10, columnspan=2)
        
        def add_card():
            # self.cards.add_card(entry_front.get(), entry_back.get())
            # self.add_frame.destroy()
            # self.create_popup("Success", "New card added!")
            # self.draw_add_screen()
            pass
        
        add_btn = ctk.CTkButton(self.add_frame, text="Add", command=add_card, corner_radius= self.corner_radius)
        add_btn.grid(column=0, pady=50, row=6, padx=20)
        cancel_btn = ctk.CTkButton(self.add_frame, text="Cancel", command=self.draw_home_screen, corner_radius= self.corner_radius)
        cancel_btn.grid(column=1, pady=50, row=6, padx=20)
        self.frames.append(self.add_frame)
        
    
    def draw_learn_screen(self):
        self.frames[-1].destroy()
        self.learn_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR, corner_radius=0)
        self.learn_frame.grid(sticky="swen")
        
        # Create new card list and load cards from .json file
        self.card_list = CardList()
        self.card_list.load_cards()
        self.current_card = self.card_list.traverse_forward()
        
        self.side_label = ctk.CTkLabel(self.learn_frame, text="Word:", font=('CTkFont', 20), text_color=FG_TEXT)
        self.side_label.grid(column=1, pady=10, columnspan=3)
        
        self.card_label = ctk.CTkLabel(self.learn_frame, text=self.current_card.get_front_value(), font=('CTkFont', 30), text_color=FG_TEXT)
        self.card_label.grid(column=1, pady=130, rowspan=6, columnspan=3)
                
        def next_card():
            self.current_card = self.card_list.traverse_forward()
            self.card_label.configure(text=self.current_card.get_front_value())
            self.prev_btn.configure(state='normal')
            if self.current_card.get_next_card() is None:
                self.next_btn.configure(state='disabled')
            reset_flip_btn_and_label()
            
            
        def prev_card():
            self.current_card = self.card_list.traverse_backward()
            self.card_label.configure(text=self.current_card.get_front_value())
            self.next_btn.configure(state='normal')
            if self.current_card.get_prev_card() is None:
                self.prev_btn.configure(state='disabled')
            reset_flip_btn_and_label()
                
        def flip_card():
            self.side_label.configure(text='Translation:')
            self.card_label.configure(text=self.current_card.get_back_value())
            def unflip():
                self.card_label.configure(text=self.current_card.get_front_value())
                reset_flip_btn_and_label() 
            self.flip_btn.configure(text="Unflip", command=unflip)
            
        def reset_flip_btn_and_label():
            self.flip_btn.configure(text="Flip", command=flip_card)
            self.side_label.configure(text="Word:")
            
            
        self.flip_btn = ctk.CTkButton(self.learn_frame, text="Flip", corner_radius=self.corner_radius, fg_color=BTN_LIGHT, hover_color=BTN_LIGHT_HOVER, text_color='black', command=flip_card)
        self.flip_btn.grid(columnspan=1, column=2, row=6, padx=50)
        
        self.next_btn = ctk.CTkButton(self.learn_frame, text='Next', corner_radius= self.corner_radius, fg_color=BTN_DARK, command=next_card)
        self.next_btn.grid(pady=15, padx=10, column=3, row=6)
        
        self.prev_btn = ctk.CTkButton(self.learn_frame, text='Previous', corner_radius= self.corner_radius, state='disabled', fg_color=BTN_DARK, command=prev_card)
        self.prev_btn.grid(pady=10, padx=10, column=1, row=6)
        self.frames.append(self.learn_frame)
        


if __name__ == "__main__":
    app = App()