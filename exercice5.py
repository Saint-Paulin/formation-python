#!/usr/bin/python3.6
def address(contenu):
    portf = contenu.split(":")
    for portf in contenu:
        if portf[1] == 22:
            print("ssh://portf[0]")
        elif portf[1] == 80:
            print("http://portf[0]")
    return 

port = {
    "ssh": "22",
    "http": "80"
}

with open("exe5.txt", "r") as f:
    contenu = f.read()
print(address(contenu))