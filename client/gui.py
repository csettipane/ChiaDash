"""
This module contains the tkinter-based
GUI for the application. The interface displays information to the users 
about their chia servers.
"""

import tkinter as tk

class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())



root = tk.Tk()
myapp = App(root)

myapp.master.title("My Do-Nothing Application")

myapp.mainloop()