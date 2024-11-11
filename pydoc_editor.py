# 11/11/2024

from tkinter import *
from tkinter import filedialog as tkFileDialog

root = Tk() #think of root as the control center as everything is done through it
root.title("PyDoc Editor")
# Tk has no agruments, but the title() function is used to set the title of the window
# Tkinter has two parts, writing what is supposed to be on the screen, and displaying it to the screen
# The first part is done by creating a root window, which is the main window of the application


text=Text(root)
text.grid()

#saving the program
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

#onto the fonts
def FontHelvetica():
    global text#global is used to make the variable text global, so that it can be used in the function
    text.config(font="Helvetica")  

#repeat the same process for some basic fonts
def FontCourier():
    global text
    text.config(font="Courier")
    
def FontTimes():
    global text
    text.config(font="Times")
    
def FontComic():
    global text
    text.config(font="Comic Sans MS")
    
def FontArial():
    global text
    text.config(font="Arial")
    
font=Menubutton(root, text="Fonts ↓")
# menubutton is used to create a button that opens a dropdown menu
font.grid()
font.menu=Menu(font, tearoff=0) #tearoff is used to remove the dashed line from the dropdown menu
font['menu']=font.menu # this is used to display the dropdown menu
helvetica=IntVar() #IntVar() is used to create a variable that can be used to store integers
# repeat the same process for the other fonts
courier=IntVar()
times=IntVar()
comic=IntVar()
arial=IntVar()

font.menu.add_checkbutton(label='Helvetica', variable=helvetica, command=FontHelvetica)
# this is used to add a checkbutton to the dropdown menu
# the label is the text that is displayed on the dropdown menu
# the Variable is used to store the value of the checkbutton
# the command is used to run the function FontCourier when the checkbutton is clicked
# repeat the same process for the other fonts
font.menu.add_checkbutton(label='Courier', variable=courier, command=FontCourier)
font.menu.add_checkbutton(label='Times', variable=times, command=FontTimes)
font.menu.add_checkbutton(label='Comic Sans MS', variable=comic, command=FontComic)
font.menu.add_checkbutton(label="Arial", variable=arial, command=FontArial)

#it changes the font for the whole thing or whatever you decided to write

#the following part always comes last
root.mainloop()
# the mainloop() function is used to run the application


'''

in summary,

the program is a simple text editor that allows the user to write text, 
save it, and change the font of the text.

The program uses the Tkinter library to create a GUI application.
The program creates a root window using the Tk() function.
The program creates a text widget using the Text() function to display text.
The program creates a button using the Button() function to save

The program creates a dropdown menu with menu items which are the fonts, each in their own function
The program uses the fonts as integers to store the value of the checkbutton

 add_checkbutton is part of the Tk lib and has 3 arguments
 in this case they are uses to peice the function and labels together. 
'''