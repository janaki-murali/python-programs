from tkinter import *

class Bouncy(Frame):
  def __init__(self):
     Frame.__init__(self)
     self.master.title('Bouncy')
     self.htVar = DoubleVar()
     self.bcVar = DoubleVar()
     self.nbVar = IntVar()
     self.distance = DoubleVar()
     self.grid()
     self.label1 = Label(self, text = 'Enter initial height')
     self.label1.grid(row=0,column=0)
     self.heightEntry = Entry(self,textvariable = self.htVar)
     self.heightEntry.grid(row=0,column=1)
     self.label2 = Label(self, text = 'Enter bounciness index')
     self.label2.grid(row=1,column=0)
     self.bouncyEntry = Entry(self,textvariable = self.bcVar)
     self.bouncyEntry.grid(row=1,column=1)
     self.label3 = Label(self, text = 'Number of bounces')
     self.label3.grid(row=2,column=0)
     self.bouncesEntry = Entry(self,textvariable = self.nbVar)
     self.bouncesEntry.grid(row=2,column=1)
     self.button = Button(self, text = 'Compute', command = self.dist)
     self.button.grid(row = 3, column = 0, columnspan = 2)
     self.label4 = Label(self, text = 'Total distance')
     self.label4.grid(row=4,column=0)
     self.distEntry = Entry(self,textvariable = self.distance)
     self.distEntry.grid(row=4,column=1)
     
  def dist(self):
      total = 0
      height = self.htVar.get()
      bIndex = self.bcVar.get()
      bounces = self.nbVar.get()
      for i in range(bounces):
          total+=height
          height*=bIndex
          total+=height
      self.distance.set(total)
      
     
def main():
    Bouncy().mainloop()

main()

    
