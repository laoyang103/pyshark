#!/usr/bin/python

import os

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<table border="1">'

for filename in os.listdir('./'):
    if '.pcap' in filename:
        print '<tr>'
        print '<td>' + filename + '</td>'
        print '<td> \
        <form action="read.py" method="POST"> \
            Display Filter: <input type="text" name="flt" /> \
            <input type="hidden" name="filename" value="' + filename + '" /> \
            <input type="submit" value="Submit" /> \
        </form></td>'
        print '</tr>'

print '</table>'
print '</body>'
print '</html>'
