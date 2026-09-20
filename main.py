import tkinter as tk
import random

# ----- GAME LOGIC -----

# Gets a random choice between rock, paper, or scissors
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# ----- GRAPHICAL USER INTERFACE -----
class RockPaperScissors:
    # Tkinter initialization: creates window and other widgets
    def __init__(self):
        self.window = tk.Tk()
        self.create_user_interface()

    def create_user_interface(self):
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x200")

        self.message = tk.Label(self.window, text="Your Input:")
        self.message.pack()

        # --- Creates a frame for the buttons ---
        self.buttons_frame = tk.Frame(self.window)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock")
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper")
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors")
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        # Packs button_frame
        self.buttons_frame.pack()    

        #---Creates the frame for the result---
        self.result_frame = tk.Frame(self.window)
                    
        # Creates an empty label to be asigned later
        self.round_result = tk.Label(self.result_frame)
        self.round_result.pack()
                    
        self.result_frame.pack() 

    def on_click(self, event):

        # Runs get_computer_choice() and name is as computer_choice
        computer_choice = get_computer_choice()

        # Gets the text of the button and name is as human_choice
        button = event.widget
        human_choice = button.cget("text").lower()

        # Runs conditional checking to identify the winner
        if human_choice == computer_choice:
            output = "It's a draw!"
        elif wins[human_choice] == computer_choice:
            output = f"You Won!\nYou: {human_choice.capitalize()}, Computer: {computer_choice.capitalize()}"
        else:
            output = f"You Lost!\nYou: {human_choice.capitalize()}, Computer: {computer_choice.capitalize()}"

        self.round_result.config(text=output)

    def run(self):
        # Listens for event to the buttons
        self.rock_button.bind("<Button-1>", self.on_click)
        self.paper_button.bind("<Button-1>", self.on_click)
        self.scissors_button.bind("<Button-1>", self.on_click)

        self.window.mainloop()

# ----- Runs the program -----
if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()