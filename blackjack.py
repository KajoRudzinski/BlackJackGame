import random

try:
    import tkinter as tk
except ImportError:  # python 2 scenario
    import Tkinter as tk

main_window = tk.Tk()

# screen and frames for dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")

result_text = tk.StringVar()
result = tk.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(
    main_window, relief="sunken", borderwidth=1, bg="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer
dealer_score_label = tk.IntVar()
tk.Label(
    card_frame, text="Dealer", bg="green", fg="white")\
    .grid(row=0, column=0)
tk.Label(
    card_frame, textvariable=dealer_score_label, bg="green", fg="white")\
    .grid(row=1, column=0)

# dealer cards
dealer_card_frame = tk.Frame(card_frame, bg="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tk.IntVar()
tk.Label(
    card_frame, text="Player", bg="green", fg="white") \
    .grid(row=2, column=0)
tk.Label(
    card_frame, textvariable=player_score_label, bg="green", fg="white") \
    .grid(row=3, column=0)

# player cards
player_card_frame = tk.Frame(card_frame, bg="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# button frames
button_frame = tk.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

# button dealer
dealer_button = tk.Button(button_frame, text="Dealer")
dealer_button.grid(row=0, column=0)

# button player
player_button = tk.Button(button_frame, text="Player")
player_button.grid(row=0, column=1)

main_window.mainloop()
