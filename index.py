from tkinter import *
import random

def play_game():
    user_choice = user_input.get().lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if user_choice not in ["rock", "paper", "scissors"]:
        result.set("Invalid input! Please select from rock, paper, or scissors.")
    elif user_choice == computer_choice:
        result.set(f"It's a Tie! Both chose {user_choice.capitalize()}.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result.set(f"Congratulations! You win. Computer chose {computer_choice.capitalize()}.")
    else:
        result.set(f"Oops! You lose. Computer chose {computer_choice.capitalize()}.")

def reset_game():
    user_input.set("")
    result.set("")

def exit_game():
    guiWindow.destroy()

guiWindow = Tk()
guiWindow.title("Rock Paper Scissors Game")
guiWindow.geometry("400x300")
guiWindow.config(bg="#212F3D")

Label(guiWindow, text="Let's play Rock, Paper, Scissors", font="Arial 16 bold", bg="#212F3D", fg="white").pack(pady=10)

user_input = StringVar()
entry_field = Entry(guiWindow, textvariable=user_input, font="Arial 12", width=20, bd=2, relief="groove", highlightcolor="#85929E", highlightthickness=1)
entry_field.pack(pady=5)
entry_field.bind("<FocusIn>", lambda event: entry_field.config(highlightbackground="#85C1E9"))  # Change border color on focus
entry_field.bind("<FocusOut>", lambda event: entry_field.config(highlightbackground="#85929E"))  # Change border color on focus out

play_button = Button(guiWindow, text="PLAY", font="Arial 10 bold", bg="#5DADE2", fg="white", activebackground="#5499C7", activeforeground="white", bd=2, relief="raised", padx=10, pady=5, command=play_game)
play_button.pack(side=LEFT, padx=20)
play_button.bind("<Enter>", lambda event: play_button.config(bg="#5499C7", fg="white"))  # Change colors on hover
play_button.bind("<Leave>", lambda event: play_button.config(bg="#5DADE2", fg="white"))  # Restore colors on leave

reset_button = Button(guiWindow, text="RESET", font="Arial 10 bold", bg="#5DADE2", fg="white", activebackground="#5499C7", activeforeground="white", bd=2, relief="raised", padx=10, pady=5, command=reset_game)
reset_button.pack(side=LEFT, padx=20)
reset_button.bind("<Enter>", lambda event: reset_button.config(bg="#5499C7", fg="white"))  # Change colors on hover
reset_button.bind("<Leave>", lambda event: reset_button.config(bg="#5DADE2", fg="white"))  # Restore colors on leave

exit_button = Button(guiWindow, text="EXIT", font="Arial 10 bold", bg="#5DADE2", fg="white", activebackground="#5499C7", activeforeground="white", bd=2, relief="raised", padx=10, pady=5, command=exit_game)
exit_button.pack(side=LEFT, padx=20)
exit_button.bind("<Enter>", lambda event: exit_button.config(bg="#5499C7", fg="white"))  # Change colors on hover
exit_button.bind("<Leave>", lambda event: exit_button.config(bg="#5DADE2", fg="white"))  # Restore colors on leave
result = StringVar()
Label(guiWindow, textvariable=result, font="Arial 12 bold", bg="#212F3D", fg="white").pack(pady=20)
guiWindow.mainloop()
