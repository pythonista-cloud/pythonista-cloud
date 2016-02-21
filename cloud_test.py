# coding: utf-8

'''
cloud_test.py

Vision:

- cloud.Import: to make the entry curve to using code hosted on GitHub much easier

Credits:

- cloud.Import: idea and first version by @guerito, future versions on @webmaster4o's GitHub

'''

import os

SITE_DIR = os.path.expanduser('~/Documents/site-packages')

if __name__ == '__main__':
	'''As a test of the system, try to add Gestures to site-packages'''
	filename = 'Gestures'
	filepath = os.path.join(SITE_DIR, filename)
	print('Before: os.path.isfile({}) is {}'.format(filepath, os.path.isfile(filepath)))
	Import(filename)
	print(' After: os.path.isfile({}) is {}'.format(filepath, os.path.isfile(filepath)))
