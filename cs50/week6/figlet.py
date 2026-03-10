import sys
from pyfiglet import Figlet

while (len(sys.argv) != 1 and len(sys.argv) != 3):
    print("Invalid Usage")
    sys.exit
s = input("Enter text: ")
figlet = Figlet()
figlet.getFonts()
if (len(sys.argv) == 3):
    figlet.setFont(font=sys.argv[2])
print(figlet.renderText(s))
