import tkinter as tk
from Pass_Maker import password
import pyperclip as pc
window= tk.Tk()
window.title('Password Creator')

#window Settings
window.columnconfigure(0, weight=1, minsize = 75)
window.columnconfigure(1, weight=5, minsize = 300)
window.rowconfigure([0,1,2,3,4,5,6,7], weight=1, minsize = 20)

#Label and Entry Setup
label_NumChar = tk.Label(window, text='Number of characters: ')
label_NumChar.grid(row=0, column=0)
entry_NumChar = tk.Entry(window)
entry_NumChar.grid(row=0, column=1, sticky='we')

label_NumUpper = tk.Label(window, text='Min. number of Uppercase letters: ')
label_NumUpper.grid(row=1, column=0)
entry_NumUpper = tk.Entry(window)
entry_NumUpper.grid(row=1, column=1, sticky='enws')

label_SC = tk.Label(window, text='Min. number of Special Characters: ')
label_SC.grid(row=2, column=0)
entry_SC = tk.Entry(window)
entry_SC.grid(row=2, column=1, sticky='enws')

label_Digit = tk.Label(window, text='Number of Digits: ')
label_Digit.grid(row=3, column=0)
entry_Digit = tk.Entry(window)
entry_Digit.grid(row=3, column=1, sticky='enws')

label_web = tk.Label(window, text='Website: ')
label_web.grid(row=4, column=0)
entry_web = tk.Entry(window)
entry_web.grid(row=4, column=1, sticky='enws')

label_un = tk.Label(window, text='Username: ')
label_un.grid(row=5, column=0)
entry_un = tk.Entry(window)
entry_un.grid(row=5, column=1, sticky='enws')


label_pass = tk.Label(window, text='Generated Password: ')
label_pass.grid(row=7, column=0)
label_error = tk.Label(window, text='')
label_error.grid(row=7, column=1, sticky='w')



#Clears all entries and outputs
def handler_clear():
    entry_NumChar.delete(0, tk.END)
    entry_NumUpper.delete(0, tk.END)
    entry_SC.delete(0, tk.END)
    entry_Digit.delete(0, tk.END)
    entry_web.delete(0, tk.END)

    n_un = len(entry_un.get())
    entry_un.delete(0, n_un)

    label_error['text'] = ''
    button_copy['text'] = 'Copy Password'
    

#Initializes Password
pw =''

#When hitting submit button it checks for errors, creates password, and appends password to a txt file
def handler_submit():
    global button_copy
    
    str_NumChar = entry_NumChar.get()
    if not str_NumChar.isnumeric():
        label_error['text'] = 'Enter a Number. '

    str_NumUpper = entry_NumUpper.get()
    if not str_NumUpper.isnumeric():
        label_error['text'] = 'Enter a Number. '
    
    str_SC = entry_SC.get()
    if not str_SC.isnumeric():
        label_error['text'] = 'Enter a Number. '  
    
    str_Digit = entry_Digit.get()
    if not str_Digit.isnumeric():
        label_error['text'] = 'Enter a Number. '

    pw = password(str_NumChar, str_NumUpper, str_SC, str_Digit)

    str_web = entry_web.get()

    str_un = entry_un.get()
    
    
    label_error['text'] = pw
    
    if int(str_NumUpper) + int(str_SC) + int(str_Digit) > int(str_NumChar):
        label_error['text'] = f'Error: You have exceeded {int(str_NumChar)} Characters. '
    
    

    with open('./jk.txt', mode='a', encoding='utf-8') as f:
        f.write('Website: ')
        f.write(str_web)
        f.write('\n')

        f.write('Username: ')
        f.write(str_un)
        f.write('\n')

        f.write('Password: ')
        f.write(pw)
        f.write('\n')
        f.write('\n')

#Function fort the copy button that copies password to users clipboard
def handler_copy():
        global button_copy
        pw = label_error['text']
        if pw:
            pc.copy(pw)
            button_copy['text'] = 'Copied!'


frame= tk.Frame(window)


#Button setup
button_submit = tk.Button(frame, text='Submit', command=handler_submit)
button_submit.pack(side=tk.LEFT)

button_clear = tk.Button(frame, text='Clear', command=handler_clear)
button_clear.pack(side=tk.LEFT)


button_copy = tk.Button(frame, text='Copy Password', command=handler_copy)
button_copy.pack(side=tk.LEFT)

frame.grid(row=6, column=1, sticky='enws')




window.mainloop()