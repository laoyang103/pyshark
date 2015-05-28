#!/usr/bin/python

import cgi
import cgitb
import pyshark

print "Content-type:text/html\r\n\r\n"

outdict = {}
cap = pyshark.FileCapture('./dns.pcap', display_filter = 'dns', only_summaries = True)

filedict = outdict['File'] = {}
filedict['Name'] = cap.input_filename
filedict['Length'] = 0
filedict['Format'] = 'Wireshark/tcpdump/...-libpcap'
filedict['Encapsulation'] = 'Ethernet'
filedict['Packet size limit'] = '65535 bytes'

timedict = outdict['Time'] = {}
timedict['First packet'] = cap[0].time 
timedict['Last packet'] = 0
timedict['Elapsed'] = 0

print outdict

for pkt in cap:
    print pkt.time

print dir(cap)
print cap.get_parameters()
print cap.tshark_path
print cap.input_filename

