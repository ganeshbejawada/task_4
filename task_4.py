#TASK 4
#ROCK-PAPER-SCISSORS GAME

import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        # Create a frame for the game
        self.game_frame = tk.Frame(self.root, padx=20, pady=20)
        self.game_frame.pack()
        
        # Header label
        self.header_label = tk.Label(self.game_frame, text="Rock Paper Scissors Game", font=("Helvetica", 20, "bold"), pady=10)
        self.header_label.grid(row=0, column=0, columnspan=3)
        
        # User's choice label and buttons
        self.user_choice_label = tk.Label(self.game_frame, text="Your Choice:", font=("Helvetica", 14))
        self.user_choice_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.rock_button = tk.Button(self.game_frame, text="Rock", font=("Helvetica", 12), width=10, command=lambda: self.play_game("rock"), bg="#ff9999")
        self.rock_button.grid(row=1, column=1, padx=10, pady=5)
        
        self.paper_button = tk.Button(self.game_frame, text="Paper", font=("Helvetica", 12), width=10, command=lambda: self.play_game("paper"), bg="#99ff99")
        self.paper_button.grid(row=1, column=2, padx=10, pady=5)
        
        self.scissors_button = tk.Button(self.game_frame, text="Scissors", font=("Helvetica", 12), width=10, command=lambda: self.play_game("scissors"), bg="#9999ff")
        self.scissors_button.grid(row=1, column=3, padx=10, pady=5)
        
        # Computer's choice label and result display
        self.computer_choice_label = tk.Label(self.game_frame, text="Computer's Choice:", font=("Helvetica", 14))
        self.computer_choice_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.computer_choice_display = tk.Label(self.game_frame, text="", font=("Helvetica", 14, "bold"))
        self.computer_choice_display.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
        
        # Result display label
        self.result_label = tk.Label(self.game_frame, text="Result:", font=("Helvetica", 16, "bold"))
        self.result_label.grid(row=3, column=0, padx=10, pady=5)
        
        self.result_display = tk.Label(self.game_frame, text="", font=("Helvetica", 16))
        self.result_display.grid(row=3, column=1, columnspan=3, padx=10, pady=5)
        
        # Score display
        self.score_label = tk.Label(self.game_frame, text="Score:", font=("Helvetica", 14))
        self.score_label.grid(row=4, column=0, padx=10, pady=5)
        
        self.score_display = tk.Label(self.game_frame, text=f"You: {self.user_score} | Computer: {self.computer_score}", font=("Helvetica", 14))
        self.score_display.grid(row=4, column=1, columnspan=3, padx=10, pady=5)
        
        # Play again button
        self.play_again_button = tk.Button(self.game_frame, text="Play Again", font=("Helvetica", 12), command=self.reset_game, bg="#cccccc")
        self.play_again_button.grid(row=5, column=0, columnspan=4, pady=10)
        
    def play_game(self, user_choice):
        # Generate computer's choice
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        # Display computer's choice
        self.computer_choice_display.config(text=computer_choice.capitalize(), fg="black")
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        # Update result display and score
        self.result_display.config(text=result, fg="black")
        self.score_display.config(text=f"You: {self.user_score} | Computer: {self.computer_score}")
        
    def reset_game(self):
        # Reset game state
        self.user_score = 0
        self.computer_score = 0
        
        self.computer_choice_display.config(text="")
        self.result_display.config(text="")
        self.score_display.config(text=f"You: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
