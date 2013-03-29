#!/usr/bin/python
#download all open-source magazines from kaniyam.com
import urllib
import re
import os
import sys
kaniyam=[] #list stores the only kaniyam releases
spec=[] #stores special releases
#parsed function will fetch the internet and
#read all the available links.
#stores kaniyam, and spec list
#return list of all books
def parser():
  try:
	print 'fetching pls.. wait...'
	url='http://www.kaniyam.com/all-releases/'
	ufile=urllib.urlopen(url)
	utext=ufile.read()
	pdf=re.findall(r'\<a\shref="(\S+.pdf)"',utext)
	final=[]
	latest=[]
	for file in pdf:
		if file not in final:
			final.append(file)
	for f in final:
		if 'kaniyam-' in f:
			kaniyam.append(f)
		else:
			spec.append(f)
	return final
	
  except IOError:
	  print sys.stderr.write()
	  sys.exit(1)
	  
#bulk function will download all the pdf
def bulk(books):
	print 'books going to be downloaded: '
	sortbook=sorted(books)
	for i in sortbook: print i
	dloader(sortbook)
	

#this will download only a latest release
def single(kaniyam):
	first=[]
	first.append(kaniyam[0])
	print 'downloading latest release: \n'
	dloader(first)
#downloads special editions
def special(spec):
	print 'downloading special editions:'
	dloader(spec)
#downloader function helps to download urls
#feeded by list of urls
def dloader(books):
  try:
	for pdffile in books:
		print 'Downloading :'+pdffile+' pls.. wait'
		urllib.urlretrieve(pdffile)
		print 'completed :'+pdffile
  except (KeyboardInterrupt, IOError):
	  print 'download failure.. :('

def main():
 
 books=parser()
 loop=True
 while loop == True:
        res=str(raw_input('''
 (1) latest magazine
 (2) all magazines
 (3) special releases 
 (4) exit
  =>'''))
	if res=='1':
		single(kaniyam)
	elif res=='2':
		bulk(books)
	elif res=='3':
		special(spec)
	elif res=='4':
		print 'thank you'
		loop=False	
	
if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		print 'aborted by user'
		

