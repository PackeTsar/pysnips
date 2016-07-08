#!/usr/bin/python



#####       Written by John W Kerns        #####
#####      http://blog.packetsar.com       #####
#####    https://github.com/packetsar/     #####









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









#######################################################################################################
################################### S T A T U S   R E P O R T E R #####################################
#######################################################################################################

########################################## MESSAGING STANDARD #########################################
##### A standard status message from a "check" method is dictionary formatted as {'status': <pass, warning, or fail>, 'messages': [<list of dicts>]} #####
##### The 'messages' value is a list of dicts. Each dict in the list is formatted as {<OK, WARNING, or FATAL>: <Readable message from the specific check>} #####
#######################################################################################################

##### Report on standard status messages coming from input check functions #####
##### Input argument "statusdata" is a standard check message as defined in the "Messaging Standard" section. #####
##### Input argument "reportlevel" can have values (onfail | onwarning | all) which set the level of report by the function #####
##### Output is a string of prinatable status messages which report on the different checks #####

def status_reporter(statusdata, reportlevel):
	result = "" # Initialize the result string
	for message in statusdata['messages']: # For each message in the messages list
		if list(message)[0] == "FATAL": # If the entry in the message has a key of "FATAL"
			result += list(message)[0] + ": " + message[list(message)[0]] + "\n"
		if list(message)[0] == "WARNING": # If the entry in the message has a key of "WARNING"
			if reportlevel == "onwarning" or reportlevel == "all": # And if we are reporting on warnings or all messages
				result += list(message)[0] + ": " + message[list(message)[0]] + "\n"
		if list(message)[0] == "OK": # If the entry in the message has a key of "OK"
			if reportlevel == "all": # And if we are reporting on all messages
				result += list(message)[0] + ": " + message[list(message)[0]] + "\n"
	return result


########################################## USAGE AND EXAMPLES #########################################
#
#>>> somecheckmessages = {'status': 'fail', 'messages': [{'OK': 'No illegal characters found'}, {'OK': 'Domain total length is good'}, {'OK': 'Domain first character is legal'}, {'FATAL': 'First and last character in domain must be alphanumeric'}, {'OK': 'No labels begin or end with hyphens'}, {'OK': 'No double periods or triple hyphens found'}, {'OK': 'At least one period found in the domain name'}]}
#
#>>> print(status_reporter(somecheckmessages, "all"))
#
#>>> print(status_reporter(somecheckmessages, "onfail"))
#
#######################################################################################################
#######################################################################################################
#######################################################################################################









#######################################################################################################
################################## C H E C K   D O M A I N   N A M E ##################################
#######################################################################################################

##### Check a domain or FQDN host name for legitimacy and proper formatting #####
##### Input "domainname" is a string of the domain name #####
##### Output will be a pass/fail with status messages formatted in the standard messaging format (see "status_reporter" method for more info) #####

import re # Needed for regex checks

