import sys
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3 and (
    sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts
):
    sys.exit("Invalid usage")

response = input("Input: ")
figlet.setFont(font=sys.argv[2])
print(figlet.renderText(response))

"""
elif sys.argv[1] not in ['-f', '--font']:
    sys.exit('Invalid argument')
elif sys.argv[2] not in fonts:
    sys.exit('Invalid font name')
"""
