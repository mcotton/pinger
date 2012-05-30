import os
import time

sites = [{'name': 'Greco', 'ip': '192.168.1.1'},
         {'name': 'New Braunfels', 'ip': '192.168.2.1'},
         {'name': 'Floresville', 'ip': '192.168.3.1'},
         {'name': 'Billing', 'ip': '192.168.4.1'},
         {'name': 'Pleasanton', 'ip': '192.168.5.1'},
         {'name': 'Judson', 'ip': '192.168.6.1'},
         {'name': 'Poth', 'ip': '192.168.7.1'},
         {'name': 'Wellness Center', 'ip': '192.168.8.1'},
         {'name': 'Seguin', 'ip': '192.168.9.1'},
         {'name': 'RackSpace', 'ip': '192.168.10.3'}]


def pinger(sites):
	results = '\n************** RESULTS *************************\n\n'

	for s in sites:
		if os.system('ping ' + s['ip']) == 0:
			results = results + '\t' + s['name'] + ' is up\n'
		else:
			results = results + '\t' + s['name'] + '(' + s['ip'] + ')' + ' is down\n'

	print results + '\tClosing in 20 seconds.'

pinger(sites)
time.sleep(20)
