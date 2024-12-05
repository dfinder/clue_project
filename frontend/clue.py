import tkinter as tk
from tkinter import messagebox
import os
parent_directory = os.path.abspath('..')
from parent_directory.ui import suggestion, accuse, move

# Define an action for the "Standard Out" button

def standard_out_action():
    messagebox.showinfo("Standard Out", "Exiting")

# Initialize main window
root = tk.Tk()
root.title("CLUE Game UI")
root.geometry("800x600")  # Set a fixed size for the window

# Define button data
players = ["Mr. Green", "Miss Peacock", "Prof. Plum", "Mrs. Scarlett", "Dr. Orchid", "Colonel Mustard"]
weapons = ["Candlestick", "Dagger", "Revolver", "Lead pipe", "Wrench", "Rope"]
rooms = ["The Hall", "The Lounge", "The Dining Room", "The Kitchen", "The Ballroom", "The Conservatory", "The Billiard Room", "The Library", "The Study"]

# Define the left-side frame 
left_frame = tk.Frame(root, width=320, height=600, bg="lightgray")
left_frame.pack(side=tk.LEFT, fill=tk.Y)

# Player Buttons
player_label = tk.Label(left_frame, text="Players", bg="lightgray", font=("Arial", 12, "bold"))
player_label.grid(row=0, column=0, padx=10, pady=5)
for i, player in enumerate(players):
    tk.Button(left_frame, text=player, width=15, bg="lightblue", font=("Arial", 10)).grid(row=i + 1, column=0, padx=10, pady=5)

# Weapon Buttons
weapon_label = tk.Label(left_frame, text="Weapons", bg="lightgray", font=("Arial", 12, "bold"))
weapon_label.grid(row=0, column=1, padx=10, pady=5)
for i, weapon in enumerate(weapons):
    tk.Button(left_frame, text=weapon, width=15, bg="lightgreen", font=("Arial", 10)).grid(row=i + 1, column=1, padx=10, pady=5)

# Room Buttons
room_label = tk.Label(left_frame, text="Rooms", bg="lightgray", font=("Arial", 12, "bold"))
room_label.grid(row=0, column=2, padx=10, pady=5)
for i, room in enumerate(rooms):
    tk.Button(left_frame, text=room, width=15, bg="lightpink", font=("Arial", 10)).grid(row=i + 1, column=2, padx=10, pady=5)

# Adjust grid weights to ensure consistent resizing
for col in range(3):
    left_frame.grid_columnconfigure(col, weight=1)

# Right-side frame (occupies 3/5 of the width)
right_frame = tk.Frame(root, width=480, height=600, bg="white")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add Action Buttons at the top of the right frame
action_frame = tk.Frame(right_frame, bg="white")
action_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

tk.Button(action_frame, text="Accuse", width=15, bg="lightyellow", font=("Arial", 12), command=accuse).pack(side=tk.LEFT, padx=10)
tk.Button(action_frame, text="Suggest", width=15, bg="lightyellow", font=("Arial", 12), command=suggestion).pack(side=tk.LEFT, padx=10)
tk.Button(action_frame, text="Move", width=15, bg="lightyellow", font=("Arial", 12), command=move).pack(side=tk.LEFT, padx=10)
# 6x6 Matrix for Player Positions
matrix_frame = tk.Frame(right_frame, bg="white")
matrix_frame.pack(expand=True)

matrix_labels = []  # Store matrix cells for future updates
for row in range(6):
    row_labels = []
    for col in range(6):
        label = tk.Label(matrix_frame, text=" ", width=5, height=2, bg="lightgray", relief=tk.RAISED, font=("Arial", 10))
        label.grid(row=row, column=col, padx=2, pady=2)
        row_labels.append(label)
    matrix_labels.append(row_labels)

# Add "Standard Out" button in the bottom-right corner
standard_out_button = tk.Button(right_frame, text="Standard Out", bg="red", fg="white", font=("Arial", 12), command=standard_out_action)
standard_out_button.pack(side=tk.BOTTOM, anchor="se", padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
