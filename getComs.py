#!/usr/bin/env python3
import re
import sys

Help = ("ERROR - Wrong Parameters :\n\t the way to do it is: getComs.py inputfile.py outputfile.txt")

Example="EXAMPLE- ./getComs.py test.py test.txt"


if __name__ == "__main__":
    ''' Program that extracts function names, docstrings and comments from py files'''
    
    #verify 2 arguments
    if (len(sys.argv) == 3):
        print("Opening " + sys.argv[1])
        print("Out is "+ sys.argv[2])
        #Flag dentro de función
        inFunc = False
        #variable salida, modo escritura
        OuFile = open(sys.argv[2], 'w')
        #examinamos el archivo py
        with open(sys.argv[1],'U') as f:
            for line in f:
                #si inicio la función encuentra docstring:
                if inFunc == True: 
                    match = re.search("('''.*?''')", line)
                    inFunc = False
                    print(match)
                    print(type(match))
                #si encontro en la linea declaración de función
                if 'def' in line and ':' in line:
                    inFunc = True

                #if match != None:
                #OuFile.write(match)

        f.close()
        OuFile.close()
    #need help?
    else:
        print(Help)
        print(Example)
