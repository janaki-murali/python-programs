from tkinter import *

class TempConverter(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Temperature Converter')
        
        self.fVar = DoubleVar()
        self.cVar = DoubleVar()
        
        self.grid()

        # Row 0 - Labels
        self.labelF = Label(self, text='Fahrenheit')
        self.labelF.grid(row=0, column=0)
        self.labelC = Label(self, text='Celsius')
        self.labelC.grid(row=0, column=1)

        # Row 1 - Entry fields
        self.entryF = Entry(self, textvariable=self.fVar)
        self.entryF.grid(row=1, column=0)
        self.fVar.set(32.0)

        self.entryC = Entry(self, textvariable=self.cVar)
        self.entryC.grid(row=1, column=1)
        self.cVar.set(0.0)

        # Row 2 - Buttons
        self.toCelsiusBtn = Button(self, text='>>>>', command=self.to_celsius)
        self.toCelsiusBtn.grid(row=2, column=0)

        self.toFahrenheitBtn = Button(self, text='<<<<', command=self.to_fahrenheit)
        self.toFahrenheitBtn.grid(row=2, column=1)

    def to_celsius(self):
        try:
            f = self.fVar.get()
            c = (f - 32) * 5 / 9
            self.cVar.set(round(c, 2))
        except ValueError:
            self.cVar.set('Err')

    def to_fahrenheit(self):
        try:
            c = self.cVar.get()
            f = (c * 9 / 5) + 32
            self.fVar.set(round(f, 2))
        except ValueError:
            self.fVar.set('Err')

def main():
    TempConverter().mainloop()

main()
