#!/usr/bin/python
import cgi
import os

debug = True


if debug:
	import cgitb
	cgitb.enable() # Enable pretty errors.

def printForm():
	print "Content-Type: text/html"     # HTML is following
	print                               # blank line, end of headers
	print '''
	<form method ="POST" action="welcome.py">
		<h3>Welcome to welcome.py! "Pie puts the <i>Well</i> in <i>Welcome!</i>"</h3>
		<p>Your first name: <input type="text" name="firstname"></p> 
		<p>Your last name: <input type="text" name="lastname"></p>
		<p>Select skill level: <select name="dropdown">
		<option value="Novice">Novice</option>
		<option value="Some Experience">Some Experience</option>
		<option value="Working Experience">Working Experience</option>
		<option value="Nerd">Nerd</option>
		<option value="Super Nerd">Super Nerd</option></select></p>
		<p>Click to submit: <input type="submit" value="Go"></p>
	</form>'''
	
	return
if os.environ['REQUEST_METHOD'] == 'POST':
	# Get values if they exist
	form = cgi.FieldStorage()

	firstname = form.getvalue("firstname")
	lastname = form.getvalue("lastname")
	exp = form.getvalue("dropdown")
	
	error = []


	# Validate Strings
	if len(str(firstname)) > 30:
		error.append("First name too long")
	if len(str(lastname)) > 30:
		error.append("Last name too long")
	if set('!@#$%^&*()-+`~"1234567890.').intersection(str(firstname)) or set('1234567890!@#$%^&*()-+`~".').intersection(str(lastname)):
		error.append("No special characters or numbers allowed in a name")
	if not lastname and not firstname:
		error.append("You must input a first and last name.")
	elif firstname and not lastname:
		error.append("You must enter a last name.")
	elif lastname and not firstname:
		error.append("You must enter a first name.")
	
	

	if error: # If we have errors, STOP. Print errors and reprint form
		printForm()
		for err in error:
			print '<p style="color:red">', err, '</p>'	

	elif firstname and lastname: # If we have a first and last name and no errors, print out final page.
		print "Content-Type: text/html"     # HTML is following
		print                               # blank line, end of headers
	
		print "<p>Name: ", firstname.upper(), " ", lastname.upper(), "</p>" # Name printed in uppercase as per guidelines
		print "<p>Skill Level: ", exp, "</p>"
		print '<a href="welcome.py">Back</a>' # provide a back button because clicking back doesn't work so well
		
	else:
		os.printForm()
		print '<p style="color:red">Something broke, try again.</p>'
	
elif os.environ['REQUEST_METHOD'] == 'GET':
	printForm()
	
else:
	printForm()