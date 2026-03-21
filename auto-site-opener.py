import webbrowser

link = "https://youtu.be/dQw4w9WgXcQ?si=tMc_AlGqoHzgft9b"

print("AUTOMATIC WEBSITE OPENER")
print("")
print("1. Website opener")
print("")
print("2. Click this for surprise")
print("")
print("3. Made by")
print("")
option = input("Choose option: ")

if option == "1":
    url = input("Syötä url: ")
    amount = int(input("Syötä määrä: "))

    for i in range(amount):
        webbrowser.open(url)

elif option == "2":
    webbrowser.open(link)

elif option == "3":
    print("")
    print("Tool is made by MrLizard!")

else:
    print("")
    print("invalid number")
