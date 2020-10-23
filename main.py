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

# enc = [] is an empty list
# We run loop till the length of the message
# i% of len(key) gives the remainder of division between i and len(key) and that remainder used as an index of key the value of key at that index is stored in key_c
# ord() function takes string argument of a single unicode character and return its integer unicode value
# chr() function takes an integer argument and returns the string.
# ord (message[i]) convert the value of message at index i into the integer value
# ord(key_c) converts the key_c value to integer value
# ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) and ord( key_c) with 256 and passes that remainder to chr() function
# chr() function converts that integer value to string and store to enc
# base64.urlsafe_b64encode encode a string.
# The join() method joins each element of list, string, and tuple by a string separator and returns the concatenated string.
# encode() method returns utf-8 encoded message of the string.
# decode() method decodes the string.
# return gives the result of the encoded string.

# encode function
def encode(key, message):
    enc = []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# decode function
def decode(keu, message):
    dec = []
    
    message = base64.urlsafe_b64decode(message).decode()
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        return "".join(dec)
    
    
    





 
