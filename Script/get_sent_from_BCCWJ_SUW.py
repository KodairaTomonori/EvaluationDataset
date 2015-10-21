#!usr/bin/python
#coding:utf-8
import glob
import pickle
import sys


if __name__ == "__main__":
    dir_name = '../Orig_Data/' #sys.args[1]
    
    fnames = sorted(glob.glob(dir_name + '*.txt') )
    for fname in fnames:
        sentences = ''
        print fname
        file_name = fname.split('/')[-1][:-4]
        try:
            fin = open(fname).readlines()
        except:
            print(fname)
            continue
        for line in fin:
            line = line.split('\t')
            try:
                if line[9] == 'B':
                    sentences += '\n'
                sentences += line[22]
            except:
                continue
        pickle.dump(sentences.split('\n'),  open('../Orig_Sent/' + file_name  + '.pkl', 'w') )
