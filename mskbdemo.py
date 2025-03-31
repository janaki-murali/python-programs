from tkinter import *
class MSKBDemo(Frame):
    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Mouse and Keyboard Demo")
        self.master.geometry('200x100') #resize
        self.grid()
        var = StringVar()
        self.focus_set()
        self._label = Label(self, textvariable=var)
        self._label.grid()
        def buttonPressed( event ):
           var.set( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

        def buttonReleased( event ):
           var.set( "Released at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

        def enteredWindow( event ):
           var.set( "Mouse in window" )

        def exitedWindow(  event ):
           var.set( "Mouse outside window" )

        def keyPressed(  event ):
           var.set( repr(event.char) + " pressed")
           self.focus_set()
        self.master.bind( "<Button-1>", buttonPressed )
        self.master.bind( "<ButtonRelease-1>", buttonReleased )   
        self.master.bind( "<Enter>", enteredWindow )
        self.master.bind( "<Leave>", exitedWindow )
        self.master.bind("<Key>", keyPressed)
def main():
    """Instantiate and pop up the window."""
    MSKBDemo().mainloop()
main()