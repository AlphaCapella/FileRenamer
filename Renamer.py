import sys

print ("Welcome. This script helps with mass-renaming of files")
print ("You have the option to rename files or change the file extension. What would you like me to do?")
print ("To rename files, enter: 1")
print ("To change the file extension, enter: 2")

print ("Option: ")
selection = input()

if selection == 1:
    print ("LMAO")
elif selection == 2:
    print ("ROFL")
else: 
    print ("Enter 1 for file renaming and 2 for file extension. 0 to quit")
    selection = input()
    if selection == 0:
        sys.exit("Bye Bye :)")