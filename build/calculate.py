#!/usr/bin/env python3
# -*- using:utf-8 -*-
import linecache
import os
import re
import sys


def txtCheck(fname, check):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))  # ファイル内の最終行の行番号を取得
            lastrow_sen = linecache.getline(fname, lastrow)  # ファイル内の最終行の一行を取得
            if lastrow_sen.find(check) == -1:  # 偽の場合
                print("Please end your task")
                sys.exit()
    except FileNotFoundError as e:
        print(e)


def calculateTime(s_time, e_time):
    result = [
        int(e_time[0]) - int(s_time[0]),
        int(e_time[1]) - int(s_time[1]),
        int(e_time[2]) - int(s_time[2]),
    ]
    if result[2] < 0:
        result[2] = 60 + result[2]
        result[1] -= 1
    if result[1] < 0:
        result[1] = 60 + result[1]
        result[0] -= 1
    if result[0] < 0:
        result[0] = 24 + result[0]
    return result


def startGetTime(fname):
    try:
        if os.path.isfile(fname):
            lastrow = sum(1 for i in open(fname))
            lastrow_sen = linecache.getline(fname, lastrow - 1)
            pattern = r"([0-9]*)"  # 数値にマッチするパターン（0～9の文字(数字)の繰り返し)を定義
            time = re.findall(pattern, lastrow_sen)
    except FileNotFoundError as e:
        print(e)
    result = time[13], time[15], time[17]
    return result


def endGetTime(fname):
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
    path = "../recorder/record.txt"
    txtCheck(path, "end")

    start_time = startGetTime(path)
    end_time = endGetTime(path)
    try:
        with open(path, mode="a") as f:
            task_time = calculateTime(start_time, end_time)

            f.write(
                "task time: "
                + str(task_time[0])
                + ":"
                + str(task_time[1])
                + ":"
                + str(task_time[2])
            )
            f.write("\n----------------------------------\n")
            print(
                "task time: "
                + str(task_time[0])
                + ":"
                + str(task_time[1])
                + ":"
                + str(task_time[2])
            )

    except FileNotFoundError as e:
        print(e)