def check_domainname(domainname):
	result = {"status": "pass", "messages": []} # Start with a passing result
	##### 1. Check that only legal characters are in name (RFC883 and RFC952) #####
	characterregex = "^[a-zA-Z0-9\-\.]+$" # A list of the valid domain-name characters in a domain name
	for entry in re.findall(characterregex, domainname): # For each string in the list returned by re.findall
		if entry == domainname: # If one of the strings in the returned list equals the full domainname string
			charactercheck = "pass" # Then all its characters are legal and it passes the check
			result["messages"].append({"OK": "No illegal characters found"}) # Append a message to the result
	if charactercheck == "fail": # If the check failed
		result["messages"].append({"FATAL": "Illegal character found. Only a-z, A-Z, 0-9, period (.), and hyphen (-) allowed."})
	##### 2. Check the Length Restrictions: 63 max char per label, 253 max total (RFC1035) #####
	if len(domainname) <= 253: # If total length of domain name is 253 char or less
		result["messages"].append({"OK": "Domain total length is good"})
		labelcheck = {'passlength': 0, 'faillength': 0} # Start a tally of passed and failed labels
		for label in domainname.split("."): # Split the domain into its labels and for each label
			if len(label) <= 63: # If the individual label is less than or equal to 63 characters...
				labelcheck['passlength'] = labelcheck['passlength'] + 1 # Add it as a passed label in the tally
			else: # If it is longer than 63 characters
				labelcheck['faillength'] = labelcheck['faillength'] + 1 # Add it as a failed label in the tally
				result["messages"].append({"FATAL": "Label: " + label + " exceeds max label length of 63 characters"})
		if labelcheck['faillength'] == 0: # If there are NOT any failed labels in the tally
			maxlengthcheck = "pass" # Then all labels are passed and the check passes
	##### 3. Check that first and last character are not a hyphen or period #####
	firstcharregex = "^[a-zA-Z0-9]" # Match a first character of upper or lower A-Z and any digit (no hyphens or periods)
	lastcharregex = "[a-zA-Z0-9]$" # Match a last character of upper or lower A-Z and any digit (no hyphens or periods)
	if len(re.findall(firstcharregex, domainname)) > 0: # If the first characters produces a match
		result["messages"].append({"OK": "Domain first character is legal"})
		if len(re.findall(lastcharregex, domainname)) > 0: # And the last characters produces a match
			result["messages"].append({"OK": "Domain last character is legal"})
			firstlastcheck = "pass" # Then first and last characters are legal and the check passes
		else:
			result["messages"].append({"FATAL": "First and last character in domain must be alphanumeric"})
	else:
		result["messages"].append({"FATAL": "First and last character in domain must be alphanumeric"})
	##### 4. Check that no labels begin or end with hyphens (https://www.icann.org/news/announcement-2000-01-07-en) #####
	beginendhyphenregex = "\.\-|\-\." # Match any instance where a hyphen follows a period or vice-versa
	if len(re.findall(beginendhyphenregex, domainname)) == 0: # If the regex does NOT make a match anywhere
		result["messages"].append({"OK": "No labels begin or end with hyphens"})
		beginendhyphencheck = "pass" # Then no names begin with a hyphen and the check passes
	else:
		result["messages"].append({"FATAL": "Each label in the domain name must begin and end with an alphanumeric character. No hyphens"})
	##### 5. No double periods or triple-hyphens exist (RFC5891 for double-hyphens) #####
	nomultiplesregex = "\.\.|\-\-\-" # Match any instance where a double period (..) or a triple hyphen (---) exist
	if len(re.findall(nomultiplesregex, domainname)) == 0: # If the regex does NOT make a match anywhere
		result["messages"].append({"OK": "No double periods or triple hyphens found"})
		nomultiplescheck = "pass" # Then no double periods or triple hyphens exist and the check passes
	else:
		result["messages"].append({"FATAL": "No double-periods (..) or triple-hyphens (---) allowed in domain name"})
	##### 6. There is at least one period in the domain name #####
	periodinnameregex = "\." # Match any instance of a period
	if len(re.findall(periodinnameregex, domainname)) > 0: # If there is at least one period in the domain name...
		periodinnamecheck = "pass"
		result["messages"].append({"OK": "At least one period found in the domain name"})
	else:
		result["messages"].append({"WARNING": "No period (.) found in domain name. FQDNs are preferred but not required."})
	##### Make sure all checks are passed #####
	for listentry in result["messages"]:
		for key in listentry:
			if key == "FATAL":
				result["status"] = "fail"
	return result

########################################## USAGE AND EXAMPLES #########################################
#
#>>> check_domainname("host.domain.com") # Should pass
#>>> print(status_reporter(check_domainname("host.domain.com"), "all")) # Use reporting method to report on checks
#
#>>> check_domainname("host.dom-ain.com") # Should pass
#>>> print(status_reporter(check_domainname("host.dom-ain.com"), "all")) # Use reporting method to report on checks
#
#>>> check_domainname("host.dom-ain.com-") # Should fail
#>>> print(status_reporter(check_domainname("host.dom-ain.com-"), "all")) # Use reporting method to report on checks
#
#######################################################################################################
#######################################################################################################
#######################################################################################################









#######################################################################################################
################################# C H E C K   I P v 4   A D D R E S S #################################
#######################################################################################################

##### Check that legit IP address or CIDR block was entered #####
##### Input argument "iptype" (str) can be (address | cidr) and argument "ipdata" (str) should be the IP address #####
##### Output will be a pass/fail with status messages formatted in the standard messaging format (see "status_reporter" method for more info) #####

