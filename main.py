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

# Here is where I will define the variables:
# "Text" variable stores the message to encode and decode
# "private_key" variable store the private key used to encode and decode
# "mode" is used to select that is either encoding or decoding
# "Result" store the result
Text = Stringvar()
private_key = Stringvar()
mode = Stringvar()
Result = Stringvar()

# This is the function to encode the message

def encode(key, message):
    enc = []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()






 
