from tkinter import *
import pandas
import random
import csv
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
df = pandas.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")
to_learn2=[]



#CURRENT_CARD=random.choice(to_learn)
#current_card = {}

def next_card():
    """provides new card"""
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARD = random.choice(to_learn2)
    french_value = CURRENT_CARD["French"]
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_value, fill="black")
    window.after(3000, flip_card)


def flip_card():
    """turns the card providing the solution"""
    english_value = CURRENT_CARD["English"]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text= "English", fill="white")
    canvas.itemconfig(word, text=english_value, fill="white")

# ---------------------------- DUPLICATES INFO AND SAVES TO NEW CSV ------------------------------- #
def is_known():
    """Angela's version"""
    to_learn.remove(CURRENT_CARD)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

    next_card()

try:
    df2 = pandas.read_csv("data/words_to_learn.csv")

except:

    data2 = pandas.DataFrame (to_learn)
    data2.to_csv("data/words_to_learn.csv", index=False)
    df2 = pandas.read_csv("data/words_to_learn.csv")

to_learn2 = df2.to_dict(orient="records")


# ---------------------------- DELETE CARDS USER DOES KNOW ------------------------------- #

def known_answer():
    """Delete cards the user knows from words_o_learn.csv"""

    to_learn2.remove(CURRENT_CARD)
    data2 = pandas.DataFrame(to_learn2)
    data2.to_csv("words_to_learn.csv", index=False)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

#CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage (file="./images/card_back.png")
card_front_img = PhotoImage (file="./images/card_front.png")
canvas_image = canvas.create_image(410, 270, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

#BUTTONS
check_image = PhotoImage (file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=lambda:[next_card(), known_answer()])
known_button.grid(column=1, row=1)

cross_image = PhotoImage (file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()














window.mainloop()

