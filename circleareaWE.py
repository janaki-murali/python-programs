"""
File: circleAreaWE.py

Inputs a radius of a circle and outputs its area.
Expands the grid cells and also the widgets in all directions.
"""

from tkinter import *
import math

class CircleArea(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Circle Area")
        self.grid()

        # Expand the frame within the window
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)

        # Label and field for the radius
        self._radiusLabel = Label(self, text = "Radius")
        self._radiusLabel.grid(row = 0, column = 0,
                               sticky = W+E+N+S)
        self._radiusVar = DoubleVar()
        self._radiusEntry = Entry(self,
                                  textvariable = self._radiusVar)
        self._radiusEntry.grid(row = 0, column = 1,
                               sticky = W+E+N+S)

        # Label and field for the area
        self._areaLabel = Label(self, text = "Area")
        self._areaLabel.grid(row = 1, column = 0)
        self._areaVar = DoubleVar()
        self._areaEntry = Entry(self,
                                textvariable = self._areaVar)
        self._areaEntry.grid(row = 1, column = 1,
                             sticky = W+E+N+S)

        # The command buton
        self._button = Button(self,
                              text = "Compute",
                              command = self._area)
        self._button.grid(row = 2, column = 0, columnspan = 2,
                          sticky = W+E+N+S)

        # Set the expansion weights in the grid cells
        for row in range(3):
            self.rowconfigure(row, weight = 1)
        for column in range(2):
            self.columnconfigure(column, weight = 1)

    def _area(self):
        """Event handler for the button."""
        radius = self._radiusVar.get()
        area = radius ** 2 * math.pi
        self._areaVar.set(area)

def main():
    """Instantiate and pop up the window."""
    CircleArea().mainloop()

main()
