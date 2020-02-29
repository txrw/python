#!/usr/bin/python
# conding=utf-8
import random
import string
from Tkinter import *


def one_str():
    num = string.digits
    str_list = string.ascii_letters
    zifuchuan = num + str_list + '~!>?<,./()[]{}'
    return random.choice(zifuchuan)


def passwd():
    passwd_len = 0
    password = str()
    while passwd_len != 14:
        str1 = one_str()
        password = ''.join([password, str1])
        passwd_len = passwd_len + 1
    return password


def main():
    str2 = passwd()
    length = len(re.findall('\d+', str2))
    while length < 4 or length > 7:
        str2 = passwd()
        length = len(re.findall('\d+', str2))
    v1.set(str2)


def save():
    pas = v1.get()
    use_e2 = e2.get()
    strs = use_e2 + ':' + pas
    fil = v3.get()
    with open(fil, 'a+') as f:
        f.write(strs)
        f.write('\n')
    sys.exit()


window = Tk()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
window.title('pass-creat')
window.geometry('200x150')
s = Scrollbar(window)
T = Text(window, height=4, width=50)
T.grid(row=5,rowspan=4, column=0,columnspan=1, sticky=E)

label = Label(window, text='output')
label.grid(row=1, sticky=W)
label2 = Label(window, text='use')
label2.grid(row=2, column=0, sticky=W)
label3 = Label(window, text='addr')
label3.grid(row=3, column=0, sticky=W)

e = Entry(window, textvariable=v1)
e.grid(row=1, column=1, columnspan=2, sticky=E)
e2 = Entry(window, textvariable=v2)
e2.grid(row=2, column=1, columnspan=2, sticky=E)
e3 = Entry(window, textvariable=v3)
e3.grid(row=3, column=1, columnspan=2, sticky=E)
e3.insert(10, "C:/Users/test/Desktop/passwd.txt")

button = Button(window, text='creat', command=main)
button.grid(row=0, column=1)
button2 = Button(window, text='save', command=save)
button2.grid(row=4, column=2, sticky=E)

window.mainloop()

if __name__ == '__main__':
    main()
