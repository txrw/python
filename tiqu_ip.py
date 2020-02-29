#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import re
import requests
from lxml import etree


def tiqu_ip():
    f = open("A_record.txt", "r")
    for i in f:
        i = i.strip("\n")
        res = re.findall("([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", i)
        for j in res:
            ip_f = open("ip_f.txt", "a+")
            ip_f.write(j)
            ip_f.write('\n')
            ip_f.close()
    clear_repeat()


def clear_repeat():
    current_subdomain_file_handler = open("ip_f.txt", "r")

    exists_subdomain_array = []

    for i in current_subdomain_file_handler:
        url = i
        if url not in exists_subdomain_array:
            exists_subdomain_array.append(url)
    f = open('final_ip.txt', 'a+')
    f.writelines(exists_subdomain_array)
    f.close()
    # checkip()
tiqu_ip()
