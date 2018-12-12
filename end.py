#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

if __name__ == '__main__':
    end = datetime.now()
    print('End your task time.')
    print(end)
    
    path = './recorder/record.txt'
    
    try:
        with open(path, mode='r') as f:
            f.read()

    try:
        with open(path, mode='a') as f:
            f.write('----------------------------------\n')
            f.write("result = ")
    except FileNotFoundError as e:
        print(e)
