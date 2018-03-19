#!/usr/bin/python

import argparse 
import socks
import socket
import requests
import sys
sys.tracebacklimit=0

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))

prRed ( 
'''
                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::'' 
''')
prCyan ("	 			CLOUDKiLL3R V1.0")

parser = argparse.ArgumentParser(description="[+] CLOUDKiLL3R is a tool that Helps bypassing CloudFlare Protection Service.[+]")
parser.add_argument("-s", "--scan", type=str, help="-s example.com OR --scan example.com")
parser.add_argument("-a", "--author", help="-a OR --author",  action='store_true')
args = parser.parse_args()


TAGET_URL = args.scan
# Remember to modify either the host or port to be the same TOR Browser.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

if args.scan:
	prRed("	[+] Scanning ..")
	prPurple("	[-]---------------------------[-]")
	prGreen("	[+] TARGET : "+TAGET_URL)
	URL = 'http://www.crimeflare.org/cgi-bin/cfsearch.cgi'
	requests.get(URL)
	payload = {'cfS':TAGET_URL}
	SERVER_RESP = (requests.post(URL, data=payload).text)

	if "these are not CloudFlare-user nameservers" in SERVER_RESP:
		prRed("	[+] "+TAGET_URL+" : IS NOT A CLOUDFLARE USER ")
		prPurple("	[-]---------------------------[-]")
		print "\n\n"
		exit()
	else:
		prGreen("	[+] "+TAGET_URL+" : IS A CLOUDFLARE USER ")
		FILTER = open('FILTER.txt','w')
		FILTER.write(SERVER_RESP)
		FILTER.close()
		
		FILTER2 = open('FILTER.txt','r')
		FILTER2_R = FILTER2.readlines()
		for FILTER2_LINES in FILTER2_R:
			X01 = '<LI>'
			if FILTER2_LINES.startswith(X01):
				SP05 = FILTER2_LINES.split(" ")
				SP05[0]
				SP05[1]
				REAL_IP = SP05[2] 
				SP05[3]
				prGreen("	[+] REAL IP : "+REAL_IP)
				prPurple("	[-]---------------------------[-]")
				print "\n\n"
				exit()
if args.author:
	prGreen("	[+] By MOHAMMED ADEL ")
	prGreen("	[+] github.com/inurlx")
	prGreen("	[+] twitter.com/moh_security")
	print "\n\n"
	exit()
