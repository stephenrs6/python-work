from tkinter import *



class MathCalculator:

    def __init__(self):

        self.window = Tk()

        self.window.title("Math Calculator")

        Label(self.window, text="+").grid(row=1, column=2, sticky=W)

        Label(self.window, text="=").grid(row=1, column=4, sticky=W)

        self.labelText = StringVar()

        self.labelText.set("")

        self.result = Label(self.window, textvariable=self.labelText).grid(row=1, column=5, sticky=W)

        self.num1 = StringVar()

        Entry(self.window, textvariable=self.num1,

        justify=RIGHT).grid(row=1, column=1)

        self.num2 = StringVar()

        Entry(self.window, textvariable=self.num2,

        justify=RIGHT).grid(row=1, column=3)

        btAdd = Button(self.window, text="Add",

        command=self.computeAdd).grid(row=4, column=1, sticky=E)

        btClear = Button(self.window, text="Clear",

        command=self.Clear).grid(row=4, column=2, sticky=E)

        btQuit = Button(self.window, text="Quit", justify=LEFT,

        command=self.Quit).grid(row=4, column=3, sticky=W)

        self.window.mainloop()

    def computeAdd(self):

        output = int(self.num1.get()) + int(self.num2.get())

        self.labelText.set(str(output))

    def Clear(self):

        self.num1.set("")

        self.num2.set("")

        self.labelText.set("")

    def Quit(self):

        self.window.quit()



def main():

    MathCalculator()



main()