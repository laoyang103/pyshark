#!/usr/bin/python

import cgi
import cgitb
import subprocess as sp

print "Content-type:text/html\r\n\r\n"

NAME, VALUE = SOCK_ADDR, SOCK_PORT = range(2)
SRCINFO, CONVSTR, DSTINFO, PACKETS_DST2SRC, BYTES_DST2SRC, PACKETS_SRC2DST, BYTES_SRC2DST, PACKETS, BYTES, REL_START, DURATION = range(11)

def conv(filename, flt):
    outconv = []
    if flt and flt != '': flt = ',' + flt 
    if not flt: flt = ''
    p = sp.Popen(['tshark', '-q', '-nn', '-r', './' + filename, '-z', 'conv,tcp' + flt], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)
    
    line = p.stdout.readline()
    while line:
        line = p.stdout.readline()
        if '<->' not in line: continue
        fields = line.split()
        srcsock = fields[SRCINFO].split(':')
        dstsock = fields[DSTINFO].split(':')
        conv = {}
        conv['Address SRC']         = srcsock[SOCK_ADDR]
        conv['Port SRC']            = srcsock[SOCK_PORT]
        conv['Address DST']         = dstsock[SOCK_ADDR]
        conv['Port DST']            = dstsock[SOCK_PORT]
        conv['Total Packets']       = fields[PACKETS]
        conv['Total Bytes']         = fields[BYTES]
        conv['Packets SRC -> DST']  = fields[PACKETS_SRC2DST]
        conv['Bytes SRC -> DST']    = fields[BYTES_SRC2DST]
        conv['Packets DST -> SRC']  = fields[PACKETS_DST2SRC]
        conv['Bytes DST -> SRC']    = fields[BYTES_DST2SRC]
        conv['Rel Start']           = fields[REL_START]
        conv['Duration']            = fields[DURATION]
        outconv.append(conv)
    p.stdout.close()
    p.stdin.close()
    return outconv

def summary(filename):
    outsummary = {}
    p = sp.Popen(['capinfos', './' + filename], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)
    line = p.stdout.readline()
    while line:
        fields = line.split(':', 1)
        outsummary[fields[NAME]] = fields[VALUE].strip()
        line = p.stdout.readline()
    p.stdout.close()
    p.stdin.close()
    return outsummary

form = cgi.FieldStorage()
pflt = form.getvalue('flt')
pfilename = form.getvalue('filename')
pmethod = form.getvalue('method')

if pmethod == 'summary': 
    print summary(pfilename)
elif pmethod == 'conv': 
    print conv(pfilename, pflt)
