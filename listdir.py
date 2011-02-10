#!/usr/bin/python

import cgi
import os
import time
import operator

debug = True

if debug:
	import cgitb
	cgitb.enable()
	
	
def printPage(sort="file"):
	
	dict = {}
	contents = os.listdir(".")
	for file in contents:
		try:
			ext = file.split('.')[-1]
		except:
			ext = ""
		if ext == 'py': #Only list python files
			dict[file] = os.stat(file).st_mtime
		else:
			pass
	
	
	print "Content-Type: text/html"     # HTML is following
	print                               # blank line, end of headers
	print '<div align="center">'
	print '<h3>Alex\'s Python Projects: CS116</h3>'
	print '<table border="1">'
	print "<tr>"
	if sort == "file":
		print '<p><b>Sort:</b> Filename Descending</p>'
		
		
		print '<td><a href="listdir.py?sort=rfile">Name</a></td>'
		print '<td><a href="listdir.py?sort=date">Created/Modified</a></td>'
		print '<td><p>Run</p></td>'
		print "</tr>"
		for file in sorted(dict.keys(),key=str.lower, reverse=False):
			print "<tr>"
			print '<td><p><a href="filecontents.py?filename=' + file + '">', file, '</a></p></td>'
			print "<td><p>", time.ctime(int(dict[file])), "</p></td>"
			print '<td><a href="' + file + '" target="main">View</a>'
			print "</tr>"
			
	elif sort == "rfile":
		print '<p><b>Sort:</b> Filename Ascending</p>'
		
		print '<td><a href="listdir.py?sort=file">Name</a></td>'
		print '<td><a href="listdir.py?sort=date">Created/Modified</a></td>'
		print '<td><p>Run</p></td>'
		print "</tr>"
		for file in sorted(dict.keys(),key=str.lower, reverse=True):
			print "<tr>"
			print '<td><p><a href="filecontents.py?filename=' + file + '">', file, '</a></p></td>'
			print "<td><p>", time.ctime(int(dict[file])), "</p></td>"
			print '<td><a href="' + file + '" target="main">View</a>'
			print "</tr>"
			
	elif sort == "date":
		sorted_d = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)
		print '<p><b>Sort:</b> Created/Modified Descending</p>'
		
		print '<td><a href="listdir.py?sort=file">Name</a></td>'
		print '<td><a href="listdir.py?sort=rdate">Created/Modified</a></td>'
		print '<td><p>Run</p></td>'
		print "</tr>"
		for file, cmtime in sorted_d:
			print "<tr>"
			print '<td><p><a href="filecontents.py?filename=' + file + '">', file, '</a></p></td>'
			print "<td><p>", time.ctime(int(cmtime)), "</p></td>"
			print '<td><a href="' + file + '" target="main">View</a>'
			print "</tr>"
			
	elif sort == "rdate":
		sorted_d = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=False)
		print '<p><b>Sort:</b> Created/Modified Ascending</p>'
		
		print '<td><a href="listdir.py?sort=file">Name</a></td>'
		print '<td><a href="listdir.py?sort=date">Created/Modified</a></td>'
		print '<td><p>Run</p></td>'
		print "</tr>"
		for file, cmtime in sorted_d:
			print "<tr>"
			print '<td><p><a href="filecontents.py?filename=' + file + '">', file, '</a></p></td>'
			print "<td><p>", time.ctime(int(cmtime)), "</p></td>"
			print '<td><a href="' + file + '" target="main">View</a>'
			print "</tr>"
			
	else:
		print '<p><b>Sort:</b> Filename Descending</p>'
		
		print '<td><a href="listdir.py?sort=rfile">Name</a></td>'
		print '<td><a href="listdir.py?sort=date">Created/Modified</a></td>'
		print '<td><p>Run</p></td>'
		print "</tr>"
		for file in sorted(dict.keys(),key=str.lower, reverse=False):
			print "<tr>"
			print '<td><p><a href="filecontents.py?filename=' + file + '">', file, '</a></p></td>'
			print "<td><p>", time.ctime(int(dict[file])), "</p></td>"
			print '<td><a href="' + file + '" target="main">View</a>'
			print "</tr>"

	print "</table>"
	print '<hr width="60%"/>'
	print '<iframe name="main" frameborder="1" width="50%" height="50%" />'
	print '</div>'



form = cgi.FieldStorage()
sort = form.getvalue("sort")
printPage(sort)



	
