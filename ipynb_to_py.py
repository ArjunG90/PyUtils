import json
import os
import sys

# Convert unicode to ascii format
def utoa(input, strtype='utf-8'):
    if isinstance(input, unicode):
        return input.encode(strtype)
    elif isinstance(input,list):
        return [utoa(val,strtype) for val in input]
    elif isinstance(input,dict):
        return {utoa(key,strtype):utoa(val,strtype) for key,val in input.items()}
    return input

# Convert a single .ipynb file to a python file.
def convertfiletopy(file):
    contents = utoa(json.load(open(file)))
    sheet = contents['cells']
    codes = [cell['source'] for cell in sheet]
    
    vals = ["".join(code) for code in codes]
    with open(file + '.py','w') as f:
        for code in vals: 
            f.write(code)
            f.write('\n#-------------\n')

# Convert all .ipynb files in the directory to python files.            
def convertindir(drctry):
    ipynbfiles = [drctry+"\\"+ filename for filename in os.listdir(drctry) if filename.endswith('.ipynb')]
    for file in ipynbfiles: convertfiletopy(file)
    
def convert(arg):
    '''
    Given an argument, see if it is a file or directory, and convert accordingly.
    The new filenames are of the form <old_filename>.py
    '''
    if arg.endswith('.ipynb'): convertfiletopy(arg)
    else: convertindir(arg)
        
# Test
if __name__ == "__main__":
    convert(sys.argv[1])

