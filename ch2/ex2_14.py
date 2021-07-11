# -*- coding: utf-8 -*-


f = open("sample.txt")
for line in f:
    line = line.rstrip()
    print(line)
f.close()
