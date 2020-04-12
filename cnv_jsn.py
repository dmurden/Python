# Python program to convert text
# file to JSON

import json
from unicodedata import normalize

def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

# the file to be converted
filename = 'C:/Users/duke_/projects/python/dboratab.txt'

# intermediate and resultant dictionaries
# intermediate
dict2 = {}

# resultant
dict1 = {}

# fields in the sample file
fields =['home', 'startup', 'alias', 'typ', 'unk', 'host', 'type', 'charset', 'ver', 'name', 'cont']

with open(filename) as fh:
    
    # loop variable
    i = 0
    
    # count variable for employee id creation
    l = 1
    
    for line in fh:
        
        # reading line by line from the text file
        description = list( line.strip().split(":", 12))
        
        # for output see below
        print(description)
        
        # for automatic creation of id for each employee
        #sno ='DB'+str(l)
        sno = _removeNonAscii(description[0])
        #sno = normalize('NFKD', description[0]).encode('ascii','ignore')
        while i<len(fields):

                # creating dictionary for each employee
                dict2[fields[i]]= description[i+1]
                i = i + 1
                
        # appending the record of each employee to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1

# creating json file
out_file = open("dboratab.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()