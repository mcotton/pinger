import os
import time

sites = ['192.168.1.1','192.168.2.1','192.168.3.1','192.168.4.1','192.168.5.1','192.168.6.1','192.168.7.1','192.168.8.1','192.168.9.1', '192.168.10.5']

def pinger(sites):
	results = '\n************** RESULTS *************************\n\n'

	for s in sites:
		if os.system('ping ' + s) == 0:
			results = results + '\t' + s + ' is up\n'
		else:
			results = results + '\t' + s + ' is down\n'

	print results + '\tClosing in 20 seconds.'

pinger(sites)
time.sleep(20)
