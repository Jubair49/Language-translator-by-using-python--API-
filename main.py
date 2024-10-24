from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Create the main window
root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

# Initialize the Translator
translator = Translator()

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    try:
        # Get the text from the source text box
        text_ = text1.get(1.0, END)
        c2 = combo1.get()  # Source language
        c3 = combo2.get()  # Target language

        if text_.strip():  # Check if the text is not empty
            # Detect the source language using googletrans
            detected_lang = translator.detect(text_).lang

            # Get the language code for the target language
            for code, lang in language.items():
                if lang == c3:
                    target_lang = code
                    break

            # Translate the text using googletrans
            translated = translator.translate(text_, src=detected_lang, dest=target_lang)
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Initialize language dictionaries
language = LANGUAGES
languageV = list(language.values())

# Source language combo box
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Frame and text box for the source language
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Target language combo box
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="White", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Frame and text box for the target language
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()


