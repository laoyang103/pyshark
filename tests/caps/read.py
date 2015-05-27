#!/usr/bin/python

import cgi
import cgitb
import pyshark

form = cgi.FieldStorage()
flt = form.getvalue('flt')

print "Content-type:text/html\r\n\r\n"

cap = pyshark.FileCapture('./web.pcap', display_filter = flt, only_summaries = True)
#cap = pyshark.FileCapture('./web.pcap', only_summaries=True)


for pkt in cap:
    print pkt._fields


# high_layer_idx = len(pkt.layers) - 1
# info = pkt.layers[high_layer_idx]
# 
# lines = info._get_all_field_lines()
# for line in lines:
#     print line 

