'''
Ex1: Monitoring Prober
Author: Shweta Garg
Large Scale Web Apps, Fall 2016
'''

import sys
import time
import urllib.request
import urllib.error



def probe_server(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request).status
        return response
    except urllib.error.HTTPError:
        return -1
    except urllib.error.URLError:
        return -1
    except Exception:
        return -1

def get_vars():
    if (len(sys.argv) < 3):
        return input("Enter a URL: "), input("Enter a samples file name: ")
    else:
        return sys.argv[1], sys.argv[2]

def main():
    url, samples = get_vars()
    samples_file = open(samples, 'w')
    samples_file.write("URL = " + url + "\n")
    current_time = int(time.time())
    while True: # infinite loop until interrupted
        try:
            if (int(time.time()) - current_time >= 30):
                response = probe_server(url) 
#                print(response)
                write_line = str(int(time.time())) + ", " + str(response) + "\n"
                samples_file.write(write_line)
                samples_file.flush() # prints immediately to file
                current_time = int(time.time())                   
        except (KeyboardInterrupt, SystemExit):
                samples_file.close()
                break

main()
