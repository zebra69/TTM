#!/usr/bin/env python3
# -*- using:utf-8 -*-
import os
import sys


def txtMake(fname):
    path = "../recorder/" + fname
    if os.path.exists(path):
        print("You already created the tag.")
        sys.exit()
    else:
        f = open(path, "w")
        f.close()
        print(fname + " was successfully created.")


if __name__ == "__main__":
    fname = sys.argv
    txtMake(fname[1])
