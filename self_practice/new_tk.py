# import tkinter as tk
#
# def processOk():
#     print("Ok button is Clicked")
#
# def processCancel():
#     print("Cancel button is Clicked")
#
# window = tk.Tk()
# btOk = tk.Button(window, text='OK', fg='Red', command=processOk)
# btCancel = tk.Button(window, text="Cancel", bg='Yellow', command=processCancel)
# btOk.pack()
# btCancel.pack()
#
# window.mainloop()







from tkinter import *

#
# def processOk():
#     print("Ok button is Clicked")
#
# def processCancel():
#     print("Cancel button is Clicked")
#
# window = Tk()
# btOk = Button (window, text = 'OK', fg= 'Red', command = processOk)
# btCancel = Button(window, text = "Cancel", bg = 'Yellow', command= processCancel)
# btOk.pack()
# btCancel.pack()
#
# window.mainloop()



class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOk = Button(window, text = 'OK', fg= 'blue', command= self.processOk)
        btCancel = Button (window, text= 'cancel', bg= "yellow", command=self.processCancel)
        btOk.pack()
        btCancel.pack()
        window.mainloop()

    def processOk(self):
        # window = Tk()
        # btOk = Button(window, text = "Continue to click", fg= "blue", command= self.processOk)
        # btCancel = Button (window, text= 'cancel', bg= "yellow", command=self.processCancel)
        # btOk.pack()
        # btCancel.pack()
        print("Ok button is Clicked")

    def processCancel(self):
        print("Cancel button is Clicked")
        # self.processOk()


ProcessButtonEvent()