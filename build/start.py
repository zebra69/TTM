#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import linecache
import os
import sys
from datetime import datetime


def txtCheck(fname, check):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))  # ファイル内の最終行の行番号を取得
            lastrow_sen = linecache.getline(fname, lastrow)  # ファイル内の最終行の一行を取得
            if lastrow_sen.find(check) == 0:  # 真の場合
                print("The last task is not closed")
                sys.exit()
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    start = datetime.now()

    path = "../recorder/record.txt"

    txtCheck(path, "start")

    print("Start your task.")
    print(start)

    try:
        with open(path, mode="a") as f:
            # f.write('----------------------------------\n')
            f.write("start: " + str(start) + "\n")
    except FileNotFoundError as e:
        print(e)
