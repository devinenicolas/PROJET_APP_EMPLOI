import string
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileReader, PdfFileWriter
#import pikepdf
from string import punctuation
from tkinter import ttk
import os
from tkhtmlview import HTMLLabel

# input interface for CV document

# layout of the interface
root = tk.Tk()
root.geometry("800x550")
root.title('Competences informatiques')
root.font1 = ('arial', 18,'bold')
line1 = tk.Label(root,text="Votre CV")
button1 = tk.Button(root,text="Chargez votre CV au format .txt",width=45,command=lambda:upload_file())
line1.grid(row=2,column=4,columnspan=4)
button1.grid(row=4,column=4,columnspan=4)
#label = HTMLLabel(root, html="<p>Bonjour !</p>")
#label.grid(row=1,column=4,columnspan=1)

#directory = os.getcwd()

# Document upload

def upload_file():
    f_types = [('txt files','*.txt'),('rtf files','*.rtf'),('word files','*.docx'),('pdf files','*.pdf')]
    filename = fd.askopenfilename(filetypes=f_types)

    with open (filename, 'r+', encoding='latin-1') as text_file:
        for line in text_file.readlines():
            text_widget.insert(END,line)

    file_content = filename.read().decode('latin-1')
    words = file_content.split()
    with open('templates/wordscv.txt', 'w') as wordscv:
        for word in wordscv:
            wordscv.write(word + '\n')
    return f'Mots dans le document: {filename}\nFile content: {file_content}'

text_widget = Text(root, width=80, height=20, font=12)
text_widget.grid(row=6,column=4,columnspan=4)

#get individual words from the CV file
text_contents = text_widget.get("1.0", 'end-1c')

punctuation = set(".;,?!:-_\"'\n\t’"+ string.punctuation)
for p in punctuation:
    text_contents = text_contents.replace(p," ")

text_contents = text_contents.lower()

while '  ' in text_contents:
    text_contents = text_contents.replace('  ', ' ')

words = text_contents.split(" ")

words_unique = set(words)

list_words = list(words_unique)

print(list_words)

text_widget_out = Text(root, width=80, height=20, font=12)

for w in words_unique:
    text_widget_out.insert(END,w)

text_widget_out.grid(row=18,column=6,columnspan=4)

root.mainloop()