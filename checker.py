import pycurl
import sys
from StringIO import StringIO
inputfile = str(sys.argv[1])
newfile = open(inputfile)
file = newfile.readlines()
def checkaddress(file):
        counter = 0
        while counter < len(file)-1:
                buffer = StringIO()
                c = pycurl.Curl()
                print "Checking URL: " + file[counter]
                c.setopt(c.URL, file[counter].rstrip())
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                print "status code: %s" % c.getinfo(pycurl.HTTP_CODE)
                counter += 1
        c.close()
checkaddress(file)
