#!usr/bin/python
#coding:utf-8
import glob
import zipfile
import pickle
import sys

if __name__ == "__main__":
    # zip_files
    dir_name = sys.args[1] # BCCWJ/SUW/
    zip_file = zipfile.ZipFile(dir_name + '*/*.zip', 'r')
    count = 0
    for file_name in sorted(zip_file.namelist() ):
        sentences = ''
        count = 0
        for line in zip_file.open(file_name, 'r'):
            line = line.split('\t')
            try:
                if line[9] == 'B':
                    sentences += '\n'
                sentences += line[22]
            except:
                continue
        open('../BCCWJ/original/' + file_name.split('/')[-1].split('.')[0] \
            + '.txt', 'w').write(sentences)
