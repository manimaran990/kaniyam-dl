#!/usr/bin/python
#download all open-source magazines from kaniyam.com
import urllib
import re
import os
import sys

def parser():
  try:
	url='http://www.kaniyam.com/all-releases/'
	ufile=urllib.urlopen(url)
	utext=ufile.read()
	pdf=re.findall(r'\<a\shref="(\S+.pdf)"',utext)
	final=[]
	for file in pdf:
		if file not in final:
			final.append(file)
	books=sorted(final)
	print 'books going to downloaded: '
	for i in books: print i
	return books
  except IOError:
	  print sys.stderr.write()
	  sys.exit(1)

def dloader(books):
  try:
	for pdffile in books:
		print 'Downloading :'+pdffile+' pls.. wait'
		urllib.urlretrieve(pdffile)
		print 'completed :'+pdffile
  except IOError:
	  print 'error downloading file try after sometimes'

def main():
	print 'running.. pls wait'
	books=parser()
	dloader(books)
	print 'happy reading'
	
if __name__=='__main__':
	main()
		

