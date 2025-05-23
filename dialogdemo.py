"""
File: dialogdemo.py

Class for testing popup dialogs
"""

from tkinter import *
#import tkMessageBox
from tkinter import messagebox

class DialogDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Dialog Demo")
        self.grid()
        self._button1 = Button(self,
                               text = "Info",
                               command = self._info)
        self._button1.grid()

        self._button2 = Button(self,
                               text = "Error",
                               command = self._error)
        self._button2.grid()
        self._button3 = Button(self,
                               text = "Warning",
                               command = self._warning)
        self._button3.grid()
        self._button4 = Button(self,
                               text = "Yes/No",
                               command = self._yesno)
        self._button4.grid()
        
    def _info(self):
        #tkMessageBox.showinfo(message = "This is a nice day parent = self)
        messagebox.showinfo(message = "This is a nice day",parent = self)
    def _error(self):
        #tkMessageBox.showerror(message = "This is an error",  parent = self)
        messagebox.showerror(message = "This is an error",  parent = self)
    def _warning(self):
        #tkMessageBox.showwarning(message = "This is a warning",  parent = self)
        messagebox.showwarning(message = "This is a warning",  parent = self)
    def _yesno(self):
        #tkMessageBox.askyesno(message = "Is it a nice day?", parent = self)
        messagebox.askyesno(message = "Is it a nice day?", parent = self)
def main():
    """Instantiate and pop up the window."""
    DialogDemo().mainloop()

main()

