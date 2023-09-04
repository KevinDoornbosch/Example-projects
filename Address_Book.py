import tkinter as tk

window= tk.Tk()
window.title('Address Entry Form')


window.columnconfigure(0, weight=1, minsize = 75)
window.columnconfigure(1, weight=5, minsize = 500)
window.rowconfigure([0,1,2,3,4,5,6], weight=1, minsize = 20)


label_fn = tk.Label(window, text='First Name: ')
label_fn.grid(row=0, column=0)
entry_fn = tk.Entry(window)
entry_fn.grid(row=0, column=1, sticky='enws')

label_ln = tk.Label(window, text='Last Name: ')
label_ln.grid(row=1, column=0)
entry_ln = tk.Entry(window)
entry_ln.grid(row=1, column=1, sticky='enws')

label_a = tk.Label(window, text='Address: ')
label_a.grid(row=2, column=0)
entry_a = tk.Entry(window)
entry_a.grid(row=2, column=1, sticky='enws')

label_city = tk.Label(window, text='City: ')
label_city.grid(row=3, column=0)
entry_city = tk.Entry(window)
entry_city.grid(row=3, column=1, sticky='enws')

label_state = tk.Label(window, text='State: ')
label_state.grid(row=4, column=0)
entry_state = tk.Entry(window)
entry_state.grid(row=4, column=1, sticky='enws')

label_zip = tk.Label(window, text='Zip Code: ')
label_zip.grid(row=5, column=0)
entry_zip = tk.Entry(window)
entry_zip.grid(row=5, column=1, sticky='enws')

def handler_clear():
    entry_fn.delete(0, tk.END)
    entry_ln.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_state.delete(0, tk.END)

    n_zip = len(entry_zip.get())
    entry_zip.delete(0, n_zip)

    label_error['text'] = ''

def handler_submit():
    
    str_fn = entry_fn.get()
    if not str_fn.isalpha():
        label_error['text'] = 'First Name can only have letters. '

    str_ln = entry_ln.get()
    if not str_ln.isalpha():
        label_error['text'] = 'Last name can only have letters. '
    
    str_a = entry_a.get()    
    
    str_city = entry_city.get()
    if str_city.isnumeric():
        label_error['text'] = 'City can only have letters. '

    str_state = entry_state.get()
    if not str_state.isalpha():
        label_error['text'] = 'State can only have letters. '

    str_zipcode = entry_zip.get()
    if not str_zipcode.isnumeric() or len(str_zipcode) != 5:
        label_error['text'] = 'Zip code can only have 5 digits. '

    

    with open('./address_book.txt', mode='w', encoding='utf-8') as f:
        f.write(str_fn)
        f.write('\n')

        f.write(str_ln)
        f.write('\n')

        f.write(str_a)
        f.write('\n')

        f.write(str_city)
        f.write('\n')

        f.write(str_state)
        f.write('\n')

        f.write(str_zipcode)
        f.write('\n')

frame= tk.Frame(window)

button_clear = tk.Button(frame, text='Clear', command=handler_clear)
button_clear.pack(side=tk.LEFT)

button_submit = tk.Button(frame, text='Submit', command=handler_submit)
button_submit.pack(side=tk.LEFT)

label_error = tk.Label(frame, fg='red')
label_error.pack(side=tk.LEFT)

frame.grid(row=6, column=1, sticky='enws')



window.mainloop()