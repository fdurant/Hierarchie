import sys
import codecs
import json
from pprint import pprint

infile = sys.argv[1]

print infile

with open(infile, "rb") as f:
    j = json.loads(f.read())

pprint(j)
