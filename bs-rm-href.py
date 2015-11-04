from bs4 import BeautifulSoup
import os
import fnmatch

config_path = raw_input("Enter full path : ")
log = open(config_path + '/log.txt', 'w')


def replace_href(file_name):
    log.write(file_name + '\n')
    file_data = open(file_name, 'r').read()
    soup = BeautifulSoup(file_data)
    a_tags = soup.findAll('a', {"href": "#"})
    for a_tag in a_tags:
        log.write(str(a_tag))
        fixed_text = str(a_tag).replace(' href="#"', '')
        a_tag.replace_with(fixed_text)
        log.write("-->" + fixed_text)
    html = soup.prettify("utf-8")
    out = open(file_name, 'w')
    out.write(html)

for root, dir_names, files in os.walk(config_path):
    for filename in fnmatch.filter(files, '*.html'):
        replace_href(os.path.join(root, filename))
