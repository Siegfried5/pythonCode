#!/usr/bin/env python

from sys import argv
from py_compile import compile

try:
	print "[+] Compiling", "'%s'..." % argv[1]
	compile(argv[1])
	print "[+] Done Compiling '%s' -> '%sc'" % (argv[1],argv[1])

except Exception as e:
	print "\n[-]",e
