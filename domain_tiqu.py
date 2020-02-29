#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import re


def domain_tiqu():
    f = open("domain_tiqu.txt", "r")
    for i in f:
        i = i.strip("\n")
        #res = re.findall('(.+\.jianke\.com)', i, re.I)
        res = re.findall(r'(.+\.jianke\.com\.\s+[0-9]+\s+IN.*A.*[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', i)
        for j in res:
            ip_f = open("domain_tiqu_result.txt", "a+")
            ip_f.write(j)
            ip_f.write('\n')
            ip_f.close()
    clear_repeat()


def clear_repeat():
    current_subdomain_file_handler = open("domain_tiqu_result.txt", "r")

    exists_subdomain_array = []

    for i in current_subdomain_file_handler:
        url = i
        if url not in exists_subdomain_array:
            exists_subdomain_array.append(url)
    f = open('domain_tiqu_result2.txt', 'a+')
    f.writelines(exists_subdomain_array)
    f.close()
domain_tiqu()