import re

def check_ipv4(iptype, ipdata):
	result = {"status": "", "messages": []} # Initialize result
	if iptype == "address":
		ipregex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
		result["messages"].append({"OK": "IP parsed as type: Address"})
	elif iptype == "cidr":
		ipregex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(?:[0-9]|1[0-9]|2[0-9]|3[0-2]?)$"
		result["messages"].append({"OK": "IP parsed as type: CIDR"})
	check = re.search(ipregex, ipdata)
	if check is None:
		result["status"] = "fail"
		result["messages"].append({"FATAL": "Address failed parsing"})
	else:
		result["status"] = "pass"
		result["messages"].append({"OK": "Address passed parsing"})
	return result

########################################## USAGE AND EXAMPLES #########################################
#
#>>> check_ipv4("address", "1.1.1.100") # Should pass
#>>> print(status_reporter(check_ipv4("address", "1.1.1.100"), "all")) # Use reporting method to report on checks
#
#>>> check_ipv4("address", "1.1.1.256") # Should fail
#>>> print(status_reporter(check_ipv4("address", "1.1.1.256"), "all")) # Use reporting method to report on checks
#
#######################################################################################################
#######################################################################################################
#######################################################################################################









#######################################################################################################
######################################### C H E C K   P A T H #########################################
#######################################################################################################

##### Check a Unix/Linux file or directory path for illegal patterns/characters and for required patterns #####
##### Input "paathtype" argument (str) can be "dir" or "file" (depending on if the input is a file path or a directory path) #####
##### Output will be a pass/fail with status messages formatted in the standard messaging format (see "status_reporter" method for more info) #####

import re # Needed for regex checks

def check_path(pathtype, path):
	result = {"status": "pass", "messages": []} # Start with a passing result
	regexblacklistdict = {"space character": " ", "double forward slash (//)": "\/\/", 'double quote (")': '"', "single quote (')": "'", "pipe character (|)": "\|", "double period (..)": "\.\.", "comma (,)": ",", "exclamation point (!)": "!", "grave accent(`)": "`", "ampersand (&)": "&", "asterisk (*)": "\*", "left parenthesis [(]": "\(", "right parenthesis [)]": "\)"} # Set common blacklist characters and patterns with keys as friendly names and values as the regex patterns
	regexrequiredict = {"begins with /":"^\/"} # Set common required patterns with keys as friendly names and values as the regex patterns
	if pathtype == "dir": # if the path type is "dir"
		regexrequiredict.update({"ends with /": "\/$"}) # add additional patterns to requirements dict
	elif pathtype == "file": # if the path type is "file"
		regexblacklistdict.update({"ends with /": "\/$"}) # add additional patterns to blacklist dict
	for key in regexblacklistdict: # For every entry in the blacklist dict
		if len(re.findall(regexblacklistdict[key], path)) > 0: # If a pattern from the blacklist dict is matched in the path data
			result["status"] = 'fail' # Set the result to fail
			result["messages"].append({"FATAL": "Pattern Not Allowed: " + key}) # Append an error message to a failed result
		else:
			result["messages"].append({"OK": "Pattern Not Found: " + key}) # Append an OK status message
	for key in regexrequiredict: # For every entry in the requirement dict
		if len(re.findall(regexrequiredict[key], path)) == 0: # If the pattern is not found in the path
			result["status"] = 'fail' # Set the result to fail
			result["messages"].append({"FATAL": "Pattern Required: " + key}) # Append an error message to a failed result
		else:
			result["messages"].append({"OK": "Pattern Found: " + key}) # Append an OK status message
	return result

########################################## USAGE AND EXAMPLES #########################################
#
#>>> check_path("file", "/etc/pysnipsdir/somefile") # Should pass
#>>> check_path("file", "/etc/pysnip!sdir/somefile/") # Should fail
#
#>>> print(status_reporter(check_path("file", "/etc/pysnipsdir/somefile"), "all")) # Use reporting method to report on checks (should pass)
#>>> print(status_reporter(check_path("file", "/etc/pysnip!sdir/somefile/"), "all")) # Use reporting method to report on checks (should fail)
#
#######################################################################################################
#######################################################################################################
#######################################################################################################