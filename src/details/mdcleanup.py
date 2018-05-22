#!/usr/bin/python3


import os, sys

directory = "../details/"
for filename in os.listdir(directory):
    if filename.endswith(".markdown"):
        print(os.path.join(directory, filename))
        infile = open(filename, 'r')
        lines = infile.readlines()
        for line in lines:
            if 'title:' in line:
                title  = line[line.find('"')+1:-2]
                firstline = "**" + title + "**\n"
                title = title.replace(" ", "_")
                title = title + ".md"
                outfile = open(title, 'w')
                outfile.write(firstline)
        for line in lines:
            if "---" not in line:
                if "layout:" not in line:
                    if "title:" not in line:
                        if "date:" not in line:
                            if "tags:" not in line:
                                if "|   STR   |" in line:
                                    outfile.write(line + "  \n")
                                else:
                                    outfile.write(line)
                
    infile.close()
    outfile.close()
