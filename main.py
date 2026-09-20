import tkinter as tk
import random

# ----- GAME LOGIC -----

# Gets a random choice between rock, paper, or scissors
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

wins = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

# ----- GRAPHICAL USER INTERFACE -----

# Initialize tkinter widgets
class Widgets:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x200")

        self.message = tk.Label(self.window, text="Your Input:")
        self.message.pack()

widgets = Widgets()

#Initialize the button declaration
class Buttons:
    def __init__(self):
        self.buttons_frame = tk.Frame(widgets.window)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock")
        self.rock_button.grid(row=0, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper")
        self.paper_button.grid(row=0, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors")
        self.scissors_button.grid(row=0, column=2, padx=10, pady=10)

        # Packs button_frame
        self.buttons_frame.pack()

buttons = Buttons()

# Creates a frame and message to display the result to the user
class GameResult:
    def __init__(self):
        #---Creates the frame for the result---
        self.result_frame = tk.Frame(widgets.window)
    
        # Creates an empty label to be asigned later
        self.round_result = tk.Label(self.result_frame)
        self.round_result.pack()
    
        self.result_frame.pack()

game_result = GameResult()

# Creates an event for a button click
class WidgetEvents:
    def __init__(self, event):
        # Runs get_computer_choice() and name is as computer_choice
        self.computer_choice = get_computer_choice()

        # Gets the text of the button and name is as human_choice
        self.button = event.widget
        self.human_choice = self.button.cget("text").lower()

        # Runs conditional checking to identify the winner
        if self.human_choice == self.computer_choice:
            output = "It's a draw!"
        elif wins[self.human_choice] == self.computer_choice:
            output = f"You Won!\nYou: {self.human_choice.capitalize()}, Computer: {self.computer_choice.capitalize()}"
        else:
            output = f"You Lost!\nYou: {self.human_choice.capitalize()}, Computer: {self.computer_choice.capitalize()}"

        game_result.round_result.config(text=output)

# Listens for event to the buttons
buttons.rock_button.bind("<Button-1>", WidgetEvents)
buttons.paper_button.bind("<Button-1>", WidgetEvents)
buttons.scissors_button.bind("<Button-1>", WidgetEvents)

# Runs the window
if __name__ == "__main__":
    widgets.window.mainloop()