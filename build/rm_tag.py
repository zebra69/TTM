#!/usr/bin/env python3
# -*- using:utf-8 -*-
import os
import sys


def rmRecord(fname):
    try:
        if os.path.isfile(fname):
            print("Do you really want to remove all records?(yes/no)")
            heads_up = input(">>")
            if heads_up == "yes":  # 真の場合
                os.remove(fname)
                print("All record removed.")
            else:
                print("Quit this program")
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    fname = sys.argv
    path = "../recorder/" + fname[1]
    print(path)
    if os.path.isfile(path):
        rmRecord(path)
    else:
        print("File is not found.")
