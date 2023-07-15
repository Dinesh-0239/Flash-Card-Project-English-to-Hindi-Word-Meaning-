# -------------------------------- Flash-Card-Project-English-to-Hindi-Word-Meaning ---------------------------------- #
"""
# Flash-Card-Project-English-to-Hindi-Word-Meaning-

Date:- 15/07/2023
Developer:- Dinesh Singh
Technologies Used:- Python's Tkinter

Description:-  In this project you have no. of cards whose frunt side contains English word and back side contains their
hindi meaning. You have 2 buttons for where checkmark represents known word and cross represents unknown word. If cross
button will clicked then card fliped and shows hindi meaning of the the frunt english word and if checkmark clicked then
proceed to the next word and the word whose checkmark had clicked will be removed from the data and remaining will be in
the to_learn dataframe.
If none of the button will be clicked it will considered as cross button is clicked. The program wait for 3 seconds only.
"""
# ------------------------------------------ Import Statements ------------------------------------------------------- #

from tkinter import *
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIMER = 3000
current_card = None

# ------------------------------------------Dealing with Data--------------------------------------------------------- #
try:
    flashWords_df = pd.read_csv("to_learn.csv")
except FileNotFoundError:
    flashWords_df = pd.read_csv("flash_words.csv")
#Here we create a list of dictionary => [{'Hindi': 'में', 'English': 'In'}, {'Hindi': 'है', 'English': 'Is'},------]
flashWords = flashWords_df.to_dict(orient="records")

def flip_card():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(card_title,text="हिंदी",fill="white")
    canvas.itemconfig(card_word,text=current_card["Hindi"],fill="white")
    canvas.itemconfig(canvas_img,image=back_card_img)
    timer = window.after(FLIP_TIMER,func=next_card)
def next_card():
    global timer, current_card
    window.after_cancel(timer)
    current_card = choice(flashWords)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["English"],fill="black")
    canvas.itemconfig(canvas_img, image=card_frunt_img)
    timer = window.after(FLIP_TIMER,func=flip_card)
def is_known():
    global flashWords
    flashWords.remove(current_card)
    data = pd.DataFrame(flashWords)
    data.to_csv("to_learn.csv",index=False)
    next_card()

# ------------------------------------------User Interface------------------------------------------------------------ #
window = Tk()
window.title("Fashy")
window.iconbitmap("AppIcon.ico")
window.resizable(False,False)
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

#Canvas
canvas = Canvas(window,width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_frunt_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
#Image to canvas
canvas_img = canvas.create_image(400,263)
#Text to canvas
card_title = canvas.create_text(400,150,font="Ariel 40 italic")
card_word = canvas.create_text(400,263,font="Ariel 60 bold")

#timer
timer = window.after(FLIP_TIMER,func=flip_card)

#buttons
no_img = PhotoImage(file="images/wrong.png")
no_btn = Button(window,image=no_img,highlightthickness=0,command=flip_card)
no_btn.grid(row=1,column=0,pady=20)

yes_img = PhotoImage(file="images/right.png")
yes_btn = Button(window,image=yes_img,highlightthickness=0,command=is_known)
yes_btn.grid(row=1,column=1,pady=20)

#Displaying Initial words
next_card()
window.mainloop()
# -------------------------------------------------------------------------------------------------------------------- #
