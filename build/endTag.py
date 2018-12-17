#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import linecache
import os
import re
import sys
from datetime import datetime


def txtCheck(fname, check):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))  # ファイル内の最終行の行番号を取得
            lastrow_sen = linecache.getline(fname, lastrow)  # ファイル内の最終行の一行を取得
            if lastrow_sen.find(check) == -1:  # 偽の場合
                print("Please start your task")
                sys.exit()
    except FileNotFoundError:
        print(fname + " was not created.")


def getTime(fname):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))
            lastrow_sen = linecache.getline(fname, lastrow)
            pattern = r"([0-9]*)"  # 数値にマッチするパターン（0～9の文字(数字)の繰り返し)を定義
            time = re.findall(pattern, lastrow_sen)
    except FileNotFoundError as e:
        print(e)
    result = time[13], time[15], time[17]
    return result


if __name__ == "__main__":
    fname = sys.argv
    path = "../recorder/" + fname[1]

    if os.path.isfile(path):

        txtCheck(path, "start")
        start_time = getTime(path)
        end = datetime.now()
        print("End your task.")
        print(end)

        try:
            with open(path, mode="a") as f:
                f.write("end:   " + str(end) + "\n")
                end_time = getTime(path)
        except FileNotFoundError as e:
            print(e)

    else:
        print(fname[1] + " was not created")
        print("option:ttm --tag(-t) Tag")
