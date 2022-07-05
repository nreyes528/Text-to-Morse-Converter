import morse

while True:
    choice = input("Enter '1' for text to morse code conversion\n"
                   "Enter '2' to display image of morse code rules\n"
                   "Enter '3' to exit out of the application\n"
                   "Enter your choice here: ")

    if choice == "1":
        morse.toMorse()
    elif choice == '2':
        morse.show_rules()
    elif choice == '3':
        break
