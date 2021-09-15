#!usr/bin/python
#coding:utf-8
import glob
import zipfile
import pickle
import sys
import os
import glob


def extract_sentences(file_name):

    sentences = ''
    count = 0
    for line in open(file_name, 'r'):
        line = line.split('\t')
        try:
            if line[9] == 'B':
                sentences += '\n'
            sentences += line[22]
        except:
            continue
    open(write_directory + file_name.split('/')[-1].split('.')[0] \
        + '.txt', 'w').write(sentences)


if __name__ == "__main__":
    write_directory = '../BCCWJ/original/'
    # make directory
    if  glob.glob(write_directory) == []: os.makedirs(write_directory)
    
    # get_zip files infomation
    file_names = glob.glob(sys.argv[1] + '*/*')
    for file_name in file_names:
        extract_sentences(file_name)

