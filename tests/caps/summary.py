#!/usr/bin/python

import os
import cgi
import cgitb
import pyshark
import time 
import datetime 

def timestamp2date(timestamp):
    timearray = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timearray)

outdict = {}
print "Content-type:text/html\r\n\r\n"

form = cgi.FieldStorage()
flt = form.getvalue('flt')
filename = form.getvalue('filename')
cap = pyshark.FileCapture('./' + filename, display_filter = flt, only_summaries = True)

filedict = outdict['File'] = {}
filedict['Name'] = cap.input_filename
filedict['Length'] = str(os.path.getsize(cap.input_filename)) + " bytes"
filedict['Format'] = 'Wireshark/tcpdump/...-libpcap'
filedict['Encapsulation'] = 'Ethernet'
filedict['Packet size limit'] = '65535 bytes'

num_packets = 0
num_bytes = 0
for pkt in cap:
    num_packets += 1
    num_bytes += int(pkt._fields['Length'])
elapsed_sec = round(float(pkt.time) - float(cap[0].time), 3)

traffic_dict = outdict['Traffic'] = {}
traffic_dict['Bytes'] = num_bytes
traffic_dict['Packets'] = num_packets
traffic_dict['Between first and last packet'] = str(elapsed_sec) + " sec"
traffic_dict['Avg.packets/sec'] = round(float(num_packets) / elapsed_sec, 3)
traffic_dict['Avg.packet size'] = str(round(float(num_bytes) / num_packets, 3)) + " bytes"
traffic_dict['Avg.bytes/sec']   = round(float(num_bytes) / elapsed_sec, 3)
traffic_dict['Avg.MBit/sec']    = round(float(num_bytes << 3) / 1048576 / elapsed_sec, 3)

timedict = outdict['Time'] = {}
timedict['First packet'] = timestamp2date(float(cap[0].time))
timedict['Last packet'] = timestamp2date(float(pkt.time))
timedict['Elapsed'] = str(datetime.timedelta(seconds = int(elapsed_sec)))

print outdict

