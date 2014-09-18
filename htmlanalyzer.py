#!/usr/bin/python
#
# HTML source analyzer
#
import sys

def main():
    _file = open(sys.argv[1], "r")
    i = 0
    print "HTML Analyze"
    print "============"
    print
    for _line in _file:
        i = i + 1
        _analyzeLine(_line, i)
        
        
def _analyzeLine(_line, i):
    if "<!--" in _line:
        print "comment found in line %d" % (i)
    
# main program
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print "input HTML file name"