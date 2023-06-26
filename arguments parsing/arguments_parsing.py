import sys
from getopt import getopt

filename = "test.txt"
message = "Hello"
# print(sys.argv[1:])

opts, args = getopt(sys.argv[1:], "f:m:", ["filename", "message"])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)