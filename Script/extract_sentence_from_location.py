#usr/bin/python
#coding:utf8
import collections
import linecache
import pickle

def read_location_info(fname):
    '''BCCWJのどの位置に欲しい文があるか読み取る。
       データは、file name, line num, target wordの順で並んでる
       keyをファイル名に、あとはvalueに'''
    location_dict = collections.defaultdict(list)
    count = 0
    for line in open(fname):
        file_name, line_num, target_word = line.strip().split(',')
        location_dict[file_name].append((count, line_num, target_word))
        count += 1
    return location_dict


def extract_sentence(location_dict):
    '''作ったディクトの情報からセンテンス抽出'''
    # 2010文を格納するリスト
    sentence_list = ['' for i in range(2010)]
    # テキストがあるディレクトリ
    bccwj_dir = '../BCCWJ/original/'

    for fname in location_dict.keys():
        file_name = bccwj_dir + fname
        for sent_num, line_num, target in location_dict[fname]:
            sentence_list[int(sent_num)] = linecache.getline(file_name, int(line_num))
        linecache.clearcache()
    return sentence_list


if __name__ == '__main__':
    # 文の場所が書いてあるとこ
    location_fname = '../BCCWJ_target_location/location.txt'
    # BCCWJのどのファイル、何行目にあるかを記録してあるディクト
    location_dict = read_location_info(location_fname)
    sentence_list = extract_sentence(location_dict)
    open('sentences.txt', 'w').write(''.join(sentence_list))
    #pickle.dump(sentence_list, open('sentences.pkl', 'w'))
