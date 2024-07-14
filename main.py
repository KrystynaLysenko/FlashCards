import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

from cards import CardList

FG_COLOR = "#37474F"
FG_TEXT = "#D8ECC3"

BTN_DARK = "#4CAF50"
BTN_DARK_HOVER = "#388E3C"
BTN_DARK_TEXT = "#FFFFFF"

BTN_LIGHT = "#D8ECC3"
BTN_LIGHT_TEXT = "#37474F"
BTN_LIGHT_HOVER = "#C1E5B8"

BTN_FONT= ('CTkFont', 20)


class App(ctk.CTk):
 
    def __init__(self) -> None:
        self.frames = []
        self.root = ctk.CTk()
        self.root.title("FlashCards")
        self.root.minsize(800, 640)
        self.root.maxsize(800, 640)
        self.root.resizable(False, False)
        self.corner_radius = 15
        self.draw_home_screen()
        
        self.root.grid_rowconfigure(0, weight=200)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create new card list and load cards from .json file
        self.card_list = CardList()
        self.card_list.load_cards()
        # self.current_card = self.card_list.get_first_card()
        
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
        img=Image.open('assets/logo.png')
        photo_img = ctk.CTkImage(light_image=img, dark_image=img, size=(img.width, img.height))
        title = ctk.CTkLabel(self.home_frame, image=photo_img, text="", font=('Roboto', 60), text_color=FG_TEXT)
        title.grid(column=0, columnspan=2, row=1, pady=20, padx=100, sticky="nsew")
            
        start_btn = ctk.CTkButton(self.home_frame, text="START LEARNING", font=BTN_FONT, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.draw_learn_screen, height=50, width=200)
        start_btn.grid(column=0, row=4, pady=20)
        
        view_btn = ctk.CTkButton(self.home_frame, text="VIEW CARDS", font=BTN_FONT, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.view_cards_screen, height=50, width=200)
        view_btn.grid(column=0, row=5, pady=20)
        # have to implement add cards functionality
        add_card_btn = ctk.CTkButton(self.home_frame, text="ADD NEW CARD", font=BTN_FONT, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.draw_add_screen, height=50, width=200)
        add_card_btn.grid(column=1, row=4, pady=20)
        
        exit_btn = ctk.CTkButton(self.home_frame, text="EXIT", font=BTN_FONT, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=exit, height=50, width=200)
        exit_btn.grid(column=1, row=5, pady=20)
        # Updates a list of frames
        # self.frames.update(self.home_frame)
        self.frames.append(self.home_frame)
        
        
    def view_cards_screen(self):
        # Destroy the last frame
        self.frames[-1].destroy()

        # Create a new frame to hold the scrollable frame
        self.view_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR, corner_radius=0, width=800, height=640)
        self.view_frame.grid(sticky='nsew')
        self.frames.append(self.view_frame)

        # Configure the grid layout for the view frame
        self.view_frame.grid_rowconfigure(0, weight=1)
        self.view_frame.grid_columnconfigure(0, weight=1)

        # Create a scrollable frame inside the view frame
        scroll_frame = ctk.CTkScrollableFrame(self.view_frame, corner_radius=0, fg_color=FG_COLOR)
        scroll_frame.grid(row=0, column=0, sticky='nsew')
        
        current_card = self.card_list.get_first_card()

        # Add cards to the scrollable frame
        row = 0
        while current_card is not None:
            ctk.CTkLabel(
                scroll_frame, 
                text=f'{current_card.get_front_value()} - {current_card.get_back_value()}', 
                font=(ctk.CTkFont, 30), 
                text_color=FG_TEXT,
                
            ).grid(row=row, pady=10, padx=300)
            current_card = current_card.get_next_card()
            row += 1
            
        home_btn = ctk.CTkButton(self.view_frame, text="HOME", font=BTN_FONT, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=self.draw_home_screen)
        home_btn.grid(column=0, row=5, pady=20)
            
        
        
    def draw_add_screen(self):
        self.frames[-1].destroy()
        self.add_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR)
        self.add_frame.grid(sticky="nsew")
        
        
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
        
        add_btn = ctk.CTkButton(self.add_frame, text="Add", font=BTN_FONT, command=add_card, corner_radius=self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER)
        add_btn.grid(column=0, pady=50, row=6, padx=20)
        
        cancel_btn = ctk.CTkButton(self.add_frame, text="Cancel", font=BTN_FONT, command=self.draw_home_screen, corner_radius= self.corner_radius, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER)
        cancel_btn.grid(column=1, pady=50, row=6, padx=20)
        self.frames.append(self.add_frame)
        
    
    def draw_learn_screen(self):
        self.frames[-1].destroy()
        self.learn_frame = ctk.CTkFrame(self.root, fg_color=FG_COLOR, corner_radius=0, width=800, height=640)
        self.learn_frame.grid(sticky="nsew")
        
        # Create new card list and load cards from .json file
        self.card_list = CardList()
        self.card_list.load_cards()
        self.current_card = self.card_list.get_first_card()
        
        self.home_btn = ctk.CTkButton(self.learn_frame, text='HOME', corner_radius=self.corner_radius, font=BTN_FONT, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, width=60, command=self.draw_home_screen)
        self.home_btn.grid(row=0, column=2)
        
        self.side_label = ctk.CTkLabel(self.learn_frame, text="Word:", font=BTN_FONT, text_color=FG_TEXT)
        self.side_label.grid(column=0, pady=10, columnspan=3, row=0)
        
        self.card_frame = ctk.CTkFrame(self.learn_frame, fg_color=BTN_LIGHT, bg_color=FG_COLOR, corner_radius=self.corner_radius, height=300, width=400)
        self.card_frame.grid(sticky="nsew", columnspan=3, pady=20, padx=50)
        
        self.empty_image = ctk.CTkImage(Image.new('RGB', (1, 1)))
        
        self.image_label = ctk.CTkLabel(self.card_frame, image=self.empty_image, text="")
        self.image_label.size()
        self.image_label.grid(column=0, columnspan=3, rowspan=6, row=1)
        
        self.card_label = ctk.CTkLabel(self.card_frame, text=self.current_card.get_front_value(), font=('CTkFont', 30), text_color=FG_COLOR, pady=10, padx=10)
        self.card_label.grid(column=0, rowspan=6, columnspan=3, row=1, pady=200, padx=300)
        
        flip_img = Image.open('assets/flip.png')
        photo_flip_img = ctk.CTkImage(light_image=flip_img, dark_image=flip_img, size=(flip_img.width, flip_img.height))
        
        next_img = Image.open('assets/next.png')
        photo_next_img = ctk.CTkImage(light_image=next_img, dark_image=next_img, size=(next_img.width, next_img.height))
        
        prev_img = Image.open('assets/prev.png')
        photo_prev_img = ctk.CTkImage(light_image=prev_img, dark_image=prev_img, size=(prev_img.width, prev_img.height))
        
                
        def next_card():
            self.current_card=self.current_card.get_next_card()
            self.card_label.configure(text=self.current_card.get_front_value())
            self.prev_btn.configure(state='normal', fg_color=BTN_DARK)
            if self.current_card.get_next_card() is None:
                self.next_btn.configure(state='disabled', fg_color='grey')
            reset_flip_btn_and_label()
            
            
        def prev_card():
            self.current_card = self.current_card.get_prev_card()
            self.card_label.configure(text=self.current_card.get_front_value())
            self.next_btn.configure(state='normal', fg_color=BTN_DARK)
            if self.current_card.get_prev_card() is None:
                self.prev_btn.configure(state='disabled', fg_color='grey')
            reset_flip_btn_and_label()
                
        def flip_card():
            self.side_label.configure(text='Translation:')
            self.card_label.configure(text=self.current_card.get_back_value(), font=(ctk.CTkFont, 30, "bold"))
            self.image_label.configure(image=show_image())
            def unflip():
                self.card_label.configure(text=self.current_card.get_front_value(), font=('CTkFont', 30))
                reset_flip_btn_and_label()
            self.flip_btn.configure(command=unflip)
            
        def reset_flip_btn_and_label():
            self.side_label.configure(text="Word:")
            self.image_label.configure(image=self.empty_image)
            self.flip_btn.configure(command=flip_card)
            
        def show_image():
            image_url = self.current_card.get_img_path()
            try:
                img=Image.open(image_url)
                # img= img.resize((300, 225))
                photo_img = ctk.CTkImage(light_image=img, dark_image=img, size=(img.width, img.height))
            except Exception as e:
                print(e)
                return self.empty_image
           
            return photo_img
                
                
            
        self.prev_btn = ctk.CTkButton(self.learn_frame, image=photo_prev_img, text="", corner_radius= self.corner_radius, font=BTN_FONT, state='disabled', fg_color='grey', hover_color=BTN_DARK_HOVER, command=prev_card)
        self.prev_btn.grid(pady=10, padx=15, column=0, row=10)
        
            
        self.flip_btn = ctk.CTkButton(self.learn_frame, image=photo_flip_img, text="", corner_radius=self.corner_radius, font=BTN_FONT, fg_color=BTN_LIGHT, hover_color=BTN_LIGHT_HOVER, text_color='black', command=flip_card)
        self.flip_btn.grid(columnspan=1, column=1, row=10)
        
        self.next_btn = ctk.CTkButton(self.learn_frame, image=photo_next_img, text="", corner_radius= self.corner_radius, font=BTN_FONT, fg_color=BTN_DARK, hover_color=BTN_DARK_HOVER, command=next_card)
        self.next_btn.grid(pady=15, padx=15, column=2, row=10)
        
        self.frames.append(self.learn_frame)
        


if __name__ == "__main__":
    app = App()