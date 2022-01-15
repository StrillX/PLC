
from parserPLC import Parser

import sys

parser = Parser()

parser.build()

if len(sys.argv) < 2:
    s = ""
    while input := input():
        s += input + "\n"

    programa = parser.parser.parse(s)
    print(programa)
else:
    with open(sys.argv[1],"r") as f:
        programa = parser.parser.parse(f.read())
    if programa:
        if len(sys.argv) < 3 :
            with open(sys.argv[1].strip('.\\').split('.')[0]+'.vm') as maquina:
                maquina.write(programa)
        else:
            with open(sys.argv[2], 'w', newline = '\n') as maquina:
                maquina.write(programa)



