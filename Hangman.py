import tkinter as tk
x = 315
y = 250
window = tk.Tk()
window.title("Hangman Game")
window.geometry("650x650")

canvas = tk.Canvas(window, width=650, height=650)
canvas.pack_forget()

#Opening Window
title_label = tk.Label(window, text="Hangman", font="100")
title_label.place(x=285, y=290)
def play():
    canvas.pack()
    play_button.destroy()
    title_label.destroy()


play_button = tk.Button(window, text="Play", font="20", width=7, height=1, command=play)
play_button.place(x=285, y=325)


#Creating the UI
guess_letter_label = canvas.create_text(x - 100, y + 250, text="Guess a letter:", font='20')
guess_letter_entry = tk.Entry(window, width=5)
canvas.create_window(x - 17, y + 251, window=guess_letter_entry)
guess_letter_button = tk.Button(window, text="Guess")
canvas.create_window(x + 23, y + 251, window=guess_letter_button)

guess_answer_label = canvas.create_text(x - 100, y + 275, text="Guess the answer:", font='20')
guess_answer_entry = tk.Entry(window, width=15)
canvas.create_window(x + 30, y + 277, window=guess_answer_entry)
guess_answer_button = tk.Button(window, text="Guess")
canvas.create_window(x + 100, y + 277, window=guess_answer_button)


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


window.mainloop()

