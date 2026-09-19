import tkinter as tk
import random

# Initialize tkinter
window = tk.Tk()

window.title("Rock Paper Scissors")
window.geometry("300x200")

message = tk.Label(window, text="Your Input:")
message.pack()


# Gets a random choice between rock, paper, or scissors
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

wins = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

#---Initialize the button declaration---
buttons_frame = tk.Frame(window)

rock_button = tk.Button(buttons_frame, text="Rock")
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(buttons_frame, text="Paper")
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(buttons_frame, text="Scissors")
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Packs button_frame
buttons_frame.pack()

#---Creates the frame for the result---
result_frame = tk.Frame(window)
    
# Creates an empty label to be asigned later
round_result = tk.Label(result_frame)
round_result.pack()
    
result_frame.pack()

# Creates an event for a button click
def on_click(event):
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

    round_result.config(text=output)
    

# Listens for event to the buttons
rock_button.bind("<Button-1>", on_click)
paper_button.bind("<Button-1>", on_click)
scissors_button.bind("<Button-1>", on_click)

# Runs the window
window.mainloop()