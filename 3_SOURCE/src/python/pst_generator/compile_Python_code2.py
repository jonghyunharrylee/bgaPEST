from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
	console=['pst_generator.py'],
	zipfile= None,
	options = {
		  "py2exe":{
		  	   "compressed": True,
		  	   "bundle_files": 1
		  	   #"packages": ["sys","os"]
		  	   }
		   }
		)