#!/usr/bin/env python
# -*- coding: utf-8 -*-

import translator
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

translateObj = translator.HebrewTranslator()

root = Tk()
root.geometry("400x500")
root.state("zoomed")
root.title("Hebrew Translator EZ")

lb1 = Label(text="Enter your hebrew word: ")
ent1 = Entry(width=20)
listbox1 = Listbox(root, bg="white", fg="black")

translated_list_box = Listbox(root, bg="white", fg="black")
lb2 = Label(text="Translated words: ")

load = Image.open("keyboard.jpg")
render = ImageTk.PhotoImage(load)

keyboard_virtual = Label(root, image=render)
keyboard_virtual.image = render

list_of_words = []
translated_words = []


def clear_list():
    list_of_words.clear()
    listbox1.delete(0, END)
    translated_list_box.delete(0, END)


def insert_word():
    if ent1.get() not in list_of_words:
        list_of_words.append(ent1.get())
        listbox1.insert(END, ent1.get() + "\n")
    else:
        messagebox.showerror(title="Error", message="This entry already exists in the list!")

    print(list_of_words)


def translate_list():
    for item in list_of_words:
        translated = translateObj.translate(item)
        translated_list_box.insert(END, translated)


btn1 = Button(text="Add to list", command=insert_word)
btn_translate = Button(text="Translate All!", command=translate_list)

btn_clear_list = Button(text="CLEAR LISTS", command=clear_list)

listbox1.insert(1, "")

lb1.pack()

ent1.pack()
btn1.pack()

listbox1.pack()
btn_translate.pack()
lb2.pack()

translated_list_box.pack()

btn_clear_list.pack()

keyboard_virtual.place(x=0, y=0)

root.mainloop()