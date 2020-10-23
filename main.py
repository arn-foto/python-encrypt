import tkinter
import base64

# Tk() initialized tkinter which means window created
root = Tk()
# geometry() set the width and height of the window
root.geometry('500x300')
# resizable(0,0) set the fixed size of the window
root.sizable(0,0)
# title() set the title of the window
root.title("encode & decode, son")

# Label() widget use to display
#  one or more than one line of text that users aren’t able to modify.
label(root, test = 'python encrypt', font = 'arial 20 bold').pack()
# "root" is the name we call our window
# "text" is displayed on the label
# "pack" organized widget in block
label(root, text = 'excrypt python', font = 'arial 20 bold').pack(side=BOTTOM)

# here is where I will define the variables
Text = Stringvar()
private_key = Stringvar()
mode = Stringvar()
Result = Stringvar()





 
