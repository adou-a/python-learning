from pyfiglet import Figlet
import sys



n = input('Input:')
figlet =Figlet()

if len(sys.argv) == 1 :
    print(figlet.renderText(n))
elif len(sys.argv) == 3 :
    figlet.setFont(font =sys.argv[2])
    print(figlet.renderText(n))
else:
    sys.exit('Invalid usage')



