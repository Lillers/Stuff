from tkinter import *
import tkinter as tk
import tkinter.simpledialog
def read_from_file():
    with open('Pride Program.txt', 'r')as file:
        for line in file:
            line = line.rstrip('/n');
            name,definition = line.split('/');
            dictionary[name] = definition;
def write_to_file(name_name, definition_name):
    with open('Pride Program.txt', 'a') as file:
        file.write('/n'+ name_name + '/' + definition_name);
root = tk.Tk();
root.withdraw();
dictionary = {};
read_from_file();
pride_query = simpledialog.askstring('Pride', 'Name an LGBTQ+ term!');
if pride_query in dictionary:
    result = dictionary[pride_query];
    messagebox.showinfo('Definition', result);
