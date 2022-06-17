# CMD script to mass-rename files or change the file extensions

# import sys and getopt lib to work with cmd-arguments
import argparse, pathlib, datetime
import string

# Function to do the automatic renaming of the files in the directory
# Provide the date, name and path of the files
def renamer(datum, name, path):
    filename = datum + name
    for i in len(path):
        filename.append(i + 1)
    print ("I am finished :)")

# Function to change the file extension
def changeExt(path, extension):
    print ("LMAO")

# Creating parser, giving description what the script does
parser = argparse.ArgumentParser(description="Mass rename files or file-extensions in given directory. If no directory is provided, the current will be used. Use the argument '-h' or '--Help' to see all available options.")

# Available Arguments to use with the script
parser.add_argument("-n", "--name", default="Custom_Name", action='store', dest="name", required=True, help="Set the desired name for the files")
parser.add_argument("-p", "--path", default=pathlib.Path(), type=pathlib.Path, action="store", required=True, help="Set the path to the directory you want to rename files")
parser.add_argument("-d", "--date", default=datetime.date.today().strftime("%y_%m_%d"), type=datetime.date, help="Uses today's date as the default, otherwise needs to be input in the format 'YYYY_MM_DD'") 

parser.parse_args()

# Call the renamer function with the argparse arguments and do the renaming
#renamer (parser.date, parser.name, parser.path)