# 11/11/2024

from tkinter import *

root = Tk()
root.title("PyDoc Editor")
# Tk has no agruments, but the title() function is used to set the title of the window
# Tkinter has two parts, writing what is supposed to be on the screen, and displaying it to the screen
# The first part is done by creating a root window, which is the main window of the application

text=Text(root)
text.grid()
# The Text() function is used to create a text widget, which is used to display text in multiple lines


#the following part always comes last
root.mainloop()
# the mainloop() function is used to run the application


