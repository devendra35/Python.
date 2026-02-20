from tkinter import*
from random import choice
import string

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('password_generator')
        self.window.iconbitmap('')
        self.window.iconphoto(False, PhotoImage(file='')) #add your logo here
        self.window.geometry('500x255')
        self.window.config(bg='gray')
