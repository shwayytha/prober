The prober was written using Python 3.5.

BUILDING AND RUNNING THE PROBER:
Running the prober by command line - The prober will take 4 arguments to run. The first is "python3". This cannot be just python otherwise it won't import the modules used. The second is the name of the prober file with the code, which is "prober.py" in this case. The third argument is the URL of the website. It must have the prefix "http://" in order to run (so it cannot start with "www" or "https://") and it must expect port 80. The last argument is a path to the file that will be created to contain the probing samples. The first line will specify the url used and then each line after that will have one line for each sample.
For example, a possible invocation is:
python3 prober.py http://www.cs.nyu.edu output.txt

Running the prober by Python IDE - Run the program. It will prompt the user for a URL and an output file path where it will write to.

HTTP redirects:
The prober does not report the original HTTP request. Instead, it follows the redirects to the ultimate targer and reports the response from that URL. It should report 200 if the site is not down.
