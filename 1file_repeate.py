#! /usr/bin/env python
# _*_  coding:utf-8 _*_


def clear_repeat():
    current_subdomain_file_handler = open("file2.txt", "r")

    exists_subdomain_array = []

    for i in current_subdomain_file_handler:
        url = i
        if url not in exists_subdomain_array:
            exists_subdomain_array.append(url)
        else:
            print(url)
    f = open('file2_repeate.txt', 'a+')
    f.writelines(exists_subdomain_array)
    f.close()

clear_repeat()