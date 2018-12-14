#!/usr/bin/env python3
#-*- using:utf-8 -*-
import sys,os,linecache

def rmRecord(fname):
    try:
        if os.path.isfile(fname):
            print('Do you really want to remove all records?(yes/no)')
            heads_up = input('>>')
            if heads_up  == 'yes': # 真の場合
                os.remove(fname)
                f = open(fname, 'w') # ファイルを開く(該当ファイルがなければ新規作成)
                f.close()
                print('All record removed.')
            else:
                print('Quit this program')
                sys.exit()
    except FileNotFoundError as e:
        print(e)
            
if __name__ == '__main__':
    path = '../recorder/record.txt'
    rmRecord(path)

