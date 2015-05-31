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
            <input type="text" style="width:100px; height:20px;" name="flt" /> \
            <input type="hidden" name="filename" value="' + filename + '" /> \
            <input type="submit" value="Packets" /> \
        </form></td>'
        print '<td> \
        <form action="statistics.py" method="POST"> \
            <input type="text" style="width:100px; height:20px;" name="flt" /> \
            <input type="hidden" name="filename" value="' + filename + '" /> \
            <input type="hidden" name="method" value="summary" /> \
            <input type="submit" value="Summary" /> \
        </form></td>'
        print '<td> \
        <form action="statistics.py" method="POST"> \
            <input type="text" style="width:100px; height:20px;" name="flt" /> \
            <input type="hidden" name="filename" value="' + filename + '" /> \
            <input type="hidden" name="method" value="conv" /> \
            <input type="submit" value="Conv" /> \
        </form></td>'
        print '<td> \
        <form action="statistics.py" method="POST"> \
            <input type="text" style="width:100px; height:20px;" name="flt" /> \
            <input type="hidden" name="filename" value="' + filename + '" /> \
            <input type="hidden" name="method" value="expertinfo" /> \
            <input type="submit" value="Expertinfo" /> \
        </form></td>'
        print '</tr>'

print '</table>'
print '</body>'
print '</html>'
