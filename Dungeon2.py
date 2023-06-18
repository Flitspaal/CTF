from pwn import *
import time
import string

# Set up the process
process_path = './dungeon2_2'

input_range = range(10)
foundNumber = False
foundString = False

def numberInput():
	global foundNumber
	for input_1 in input_range:
		for input_2 in input_range:
			p = process(process_path)

			# Receive initial output from the process
			print(p.recvline())

			try:
				# Send the first input to the process
				p.sendline(str(input_1).encode())
				time.sleep(0.1)  # Add a delay to allow the program to process the input

				# Receive further output from the process
				print(p.recvline())

				# Send the second input to the process
				p.sendline(str(input_2).encode())
				time.sleep(0.1)  # Add a delay to allow the program to process the input

				# Receive and print the output from the process
				output = p.recvall()
				print(output)

				# Check if the desired output is found
				if b'JCR(Treasure!)' in output:
					print('Desired output found!')
					print('--- INFO ---')
					print('input_1: ', input_1)
					print('input_2: ', input_2)
					foundNumber = True
					break  # Exit the nested loops
			except BrokenPipeError:
				print('BrokenPipeError: The pipe between the script and the process is broken.')

			# Close the process
			p.close()

		if foundNumber:
			break  # Exit the outer loop

def stringInput():
	global foundString
	try:
		for letter_1 in string.ascii_lowercase:
			for letter_2 in string.ascii_lowercase:
				p = process(process_path)

				# Receive initial output from the process
				print(p.recvline())

				try:
					# Send the first input to the process
					p.sendline(letter_1.encode())
					time.sleep(0.1)  # Add a delay to allow the program to process the input

					# Receive further output from the process
					print(p.recvline())

					# Send the second input to the process
					p.sendline(letter_2.encode())
					time.sleep(0.1)  # Add a delay to allow the program to process the input

					# Receive and print the output from the process
					output = p.recvall()
					print(output)

					# Check if the desired output is found
					if b'JCR(Treasure!)' in output:
						print('Desired output found!')
						print('--- INFO ---')
						print('letter_1: ', letter_1)
						print('letter_2: ', letter_2)
						foundString = True
						break  # Exit the nested loops

					# Check if the program does not accept a letter input
					if b'Guard: Wait, that is not a number. See, I am smart!' in output:
						print('Program does not accept letter input. Exiting.')
						foundString = True
						break  # Exit the nested loops
				except BrokenPipeError:
					print('BrokenPipeError: The pipe between the script and the process is broken.')
					break
					

				# Close the process
				p.close()

			if foundString:
				break  # Exit the outer loop
	except BrokenPipeError:
		print('BrokenPipeError: The pipe between the script and the process is broken.')
		#break			
numberInput()
#stringInput()
