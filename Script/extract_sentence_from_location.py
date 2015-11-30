#usr/bin/python
#coding:utf8
import collections
import linecache
import pickle
import os
import glob

def read_location_info(fname):
    '''read location info and return info as dictionary
       data: file name, line num, target word, etc
       key: file name、value: count + others '''

    location_dict = collections.defaultdict(list)
    count = 0
    for line in open(fname):
        file_name, line_num, target_word = line.strip().split(',')[1:4]
        location_dict[file_name].append((count, line_num, target_word))
        count += 1
    return location_dict


def extract_sentence(location_dict):
    '''extract sentences from extracted sentences from BCCWJ'''
    sentence_list = ['' for i in range(2010)]
    bccwj_dir = '../BCCWJ/original/'

    for fname in location_dict.keys():
        file_name = bccwj_dir + fname
        for sent_num, line_num, target in location_dict[fname]:
            sentence_list[int(sent_num)] = linecache.getline(file_name, int(line_num))
        linecache.clearcache()
    return sentence_list


if __name__ == '__main__':
    location_fname = '../BCCWJ_target_location/location.txt'
    
    location_dict = read_location_info(location_fname)
    sentence_list = extract_sentence(location_dict)
    sentence_list = map(lambda x: x.strip() + '\n', sentence_list)

    write_directory = '../Sentence/'
    if  glob.glob(write_directory) == []: os.makedirs(write_directory)
    open(write_directory + 'sentences.txt', 'w').write(''.join(sentence_list))
