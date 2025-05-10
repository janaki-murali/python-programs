from tkinter import *
import random

class GuessNumberGame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Guess the Number Game")

        self.numberToGuess = random.randint(1, 100)
        self.guessCount = IntVar()
        self.guessCount.set(0)

        self.userGuess = IntVar()
        self.resultMsg = StringVar()

        self.grid()

        # Row 0 - Label and Entry for Guess
        self.label1 = Label(self, text="Enter your guess (1-100):")
        self.label1.grid(row=0, column=0)
        self.entry = Entry(self, textvariable=self.userGuess)
        self.entry.grid(row=0, column=1)

        # Row 1 - Button to Submit
        self.submitButton = Button(self, text="Submit Guess", command=self.check_guess)
        self.submitButton.grid(row=1, column=0, columnspan=2)

        # Row 2 - Result Message
        self.resultLabel = Label(self, textvariable=self.resultMsg)
        self.resultLabel.grid(row=2, column=0, columnspan=2)

    def check_guess(self):
        guess = self.userGuess.get()
        self.guessCount.set(self.guessCount.get() + 1)

        if guess < self.numberToGuess:
            self.resultMsg.set("Too small, try again.")
        elif guess > self.numberToGuess:
            self.resultMsg.set("Too large, try again.")
        else:
            self.resultMsg.set("Congratulations! You guessed it in {self.guessCount.get()} tries.")

def main():
    GuessNumberGame().mainloop()

main()
