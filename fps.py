from tkinter import *

class fps():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.title("FPS Trainer v1")

        lastButton = True
        points = 0

        self.timeHeader = Label(
                        text ="Time remaining: ",
                        fg = "white",
                        bg = "black",
                        width = 400,
                        anchor=NW)
        self.timeHeader.pack(side=TOP)

        self.pointHeader = Label(
                        text ="Points: ",
                        fg = "white",
                        bg = "black",
                        width = 400,
                        anchor=NW)
        self.pointHeader.pack(side=TOP)

        self.buttonStart = Button(self.root,
                        text = 'Start the game', 
                        bg = "white", 
                        command= lambda:[self.timer(self)])
        self.buttonStart.pack(side=BOTTOM,pady=15)

        self.root.mainloop()

    def timer(self, timeHeader):
       timeHeader.config(text = 'ye')

    def addPoint(points):
        points += 1

app = fps()