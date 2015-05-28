#!/usr/bin/python

import cgi
import cgitb
import pyshark

print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage()
flt = form.getvalue('flt')
filename = form.getvalue('filename')

cap = pyshark.FileCapture('./' + filename, display_filter = flt, only_summaries = True)

outjson = []
for pkt in cap:
    outjson.append(pkt._fields)

print outjson


# high_layer_idx = len(pkt.layers) - 1
# info = pkt.layers[high_layer_idx]
# 
# lines = info._get_all_field_lines()
# for line in lines:
#     print line 

