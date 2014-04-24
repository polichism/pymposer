#!/usr/bin/env python

__author__ = "Harrie Bos"
__copyright__ = "Copyright 2014, polichism"
__credits__ = []
__license__ = "BSD2"
__version__ = "0.1"
__maintainer__ = "Harrie Bos"
__email__ = "polichism@gmail.com"
__status__ = "Development"

import urllib2
import sys, getopt
import json

REPOSITORIES = ['https://github.com/',]

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "h", [])
		packages = args[1:]
	except getopt.GetoptError:
		print 'pymoposer.py install'
	for opt, arg in opts:
		if opt == '-h':
			print 'pymposer.py install'
			sys.exit(1)
	for arg in args:
		if arg == 'install':
			
			json_handler = JSONHandler();
			json_handler.get_packages()
			print 'searching for packages at GitHub...'
			manager = PacketManager()
			manager.get_packages(packages)
		if arg == 'update':
			print 'Updating packages...'

class PacketManager:
	
	def get_packages(self, packages):
		for package in packages:
			self.download_package(packages)

	def download_package(self, package):
		handler = URLHandler()
		result = handler.check_url('polichism/pymposer')
		print result

class URLHandler:

	def check_url(self, package):
		for repo in REPOSITORIES:
			print 'Searching in %s%s' % (repo, package)
			try: 
				req = urllib2.Request('%s%s' % (repo, package))
				r = urllib2.urlopen(req)
			except urllib2.HTTPError:
				pass
			return req

class JSONHandler:
	import json

	def get_packages(self):
		json_data = self.open_pymposer()
		data = json.load(json_data)
		print data

	def open_pymposer(self):
		try:
			data = open('pymposer.json', 'r')
		except IOError:
			print "pymposer.json not found."
			sys.exit(2)

		return data

if __name__ == "__main__":
	main(sys.argv[1:])
