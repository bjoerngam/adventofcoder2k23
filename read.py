import os
 
filename = "/home/bjoern/Dokumente/AdventOfCode2023/input.txt"
 
def read_file(filename):
    #read file in format string
    if os.path.isfile(filename):
        #open file in read mode
        text_file = open(filename, "r")
        #get the entire string
        data = text_file.read()
    
        #close file
        text_file.close()
        
        return(data)

def only_numbers(content):
    #only the numbers are important
    num = 0
    for c in content:
        if c.isdigit():
            #convert the int to a string
            num = num + int(c)
            
    return num


print (only_numbers(read_file(filename)))
