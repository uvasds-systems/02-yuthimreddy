#!/Users/yuthimadireddy/anaconda3/bin/python

import sys

try:
    #do something
    sum = 1 + "3"
except Exception as e:
    #print out the error
    print(e)

#stop the process and exit with a non-zero status
    sys.exit(1)


