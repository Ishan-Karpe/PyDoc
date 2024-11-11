# 11/11/2024

from tkinter import *
from tkinter import filedialog as tkFileDialog

root = Tk()
root.title("PyDoc Editor")
# Tk has no agruments, but the title() function is used to set the title of the window
# Tkinter has two parts, writing what is supposed to be on the screen, and displaying it to the screen
# The first part is done by creating a root window, which is the main window of the application

text=Text(root)
text.grid()

def save():
    t= text.get("1.0", "end-1c")
    # get() is used to get the text from the text widget
    save_location=tkFileDialog.asksaveasfilename()
    #asksaveasfilename() function is used to save the file
    file1=open(save_location, "w+") #write and read
    file1.write(t)
    file1.close()
    
button=Button(root, text="Save Your Document", command=save)
button.grid()
    #grid is used to display the button on the screen, or the second part of tkinter.
# The Text() function is used to create a text widget, which is used to display text in multiple lines


#the following part always comes last
root.mainloop()
# the mainloop() function is used to run the application


