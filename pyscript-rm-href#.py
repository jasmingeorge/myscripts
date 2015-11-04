import re 
import os
import fnmatch

config_path = raw_input("Enter full path : ")
log = open(config_path + '/log.txt', 'w')

def replace_href(file):
	log.write(file + '\n')
	txt = open(file)
	lines = txt.readlines()
	for idx, line in enumerate(lines):
		if len(line) == 0:
			continue
		if re.match(".*<a.*", line):
			log.write(line)
			if ' href="#"' in line:
				line = line.replace(' href="#"', "")
				log.write("-->" + line) 
		lines[idx] = line
	out = open(file, 'w')
	lines = ''.join(lines)
	out.write(lines)

for root, dirnames, file in os.walk(config_path):
	for filename in fnmatch.filter(file, '*.html'):
		replace_href(os.path.join(root, filename))
