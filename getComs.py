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
        #Flag when its inside a function
        inFunc = False
        #Output variable, write mode on
        OuFile = open(sys.argv[2], 'w')
        #look at the py file and get what we need
        with open(sys.argv[1],'U') as f:
            for line in f:
                #if inside the function there is the docstring, get it:
                if inFunc == True: 
                    match = re.search("('''.*?''')|(\"\"\".*?\"\"\")", line)
                    inFunc = False
                    if match:
                        print(match.group())
                        OuFile.write(match.group())
                        OuFile.write('\n')
                #if a function declaration we get it and set inside function flag
                if 'def' in line and ':' in line:
                    inFunc = True
                    print("function {} found".format(line.split()[1]))
                    OuFile.write(line.split()[1] + '\n')
                #get comments
                matchHash = re.search("(#.*?\n)", line)
                if matchHash:
                    print(matchHash.group())
                    OuFile.write(matchHash.group())

        f.close()
        OuFile.close()
    #need help?
    else:
        print(Help)
        print(Example)
