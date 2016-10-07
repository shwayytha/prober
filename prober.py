'''
Ex1: Monitoring Prober
Author: Shweta Garg
Large Scale Web Apps, Fall 2016
'''

import sys
import time


def probe_server(url):
    

def get_vars():
    if (len(sys.argv < 3)):
        return input("Enter a URL: "), input("Enter a samples file name: ")
    else:
        return sys.argv[1], sys.argv[2]

def main():
    url, samples = get_vars()
    samples_file = open(samples, 'w')
    saved_time = int(time.time())
    while True: # infinite loop until interrupted
        try:
            if (int(time.time()) - saved_time >= 30):
                response = probe_server(url) # sends get request to server, returns a response
                write_line = str(int(time.time())) + "," + str(response) + "\n"
                saved_time = int(time.time())
        except (KeyboardInterrupt, SystemExit):
                file.close()
                break

main()
