from tkinter import *
import tkinter as tk
from tkinter import ttk
# Display
window = tk.Tk()
window.title('Convert manager')
window.geometry('555x250')
ttk.Label(window, text="Convert Manager",background='grey', foreground="white",font=("Times New Roman", 20)).pack()
def Convert():
    Vn1 = nmbr1_name.get()
    Vn2 = nmbr2_name.get()

    n1 = nmbr1_value.get()
    nmbr2_value.get()
    if Vn1 == 'Decimale' and Vn2 == 'Binaire':
        nmbr2_value.set(bin(int(n1)).replace("0b", ""))

    if Vn1 == 'Binaire' and Vn2 == 'Decimale':
        nmbr2_value.set(int(n1, 2))

    if Vn1 == 'Hexadecimale' and Vn2 == 'Decimale':
        nmbr2_value.set(int(n1, 16))

    if Vn1 == 'Decimale' and Vn2 == 'Hexadecimale':
        rep = hex(int(n1)).split('x')[-1]
        nmbr2_value.set(rep)

    if Vn1 == 'Octale' and Vn2 == 'Decimale':
        rep2 = oct(int(n1))
        nmbr2_value.set(rep2)

    if Vn1 == 'Decimale' and Vn2 == 'Octale':
        nmbr2_value.set(int(n1, 8))

    if Vn1 == 'Binaire' and Vn2 == 'Hexadecimale':
        rp1 = int(n1, 2)
        rp2 = hex(int(rp1)).split('x')[-1]
        nmbr2_value.set(rp2)

    if Vn1 == 'Hexadecimale' and Vn2 == 'Binaire':
        rp1 = int(n1, 16)
        rp2 = bin(int(rp1)).replace("0b", "")
        nmbr2_value.set(rp2)

    if Vn1 == 'Binaire' and Vn2 == 'Octale':
        rp1 = int(n1, 2)
        rp2 = oct(rp1)
        nmbr2_value.set(rp2)

    if Vn1 == 'Octale' and Vn2 == 'Binaire':
        l = []
        nmbr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        o = n1
        rp1 = oct(int(o))
        print(rp1)
        for i in rp1.__str__():
            if i in nmbr:
                l.append(i)
        print(l)
        rp = ''
        for i in l:
            rp += i
        rp2 = bin(int(rp)).replace("0b", "")
        nmbr2_value.set(rp2)
# Label 1 
ttk.Label(window, text="From: ",font=("Times New Roman", 10)).place(x=10, y=50)
# Combobox 1 
nmbr1_name = tk.StringVar()
cmb1 = ttk.Combobox(window, width=20, textvariable=nmbr1_name)
cmb1['values'] = ('Binaire', 'Decimale', 'Hexadecimale', 'Octale')
cmb1.place(x=80, y=50)
cmb1.current()
# Entry 1
nmbr1_value = tk.StringVar()
entry1 = ttk.Entry(window, width=30, textvariable=nmbr1_value)
entry1.place(x=300, y=50)
# Label 2
ttk.Label(window, text="To: ",font=("Times New Roman", 10)).place(x=10, y=100)
# Combobox 2
nmbr2_name = tk.StringVar()
cmb2 = ttk.Combobox(window, width=20, textvariable=nmbr2_name)
cmb2['values'] = ('Binaire', 'Decimale', 'Hexadecimale', 'Octale')
cmb2.place(x=80, y=100)
cmb2.current()
# Entry 2
nmbr2_value = tk.StringVar()
entry2 = ttk.Entry(window, width=30, textvariable=nmbr2_value, state=DISABLED)
entry2.place(x=300, y=100)
conv_btn = ttk.Button(window, text='Convert',command=Convert).place(x=235, y=170)
credit =ttk.Label(window, text="By Ayoub Ech-chetyouy",font=("Times New Roman", 10)).place(x=200, y=230)
window.mainloop()
