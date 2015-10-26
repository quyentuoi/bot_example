from  firefox_decrypt import *
import sys
from sys import stdout as out
from sys import stderr as err
import os
import sqlite3
import json
from ConfigParser import ConfigParser
from base64 import b64decode
from os import path
from ctypes import c_uint, c_void_p, c_char_p, cast, byref, string_at
from ctypes import Structure, CDLL
from getpass import getpass
# global libnss 
# libnss = CDLL("libnss3.so")
print "begin decrypt passwords"
infor = get_information()
# print "information account: {0}".format(infor)
a = format(infor)
print type(a)
print a