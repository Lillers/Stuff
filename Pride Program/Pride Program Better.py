from tkinter import *
import tkinter as tk
import tkinter.simpledialog
def read_from_file():
    with open('C:\\Users\lilil\Documents\Python Programs\Pride Program\Pride Program.txt') as file:
        for line in file:
            line = line.rstrip('/n');
            name,definition = line.split('/');
            dictionary[name] = definition;
def write_to_file(name_name, definition_name):
    with open('C:\\Users\lilil\Documents\Python Programs\Pride Program\Pride Mod List.txt', 'a') as file:
        file.write(' ' + name_name + '/' + definition_name + ' ')
root = tk.Tk()
root.withdraw();
dictionary = {};
read_from_file();
pride_query = tkinter.simpledialog.askstring('Pride', 'Name an LGBTQ+ term!');
pride_query = pride_query.upper()
if pride_query in dictionary:
    result = dictionary[pride_query];
    tkinter.messagebox.showinfo('Definition', pride_query + ' is ' + result);
else:
    new_definition = tkinter.simpledialog.askstring ('Teach me', "I don't know that one. Teach me the definition of " + pride_query + '!')
    dictionary[pride_query] = new_definition
    write_to_file(pride_query, new_definition)
