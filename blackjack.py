import random

try:
    import tkinter as tk
except ImportError:  # python 2 scenario
    import Tkinter as tk


def load_card_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    extension = "ppm"

    # retrieve the image of the card for each suit
    for suit in suits:
        # number cards
        for card in range(1, 11):
            name = "img_cards/{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            # store value and image in tuple
            card_images.append((card, image,))
        # face cards
        for card in face_cards:
            name = "img_cards/{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            # store value and image in tuple
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card of the top (0) of the deck
    next_card = deck.pop(0)
    # and add it back to the deck at the bottom
    deck.append(next_card)
    tk.Label(frame, image=next_card[1], relief="raised")\
        .pack(side="left")
    return next_card


def get_hand_score(hand):
    # calculate tge total score of all cards in the list
    # only one ace can have the value 11
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = get_hand_score(dealer_hand)
    # Dealer will draw cards automatically until it's score is 17
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = get_hand_score(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = get_hand_score(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("It's a draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = get_hand_score(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    dealer_card_frame.destroy()
    dealer_card_frame = tk.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame = tk.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")
    # create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(get_hand_score(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


main_window = tk.Tk()

# screen and frames for dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.configure(bg="green")


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
dealer_button = tk.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# button player
player_button = tk.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tk.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tk.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_card_images(cards)
print(cards)

# create a new deck of cards and shuffle them
deck = list(cards)
shuffle()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

new_game()

main_window.mainloop()
