#!/usr/bin/python3
"""
Program: create-table
Decription: creates a Markdown table ready to use in a document
Author: Joachim Ziebs
Version: 0.0.1
Licence: GPL v3 or later
"""

# Imports
import sys

# Function
def create_table(columns, rows, file):
	
    #the base parts
	line = "|"
	space = "   "
	dash = "---"
	fullline = ""
	
    #opening the file if desired by user
	if file !="":
		f = open(file, "w")

	#creating the head of the table
	for i in range(0, columns):
		fullline = fullline + line + space
	fullline = fullline + line
	
	print(fullline)
	if file != "":
		f.write(fullline + "\n")
	fullline = ""
	
	for i in range(0, columns):
		fullline = fullline + line + dash
	fullline = fullline + line
	
	print(fullline)
	if file !="":
		f.write(fullline + "\n")
	fullline = ""	
	
	#creating the rest
	for i in range(1, rows):
		for j in range(0, columns):
			fullline = fullline + line + space
		fullline = fullline + line
		print(fullline)
		if file !="":
		  f.write(fullline + "\n")
		fullline = ""
	
    #close the file
	if file != "":
		f.close()
			
# Main
def main():
    if len(sys.argv) == 3:
      columns = int(sys.argv[1])
      rows = int(sys.argv[2])
      filename = ""
      create_table(columns, rows, filename)
    elif len(sys.argv) == 4:
      columns = int(sys.argv[1])
      rows = int(sys.argv[2])
      filename = sys.argv[3]
      create_table(columns, rows, filename)
    else:
      print("create-table")
      print(("Usage: create-table number_of_columns number_of_rows [filename]"))
    	
    sys.exit(0)

    # Execute!
if __name__ == "__main__":
    main()
