from tkinter import *

class ReverseGuess(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Computer Guesses Your Number")
        self.grid()

        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.attempts = 0

        self.guessVar = StringVar()
        self.guessVar.set(f"My guess is {self.guess}. Is it correct?")

        self.label = Label(self, textvariable=self.guessVar)
        self.label.grid(row=0, column=0, columnspan=3)

        self.tooSmallBtn = Button(self, text="Too Small", command=self.too_small)
        self.tooSmallBtn.grid(row=1, column=0)

        self.correctBtn = Button(self, text="Correct", command=self.correct)
        self.correctBtn.grid(row=1, column=1)

        self.tooLargeBtn = Button(self, text="Too Large", command=self.too_large)
        self.tooLargeBtn.grid(row=1, column=2)

        self.newGameBtn = Button(self, text="New Game", command=self.new_game, state=DISABLED)
        self.newGameBtn.grid(row=2, column=0, columnspan=3)

    def update_guess(self):
        self.guess = (self.low + self.high) // 2
        self.attempts += 1
        self.guessVar.set(f"My guess is {self.guess}. Is it correct?")

    def too_small(self):
        self.low = self.guess + 1
        self.update_guess()

    def too_large(self):
        self.high = self.guess - 1
        self.update_guess()

    def correct(self):
        self.guessVar.set(f"I guessed it! The number is {self.guess}. Attempts: {self.attempts}")
        self.disable_buttons()

    def new_game(self):
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.update_guess()

def main():
    ReverseGuess().mainloop()

main()
