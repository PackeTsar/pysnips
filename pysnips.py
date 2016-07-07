#!/usr/bin/python



#####       Written by John W Kerns        #####
#####      http://blog.packetsar.com       #####
##### https://github.com/PackeTsar/radiuid #####





#######################################################################################################
######################################### M A K E   T A B L E #########################################
#######################################################################################################

##### Create a table of data from a list of dictionaries where the key in each dict is the header and the val is the column value #####
##### The tabledata input is the list of dictionaries and the column order is an ordered list of how the columns should be displayed #####
##### The output is a printable table with automatically spaced columns, centered headers and values #####

def make_table(columnorder, tabledata):
	##### Set seperators and spacers #####
	tablewrap = "#" # The character used to wrap the table
	headsep = "=" # The character used to seperate the headers from the table values
	columnsep = "|" # The character used to seperate each value in the table
	columnspace = "  " # The amount of space between the largest value and its column seperator
	##### Generate a dictionary which contains the length of the longest value or head in each column #####
	datalengthdict = {} # Create the dictionary for storing the longest values
	for columnhead in columnorder: # For each column in the columnorder input
		datalengthdict.update({columnhead: len(columnhead)}) # Create a key in the length dict with a value which is the length of the header
	for row in tabledata: # For each row entry in the tabledata list of dicts
		for item in row: # For column entry in that row
			if len(row[item]) > datalengthdict[item]: # If the length of this column entry is longer than the current longest entry
				datalengthdict[item] = len(row[item]) # Then change the value of entry
	##### Calculate total table width #####
	totalwidth = 0 # Initialize at 0
	for columnwidth in datalengthdict: # For each of the longest column values
		totalwidth += datalengthdict[columnwidth] # Add them all up into the totalwidth variable
	totalwidth += len(columnorder) * len(columnspace) * 2 # Account for double spaces on each side of each column value
	totalwidth += len(columnorder) - 1 # Account for seperators for each row entry minus 1
	totalwidth += 2 # Account for start and end characters for each row
	##### Build Header #####
	result = tablewrap * totalwidth + "\n" + tablewrap # Initialize the result with the top header, line break, and beginning of header line
	columnqty = len(columnorder) # Count number of columns
	for columnhead in columnorder: # For each column header value
		spacing = {"before": 0, "after": 0} # Initialize the before and after spacing for that header value before the columnsep
		spacing["before"] = int((datalengthdict[columnhead] - len(columnhead)) / 2) # Calculate the before spacing
		spacing["after"] = int((datalengthdict[columnhead] - len(columnhead)) - spacing["before"]) # Calculate the after spacing
		result += columnspace + spacing["before"] * " " + columnhead + spacing["after"] * " " + columnspace # Add the header entry with spacing
		if columnqty > 1: # If this is not the last entry
			result += columnsep # Append a column seperator
		del spacing # Remove the spacing variable so it can be used again
		columnqty -= 1 # Remove 1 from the counter to keep track of when we hit the last column
	del columnqty # Remove the column spacing variable so it can be used again
	result += tablewrap + "\n" + tablewrap + headsep * (totalwidth - 2) + tablewrap + "\n" # Add bottom wrapper to header
	##### Build table contents #####
	result += tablewrap # Add the first wrapper of the value table
	for row in tabledata: # For each row (dict) in the tabledata input
		columnqty = len(columnorder) # Set a column counter so we can detect the last entry in this row
		for column in columnorder: # For each value in this row, but using the correct order from column order
			spacing = {"before": 0, "after": 0} # Initialize the before and after spacing for that header value before the columnsep
			spacing["before"] = int((datalengthdict[column] - len(row[column])) / 2) # Calculate the before spacing
			spacing["after"] = int((datalengthdict[column] - len(row[column])) - spacing["before"]) # Calculate the after spacing
			result += columnspace + spacing["before"] * " " + row[column] + spacing["after"] * " " + columnspace # Add the entry to the row with spacing
			if columnqty == 1: # If this is the last entry in this row
				result += tablewrap + "\n" + tablewrap # Add the wrapper, a line break, and start the next row
			else: # If this is not the last entry in the row
				result += columnsep # Add a column seperator
			del spacing # Remove the spacing settings for this entry 
			columnqty -= 1 # Keep count of how many row values are left so we know when we hit the last one
	result += tablewrap * (totalwidth - 1) # When all rows are complete, wrap the table with a trailer
	return result

########################################## USAGE AND EXAMPLES #########################################
#
#>>> tabledataindict = [{"key1": "val111111111", "key2": "val123", "key3": "v"}, {"key1": "val21", "key2": "val22", "key3": "v"}, {"key1": "val31", "key2": "val32", "key3": "va"}, {"key1": "val41", "key2": "val4233", "key3": "va"}, {"key1": "val51", "key2": "val52", "key3": "vasomething longer"}]
#
#>>> ordercolumnslike = ["key1", "key2", "key3"]
#
#>>> print(make_table(ordercolumnslike, tabledataindict))
#
#######################################################################################################
#######################################################################################################
#######################################################################################################









#######################################################################################################
####################################### P R O G R E S S   B A R #######################################
#######################################################################################################

##### Print a useless, but fun progress bar into the console #####
##### Input is a message (string) and the number of seconds the progress bar should last (integer) #####
##### Output will look like: "<message>    [=================                ]" #####

import sys # Needed for stdout
import time # Needed for sleeping between iterations

def progress_bar(message, seconds):
	width = 50 # Set the width (in characters) of the progress bar. Change this as you need.
	timer = float(seconds) / width # Set time (in fraction of seconds) between each bar progression
	currentwhitespace = width # Start with all bar width being whitespace
	currentblackspace = 0 # Start with no blackspace in bar
	while currentwhitespace > -1: # While there is still whitespace in the progress bar, continue adding progress
		sys.stdout.flush() # Clear out stdout to prepare for rewrite of bar
		sys.stdout.write("\r" + message + "    [") # Print beginning of bar
		sys.stdout.write("=" * currentblackspace) # Print the current number of progress icons
		sys.stdout.write(" " * currentwhitespace) # Add the whitespace at the end
		sys.stdout.write("]") # Cap the bar
		currentwhitespace = currentwhitespace - 1 # Remove 1 from the whitespace
		currentblackspace = currentblackspace + 1 # Add 1 to the blackspace
		time.sleep(timer) # Wait for next iteration
	sys.stdout.write("\n") # Print a line break once done

########################################## USAGE AND EXAMPLES #########################################
#
#>>> progress("Deleting All Your Files", 2)
#
#######################################################################################################
#######################################################################################################
#######################################################################################################




