import os
import subprocess
import signal

# global variables
file_name = './dungeon4'
user_inputs = ("%p")*4 + ("%s")*2  # Modify this string as needed
command = 'strings ./'+ file_name


def stringCompare(input_string,Output_String):
    if input_string in Output_String:
        print("the word exists in strings")
        print("this is the input string: ",input_string)
        return input_string

    else:
        return None
    
def removeStr(input_string):
    substring_to_remove = "Guard: I am hungry, I want to eat some fruit.."
    new_string = input_string.replace(substring_to_remove, "")

    substring_to_remove = "Guard: So you think I like?"
    new_string = new_string.replace(substring_to_remove, "")

    substring_to_remove = "Guard: You are wrong!"
    new_string = new_string.replace(substring_to_remove, "")

    substring_to_remove = "0x10x10xc000xfc(null)"
    new_string = new_string.replace(substring_to_remove, "")

    substring_to_remove = "\n"
    new_string = new_string.replace(substring_to_remove, "")
    return new_string

def open_executable(input_string):

    try:
        process = subprocess.Popen(
            file_name,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        output, error = process.communicate(input=input_string)
        if error:
            print("Error occurred while executing the file:")
            print(error)
        return output.strip()
    except Exception as e:
        print("An error occurred while executing the file:", str(e))
        return None

def open_executable2(input_strings,input_strings2):
    try:
        process = subprocess.Popen(
            file_name,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        process.stdin.write(str(input_strings))

        #process.stdin.write(str(input_strings2))
        print(input_strings,input_strings2)
        print("test1")
        process.stdin.flush()
        #process.wait()
        print("test2")
        output_lines = []
        for line in process.stdout:
            output_lines.append(line.strip())

        output = '\n'.join(output_lines)
        print(output)
        return output
    except KeyboardInterrupt:
        print("Execution interrupted by user.")
        process.send_signal(signal.SIGINT)  # Send interrupt signal to the subprocess
        process.wait()
        return None
    except Exception as e:
        print("An error occurred while executing the file:", str(e))
        return None

def execute_with_output(input_string):
    global outputComm
    print("Input: ", input_string)
    output = open_executable(input_string)
    new_str = removeStr(output)

    new_str2 = stringCompare(new_str,outputComm)
    if new_str is not None:
        print("Output: \n----------------------\n") 
        print(new_str)
        print("----------------------\n")
        #print("input2:", input_string, new_str)
        #output2 = open_executable2(input_string, new_str) 
        output2 = open_executable(new_str) 

        if output2 is not None:
            print("Output2: \n----------------------\n") 
            print(output2)
            print("----------------------\n")

def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        print("Command execution failed:", str(e))
        return None

# main program
#for input_string in user_inputs:
outputComm = execute_command(command) # first get the output of strings
if outputComm is not None:            # check if there was output
    print("Command output succeeded.", outputComm)

execute_with_output(user_inputs)     # second execute the program
