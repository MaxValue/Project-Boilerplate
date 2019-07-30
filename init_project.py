#!/usr/bin/env python3
# coding: utf-8
#
"""
TODOs:
CURRENT:

LONGTERM:

INFO:

"""

# CONSTANTS HERE

import re, csv, argparse, json, logging
#subprocess, csv, os, random, time, string, re, json, xmlrpc.client, configparser
#from mako.template import Template as mako_Template

parser = argparse.ArgumentParser(argument_default=False, description='Clean raw lab data.')
parser.add_argument('database', nargs='?', default='results.csv', help='The location of the database dump.')
parser.add_argument('--interactive', action='store_true', help='Prompt for all inputs.')
parser.add_argument('--name', help='The name of the project.')
parser.add_argument('--tagline', help='The short description of the project.')
parser.add_argument('--verbose', '-v', action='count', default=0, help='Turn on verbose mode.')
parser.add_argument('--log', help='Logfile path. If omitted, stdout is used.')
parser.add_argument('--debug', '-d', action='store_true', help='Log all messages including debug.')
# parser.add_argument("mandatory", help="A positional mandatory arg.")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-a", "--aaa", action='store_true', help="Either this")
# group.add_argument("-b", "--bbb", action='store_true', help="Or this.")
args = parser.parse_args()
# DEBUG: args = parser.parse_args(["-o","blublub","-a"])
# type=argparse.FileType('w', encoding='UTF-8') to provide the argument as file
# action="store_true" to save the argument as boolean True if it is provided, if not: False

if args.debug:
	loglevel = logging.DEBUG
elif args.verbose:
	loglevel = logging.INFO
else:
	loglevel = logging.WARNING

if args.log:
	logging.basicConfig(filename=args.log, filemode='a', level=loglevel)
else:
	logging.basicConfig(level=loglevel)

config = configparser.ConfigParser()
config.read('example.ini')
config.sections()
# the sections are dicts
config['section'].get('key', fallback='value')
config['section'].getint('key', fallback='value')
config['section'].getfloat('key', fallback='value')
config['section'].getboolean('key', fallback='value')

#$Logic
	#Load data

	#Do something

	#Output into file or stdout

logging.debug("Number %d", numbervar)# For testing
logging.info("String %s", stringvar)# Log additional details
logging.warning()# Something should not be/is not recommended
logging.error()# Something failed
logging.critical()# Something failed but the program can still continue
