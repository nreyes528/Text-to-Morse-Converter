from tkinter import *

"""
International Morse Code Conventions (with modifications for program)
1. The length of a dot is one unit
2. A dash is three units (one dash '-' is considered one unit for this program instead of 3 units)
3. The space between letters is three units
4. The space between words is seven units (one forward slash '/' equates to 7 units of space)
Source: https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg
"""

morse_dict = {
    "A": ". -",
    "B": "- . . .",
    "C": "- . - .",
    "D": "- . .",
    "E": ".",
    "F": ". . - .",
    "G": "- - .",
    "H": ". . . .",
    "I": ". .",
    "J": ". - - -",
    "K": "- . -",
    "L": ". - . .",
    "M": "- -",
    "N": "- .",
    "O": "- - -",
    "P": ". - - .",
    "Q": "- - .",
    "R": ". - .",
    "S": ". . .",
    "T": "-",
    "U": ". . -",
    "V": ". . . -",
    "W": ". - -",
    "X": "- . . -",
    "Y": "- . - -",
    "Z": "- - . .",
    "1": ". - - - -",
    "2": ". . - - -",
    "3": ". . . - -",
    "4": ". . . . -",
    "5": ". . . . .",
    "6": "- . . . .",
    "7": "- - . . .",
    "8": "- - - . .",
    "9": "- - - - .",
    "0": "- - - - -"
}


def toMorse():
    text = input("Enter text to be converted to morse code: ")

    words = text.split()
    code = []

    for word in words:
        code.append(convert_word(word))

    morse_code = "/".join(code)
    print(morse_code)


def convert_word(word):
    letters = list(word)
    morse_word = []

    for letter in letters:
        morse_word.append(morse_dict[letter.upper()])

    return "   ".join(morse_word)


def show_rules():
    root = Tk()

    canvas = Canvas(root, width=900, height=1100, bg='white')
    canvas.grid(row=2, column=3)

    img = PhotoImage(file="images/MorseCodeConventions.png")
    canvas.create_image(20, 20, anchor=NW, image=img)

    print("close image to continue...")
    mainloop()
