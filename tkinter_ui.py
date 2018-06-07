from tkinter import *
from tkinter import ttk

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='hello----world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='quit', command=self.quit)
#         self.quitButton.pack()
#
#
# if __name__ == '__main__':
#     app = Application()
#     app.master.title('hello world')
#     app.mainloop()

# root_win = Tk()
#
# root_win.title('root window')
#
# root_win.geometry('300x300')
#
# app = Frame(root_win, height=20, width=400, bg='red').pack()
#
# app.grid()
#
# label = Label(app, text="hello word!")
# label.grid()
#
# root_win.mainloop()

# root = Tk()
#
# Button(text='hello world').grid()
#
# root.mainloop()

# def calculate(*args):
#     try:
#         value = float(feet.get())

# from tkinter import *
# from tkinter import ttk
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass
#
# root = Tk()
# root.title("Feet to Meters")
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)
# feet = StringVar()
# meters = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#
# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)
#
# feet_entry.focus()
# root.bind('<Return>', calculate)
# root.mainloop()

from tkinter import *

# def validateText(contents):
#     print(contents)
#     return contents.isalnum()
#
# root = Tk()
#
# e = StringVar()
#
# entry = Entry(root, validtate='key', textvariable=e, validatecommand=validateText)
#
# entry.pack()

root = Tk()
e = StringVar()
def validateText(contents):
    print (contents)
    return contents.isalnum()

entry = Entry(root,validate = 'key',textvariable = e,validatecommand = validateText)
entry.pack()

root.mainloop()

