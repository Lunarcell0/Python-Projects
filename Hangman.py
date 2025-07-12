import tkinter as tk
import random
from tkinter import messagebox
from functools import partial
#Coordinates of the center of the head
x = 315
y = 250
index = 0
word_list = ["axe", 'hero', 'dog', 'rat', 'job', 'hog', 'medicine', 'ghost', 'stable', 'shepperd', 'vase']


#Adds spaces to the word
def space_add(term):
    temp = ""
    for char in term:
        temp += f"{char} "
    return temp


phrase = space_add(word_list[random.randint(0, len(word_list) - 1)])
letter_bank = ""
window = tk.Tk()
window.title("Hangman Game")
window.geometry("650x650")

#Creates a canvas and hides it until the player clicks on the play button
canvas = tk.Canvas(window, width=650, height=650)
canvas.pack_forget()


#Function that opens up the Hangman game
def play():
    canvas.pack()
    play_button.destroy()
    title_label.destroy()


#Function that creates the blank lines based on how many characters there are in the phrase
def form_blank(word):
    blank = ""
    for _ in range(int(len(word) / 2)):
        blank += "_ "
    return blank


#Function that checks if the letter has already been guessed
def key_exists(letter):
    global letter_bank
    if letter in letter_bank:
        messagebox.showinfo(title='Message', message="You've already guessed this")
        guess_letter_entry.delete(0, tk.END)
        return
    else:
        letter_bank += letter


def fill(word):
    temp = ""
    for letter in word:
        if letter in letter_bank:
            temp += "{} ".format(letter)
        elif letter == " ":
            continue
        else:
            temp += "_ "
    return temp


#Function that checks win/lose conditions
def check_conditions(i, temp, word):
    if i == 6:
        canvas.itemconfigure(game_over_label, state='normal')
        canvas.itemconfigure(display, text=word)
        guess_letter_button.config(state='disabled')
    elif temp == word:
        canvas.itemconfigure(win_label, state='normal')
        guess_letter_button.config(state='disabled')


#Function that removes a body part if the user input was wrong
def remove_body_part():
    global index
    canvas.itemconfigure(man[index], state='hidden')
    index += 1


#Function that takes a user input and determines if it's in the word
def guess(word):
    global letter_bank
    if len(guess_letter_entry.get()) > 1:
        messagebox.showinfo(title='Message', message="Please type one letter at a time")
        guess_letter_entry.delete(0, tk.END)
        return
    #Check if the letter has already been guessed
    key_exists(guess_letter_entry.get())
    if guess_letter_entry.get() in word:
        canvas.itemconfig(display, text=fill(phrase))
    else:
        remove_body_part()
    guess_letter_entry.delete(0, tk.END)
    #Checks win/lose conditions
    check_conditions(index, fill(phrase), phrase)
    window.update()


#Opening Window
title_label = tk.Label(window, text="Hangman", font="100")
title_label.place(x=285, y=290)
#Intro UI
play_button = tk.Button(window, text="Play", font="20", width=7, height=1, command=play)
play_button.place(x=285, y=325)

#Creating the UI
guess_letter_label = canvas.create_text(x - 100, y + 250, text="Guess a letter:", font='20')
guess_letter_entry = tk.Entry(window, width=5)
canvas.create_window(x - 13, y + 251, window=guess_letter_entry)
guess_letter_button = tk.Button(window, text="Guess", command=partial(guess, phrase))
canvas.create_window(x + 27, y + 251, window=guess_letter_button)
display = canvas.create_text(x, y + 220, text=form_blank(phrase), font='20')

#Creating the Hangman
base = canvas.create_line(x - 150, y + 210, x + 100, y + 210)
pillar = canvas.create_line(x - 100, y - 75, x - 100, y + 210)
beam = canvas.create_line(x, y - 75, x - 100, y - 75)
knot = canvas.create_line(x, y - 50, x, y - 75)
head = canvas.create_oval(x - 25, y, x + 25, y - 50)
body = canvas.create_line(x, y, x, y + 100)
left_arm = canvas.create_line(x, y, x - 50, y + 100)
right_arm = canvas.create_line(x, y, x + 50, y + 100)
left_leg = canvas.create_line(x, y + 100, x - 40, y + 200)
right_leg = canvas.create_line(x, y + 100, x + 40, y + 200)
man = [right_leg, left_leg, right_arm, left_arm, body, head]

#Game Over/Winner UI
game_over_label = canvas.create_text(x, y - 100, text="Game Over", font='20')
canvas.itemconfigure(game_over_label, state='hidden')
win_label = canvas.create_text(x, y - 100, text="You win!!", font='20')
canvas.itemconfigure(win_label, state='hidden')

window.mainloop()
