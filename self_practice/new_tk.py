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


#
# class ProcessButtonEvent:
#     def __init__(self):
#         window = Tk()
#         btOk = Button(window, text = 'OK', fg= 'blue', command= self.processOk)
#         btCancel = Button (window, text= 'cancel', bg= "yellow", command=self.processCancel)
#         btOk.pack()
#         btCancel.pack()
#         window.mainloop()
#
#     def processOk(self):
#         print("Ok button is Clicked")
#
#     def processCancel(self):
#         print("Cancel button is Clicked")
#         # self.processOk()
#
#
# ProcessButtonEvent()


class GridManager:
    window = Tk()
    window.title("The Bank Manager")
    message = Message(window, text= "Kindly input Firstname and Lastname ")
    message.grid(row = 1, column= 1, rowspan=3, columnspan= 2)
    Label(window, text= "First Name:").grid(row=1 ,column=3)
    Entry(window).grid(row=2, column=4)
    Button(window,text= "Get Name").grid(row=3, padx= 5, pady= 5, column=4, sticky= E)

    window.mainloop()

GridManager()
