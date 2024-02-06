#!/usr/bin/python3
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
data = load_from_json_file(filename) if exists(filename) else []
data += sys.argv[1:]
save_to_json_file(data, filename)
