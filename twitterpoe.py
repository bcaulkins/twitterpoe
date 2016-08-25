import sys
poem = "theraven.txt"

with open (poem) as rf:
    for line in rf:
        print (line)