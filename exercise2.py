from pathlib import Path

"""
10-4. Guest: Write a program that prompts
 the user for their name. When they 
 respond, write their name to a file called
guest.txt.
"""

#guest = input("What's your name?: ")
#path = Path("guest.txt")
#path.write_text(guest)

"""
10-5. Guest Book: Write a while loop that 
prompts users for their name. Collect all the 
names that are entered, and then write these 
names to a file called guest_book.txt. Make 
sure each entry appears on a new line in the file.
"""

"""
list1 = []
flag = True
while flag:
    guest = input("What's your name?: ")
    if guest == "q":
        flag = False
    else:
        path = Path("guest.txt")
    #list1.append(guest.title())
        #guest += guest.title() + "\n"
        list1.append(guest.title())
        path.write_text(str(list1))
"""

def second_version():
    invitados = ""
    while True:
        guest = input("What's your name?: ")
        if guest == "q":
            break
        invitados += (f"{guest.title()}\n")

    path = Path("guest.txt")
    path.write_text(invitados)

second_version()
