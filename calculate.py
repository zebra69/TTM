#!/usr/bin/env python3
#-*- using:utf-8 -*-
import sys,os,linecache,re

def txtCheck(fname, check):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname)) # ファイル内の最終行の行番号を取得
            lastrow_sen = linecache.getline(fname, lastrow) # ファイル内の最終行の一行を取得
            if lastrow_sen.find( check ) == -1: # 偽の場合
                print('Please end your task')
                sys.exit()
    except FileNotFoundError as e:
        print(e)

def calculateTime(s_time,e_time):
    print(e_time)
    print(s_time)

    result1=int(e_time[0])-int(s_time[0])
    result2=int(e_time[1])-int(s_time[1])
    result3=int(e_time[2])-int(s_time[2])
    print(result1)
    print(result2)
    print(result3)
    if result[0] < 0:
        result[0]=60-result[0]
        result[1]-=1
    if result[1] < 0:
        result[1]=60-result[1]
        result[2]-=1
    if result[2] < 0:
        result[2]=60-result[2]
    print(result)
    return result

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
    path = './recorder/record.txt'
    txtCheck(path,'end')
    
    start_time=getTime(path)
    
    try:
        with open(path, mode='a') as f:
            task_time=calculateTime(start_time,end_time)
            print(task_time)
            f.write("task time: "+task_time[0]+":"+task_time[1]+":"+task_time[2])
            f.write('----------------------------------\n')
            print("task time: "+task_time[0]+":"+task_time[1]+":"+task_time[2])
        
    except FileNotFoundError as e:
        print(e)
