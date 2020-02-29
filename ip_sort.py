#! /usr/bin/env python
# _*_  coding:utf-8 _*_
import re

fie = open("A.txt","r")
new_list = []

for aa in fie:
    new_list.append(aa)

# 排序第一位
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1-i):
        if int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j])[0]) > int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):  # 判断前面的数是否大于后面的数
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # 大于则交换位置


# 排序第二位
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1-i):
        if int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j])[0]) > int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):  # 判断前面的数是否大于后面的数
            if int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # 大于则交换位置

# 排序第三位
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1-i):
        if int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.([0-9]+)\.[0-9]+", new_list[j])[0]) > int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.([0-9]+)\.[0-9]+", new_list[j + 1])[0]):  # 判断前面的数是否大于后面的数
            if int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):
                if int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):  # 判断前面的数是否大于后面的数
                    new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]  # 大于则交换位置

# 排序第四位
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1-i):
        if int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.[0-9]+\.([0-9]+)", new_list[j])[0]) > int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.[0-9]+\.([0-9]+)", new_list[j + 1])[0]):
            if int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*([0-9]+)\.[0-9]+\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):
                if int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*[0-9]+\.([0-9]+)\.[0-9]+\.[0-9]+", new_list[j + 1])[0]):
                    if int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.([0-9]+)\.[0-9]+", new_list[j])[0]) >= int(re.findall(".+IN.*A\D*[0-9]+\.[0-9]+\.([0-9]+)\.[0-9]+", new_list[j + 1])[0]):
                        new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

with open("A2.txt","a+") as f:
    f.writelines(new_list)
