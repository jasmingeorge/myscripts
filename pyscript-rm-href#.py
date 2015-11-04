import re
import os
import fnmatch

config_path = raw_input("Enter full path : ")
log = open(config_path + '/log.txt', 'w')


def replace_href(file_name):
    log.write(file_name + '\n')
    txt = open(file_name)
    lines = txt.readlines()
    for idx, line in enumerate(lines):
        if len(line) == 0:
            continue
        if ' href="' in line:
            log.write(line)
            line = re.sub(r' href="#?/?[a-z/]*"', "", line)
            log.write("-->" + line)
        lines[idx] = line
    out = open(file_name, 'w')
    lines = ''.join(lines)
    out.write(lines)

for root, dir_names, file in os.walk(config_path):
    for filename in fnmatch.filter(file, '*.html'):
        replace_href(os.path.join(root, filename))
