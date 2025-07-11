import tkinter as tk
import random
from tkinter import messagebox
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


word = space_add(word_list[random.randint(0, len(word_list) - 1)])
letter_bank = ""
blank = ""
window = tk.Tk()
window.title("Hangman Game")
window.geometry("650x650")

#Creates a canvas and hides it until the player clicks on the play button
canvas = tk.Canvas(window, width=650, height=650)
canvas.pack_forget()

#Opening Window
title_label = tk.Label(window, text="Hangman", font="100")
title_label.place(x=285, y=290)


#Function that opens up the Hangman game
def play():
    canvas.pack()
    play_button.destroy()
    title_label.destroy()


#Function that takes a user input and determines if it's in the word
def guess():
    global letter_bank
    global word
    global index
    temp2 = ""
    #Check if the letter has already been guessed
    if guess_letter_entry.get() in letter_bank:
        messagebox.showinfo(title='Message', message="You've already guessed this")
        guess_letter_entry.delete(0, tk.END)
        return
    else:
        letter_bank += guess_letter_entry.get()
    if guess_letter_entry.get() in word:
        for letter in word:
            if letter in letter_bank:
                temp2 += "{} ".format(letter)
            elif letter == " ":
                continue
            else:
                temp2 += "_ "
        canvas.itemconfig(display, text=temp2)
    elif len(guess_letter_entry.get()) > 1:
        messagebox.showinfo(title='Message', message="Please type one letter at a time")
    else:
        canvas.itemconfigure(man[index], state='hidden')
        index += 1
    guess_letter_entry.delete(0, tk.END)
    #Checks win/lose conditions
    if index == 6:
        canvas.itemconfigure(game_over_label, state='normal')
        canvas.itemconfigure(display, text=word)
        guess_letter_button.config(state='disabled')
    elif temp2 == word:
        canvas.itemconfigure(win_label, state='normal')
        guess_letter_button.config(state='disabled')
    window.update()


#Intro UI
play_button = tk.Button(window, text="Play", font="20", width=7, height=1, command=play)
play_button.place(x=285, y=325)


#Creating the UI
guess_letter_label = canvas.create_text(x - 100, y + 250, text="Guess a letter:", font='20')
guess_letter_entry = tk.Entry(window, width=5)
canvas.create_window(x - 13, y + 251, window=guess_letter_entry)
guess_letter_button = tk.Button(window, text="Guess", command=guess)
canvas.create_window(x + 27, y + 251, window=guess_letter_button)


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


for _ in range(int(len(word)/2)):
    blank += "_ "
display = canvas.create_text(x, y + 220, text=blank, font='20')
window.mainloop()

