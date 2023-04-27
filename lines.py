# Import the required modules for the design of this program
import os
import pyfiglet

# print a welcome words for user
print(pyfiglet.figlet_format("HELLO, ENTER TEXT AS MUCH AS YOU WANT"))

# Open the mylife.txt file for writing
with open('mylife.txt', 'w') as f:
    # Ask user for input until they say no
    while True:
        # Get a line of text from the user
        line = input("\033[35m\nEnter line: ")
       
        # Write the entered line to the file
        f.write(line + '\n')
        
        # Ask if the user wants to enter more lines
        more = input("\033[92mAre there more lines y/n? ")
        if more.lower() != 'y':
            break
       
# Print to notify the user that the file has been saved
print(pyfiglet.figlet_format("File saved!"))
