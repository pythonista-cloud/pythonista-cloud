# coding: utf-8

'''
cloud.py - import code from a remote repository with ease. Designed to be run
from Pythonista.
'''
# Idea and initial implementation by Tony Kainos (@guerito), all further
# development by Luke Taylor.

import sys

import requests


class Cloud(object):
    def __init__(self):
        self.__doc__ = __doc__

    def __getattr__(self, key):
        r = requests.get("http://pythonista.cloud/?module={}".format(key))
        return r.text

if __name__ != "__main__":
    sys.modules[__name__] = Cloud()
