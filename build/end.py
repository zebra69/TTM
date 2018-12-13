#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import sys,os,linecache,re

def txtCheck(fname, check):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname)) # ファイル内の最終行の行番号を取得
            lastrow_sen = linecache.getline(fname, lastrow) # ファイル内の最終行の一行を取得
            if lastrow_sen.find( check ) == -1: # 偽の場合
                print('Please start your task')
                sys.exit()
    except FileNotFoundError as e:
        print(e)


def getTime(fname):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))
            lastrow_sen = linecache.getline(fname,lastrow) 
            pattern=r'([0-9]*)'#数値にマッチするパターン（0～9の文字(数字)の繰り返し)を定義
            time=re.findall(pattern,lastrow_sen)
    except FileNotFoundError as e:
        print(e)
    result = time[13],time[15],time[17]
    return result




if __name__ == '__main__':
    path = '../recorder/record.txt'
    txtCheck(path,'start')
    
    start_time=getTime(path)
    end = datetime.now()
    print('End your task.')
    print(end)
    
    try:
        with open(path, mode='a') as f:
            f.write("end:   "+str(end)+'\n')
            end_time=getTime(path)
        '''
        task_time=calculateTime(start_time,end_time)
        print(task_time)
        with open(path, mode='a') as f:
            f.write("task time: "+task_time[0]+":"+task_time[1]+":"+task_time[2])
            f.write('----------------------------------\n')
        print("task time: "+task_time[0]+":"+task_time[1]+":"+task_time[2])
        '''
    except FileNotFoundError as e:
        print(e)
