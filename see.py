#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
watch value
"""

import os
import sys
import time
from multiAsset import multiAsset

def main(uid):
    while 1:
        # print chr(27) + "[2J"
        # os.system('clear')
        sys.stdout.write("\033[H\033[J" + uid + ' :\n')
        multiAsset.show(uid)
        time.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1])
