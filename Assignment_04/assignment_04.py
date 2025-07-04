#Task 1: Read a File and Handle Errors
try:
    with open('sample.txt', 'r') as my_file:
        print('Reading file content:')
        for idx, line in enumerate(my_file, start=1):
            print(f'Line {idx}: {line.strip()}')  #.strip() to remove newline \n
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

#Task 2: Write and Append Data to a File
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", 'w') as f:
    f.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

additional_text = input('Enter additional text to append: ')
with open("output.txt", 'a') as f:
    f.write(additional_text + "\n")
    print("Data successfully appended.\n")

print("Final content of output.txt: ")
with open("output.txt", 'r') as f:
    for line in f:
        print(line.strip())
