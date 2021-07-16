# -*- coding: utf-8 -*-


with open("output.txt") as fw:
    with open("sample.txt") as fr:
        for line in fr:
            print(line, end="",file=fw)
        