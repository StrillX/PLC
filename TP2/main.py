
from parserPLC import Parser

import sys

parser = Parser()

parser.build()

if len(sys.argv) < 2:
    s = ""
    while linha := input():
        s += linha + "\n"

    programa = parser.parser.parse(s)
    print(programa)
else:
    with open(sys.argv[1],"r") as f:
        programa = parser.parser.parse(f.read())
    if programa:
        with open(sys.argv[1].strip('.\\').split('.')[0]+'.vm','w') as maquina:
            maquina.write(programa)




