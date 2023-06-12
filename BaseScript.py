import subprocess
import binascii

program_path = "file.exe"

user_inputs = ""

# Execute the program and retrieve the output
def execute_program(input_string):
    cmd = [program_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Provide the user input to the program
    process.stdin.write(input_string.encode())
    process.stdin.flush()

    # Wait for the program to finish
    process.wait()

    # Retrieve the program's output
    output = process.stdout.read().decode()
    return output

def execute_with_input(input_string):
    print("input: ", input_string)
    output = execute_program(input_string)
    print("Output: \n----------------------\n") 
    print(output)
    print("----------------------\n")

for input_string in user_inputs:
    execute_with_input(input_string)
