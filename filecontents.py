#!/usr/bin/python

import cgi
import os
import re

debug = True

if debug:
	import cgitb
	cgitb.enable()
	
# Get cgi fields
args = cgi.FieldStorage()
filename = args.getvalue("filename")
filetest = str(filename)
back = '<a href="listdir.py">Back to listing.</a>'
htmlhead = "Content-Type: text/html"

# Get referer url to validate data.
try:
	ref = os.getenv('HTTP_REFERER').split('/')[-1]
except:
	ref = ""
errors = []


# Tests to make sure the filename is what we want.
try:
	if re.search('/', filename): # Match / to make sure file is inside current directory
		errors.append('No slashes allowed in filename.')
	
	if not filename.split('.')[-1] == 'py': # Match python files
		errors.append('File must be a python file.')		
except:
	errors.append('Something went wrong.') # Added this try statement when testing hex equivalent to the / character. Found that some weird characters would cause the re library to barf and cause the whole string to come back as NoneType causing a plethora of errors. Catching all exceptions.
	
if not ref == 'listdir.py': # Make sure referer is listdir.py
	errors.append('"listdir.py" must send the file.')


if not filename: # Make sure a filename was passed
	errors.append('No file specified.')

# --- End filename tests ---	
	
if len(errors) == 0: # No errors found
	try:
		codefile = open(filename)
		print htmlhead     # HTML is following
		print
		print back
		for line in codefile.readlines():
			print "<pre>" + cgi.escape(line, True) + "</pre>" #Print each line with <pre> tags for code
		print back
			
	except:
		print htmlhead
		print
		print "Error: Cannot open file."
		print back

		
else: # Errors found, print them.
	print htmlhead
	print
	for error in errors:
		print error
	print back
		
	

