from tkinter import *

class UppercaseConverter(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Uppercase Converter")
        
        self.inputStr = StringVar()
        self.outputStr = StringVar()
        
        self.grid()

        # Row 0 - Label and Entry for input
        self.label1 = Label(self, text="Enter a string:")
        self.label1.grid(row=0, column=0)
        self.inputEntry = Entry(self, textvariable=self.inputStr)
        self.inputEntry.grid(row=0, column=1)

        # Row 1 - Button to convert
        self.convertButton = Button(self, text="Convert to Uppercase", command=self.convert)
        self.convertButton.grid(row=1, column=0, columnspan=2)

        # Row 2 - Label and Entry for output
        self.label2 = Label(self, text="Uppercase result:")
        self.label2.grid(row=2, column=0)
        self.outputEntry = Entry(self, textvariable=self.outputStr)
        self.outputEntry.grid(row=2, column=1)

    def convert(self):
        text = self.inputStr.get()
        self.outputStr.set(text.upper())

def main():
    UppercaseConverter().mainloop()

main()
