#!usr/bin/python
#coding:utf-8
import glob
import zipfile
import pickle
import sys
import os
import glob


def extract_sentences(zfile_name):
    ''' extract sentences from BCCWJ/SUW/*.zip'''
    # get zip files infomation
    zip_file = zipfile.ZipFile(zfile_name, 'r')
    
    # extract sentences from BCCWJ
    for file_name in sorted(zip_file.namelist()):
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
        open(write_directory + file_name.split('/')[-1].split('.')[0] \
            + '.txt', 'w').write(sentences)


if __name__ == "__main__":
    write_directory = '../BCCWJ/original/'
    # make directory
    if  glob.glob(write_directory) == []: os.makedirs(write_directory)
    
    # get_zip files infomation
    zfile_names = glob.glob(sys.argv[1] + '*/*.zip')
    for zfile_name in zfile_names:
        extract_sentences(zfile_name)

