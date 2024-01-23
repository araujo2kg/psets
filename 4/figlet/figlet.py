import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    inp = input("Input: ")
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(inp))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            inp = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(inp))
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
