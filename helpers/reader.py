import os.path
import json


def reader():
	# read config.json file
	pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../config.json')

	with open(pathname) as file:
		return json.load(file)