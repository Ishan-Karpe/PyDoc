# 11/11/2024

from tkinter import *  
from tkinter import filedialog as tkFileDialog  

root = Tk()  # think of root as the control center as everything is done through it  
root.title("PyDoc Editor")  # Set the title of the window  

text = Text(root)  
text.grid()  

# Saving the program  
def save():  
    t = text.get("1.0", "end-1c")  
    save_location = tkFileDialog.asksaveasfilename()  
    if save_location:  # Ensure user selected a location  
        with open(save_location, "w+") as file1:  # write and read  
            file1.write(t)  

button = Button(root, text="Save Your Document", command=save)  
button.grid()  

# Global variables for font properties  
current_font_family = "Arial"  # Start with a default font  
current_font_size = 12  

# Toggle bold and italic styles  
def toggle_bold():  
    current_tags = text.tag_names("sel.first")  # Get the tags of the first character in the selection  
    if "bold" in current_tags:  
        text.tag_remove("bold", "sel.first", "sel.last")  
    else:  
        text.tag_add("bold", "sel.first", "sel.last")  
    update_font()  # Call to update font tag configuration  

def toggle_italic():  
    current_tags = text.tag_names("sel.first")  
    if "italic" in current_tags:  
        text.tag_remove("italic", "sel.first", "sel.last")  
    else:  
        text.tag_add("italic", "sel.first", "sel.last")  
    update_font()  # Call to update font tag configuration  

# Function to update font settings  
def update_font():  
    # Configure tags for bold and italic with the current selected font family and size  
    text.tag_configure("bold", font=(current_font_family, current_font_size, "bold"))  
    text.tag_configure("italic", font=(current_font_family, current_font_size, "italic"))  

# Initial tag configuration  
update_font()  # Set initial font styles  

bold_button = Button(root, text="Bold", command=toggle_bold)  
bold_button.grid()  
italic_button = Button(root, text="Italic", command=toggle_italic)  
italic_button.grid()  

def set_font(new_font):  
    global current_font_family  
    current_font_family = new_font  
    update_font()  # Update font tags whenever font is changed  

# Update your font configuration commands  
def FontHelvetica():  
    set_font("Helvetica")  

def FontCourier():  
    set_font("Courier")  

def FontTimes():  
    set_font("Times")  

def FontComic():  
    set_font("Comic Sans MS")  

def FontArial():  
    set_font("Arial")  

font = Menubutton(root, text="Fonts ↓")  
font.grid()  
font.menu = Menu(font, tearoff=0)  
font['menu'] = font.menu  

# Add font options  
font.menu.add_command(label='Helvetica', command=FontHelvetica)  
font.menu.add_command(label='Courier', command=FontCourier)  
font.menu.add_command(label='Times', command=FontTimes)  
font.menu.add_command(label='Comic Sans MS', command=FontComic)  
font.menu.add_command(label='Arial', command=FontArial)  

# The following part always comes last  
root.mainloop()  # the mainloop() function is used to run the application # the mainloop() function is used to run the application
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