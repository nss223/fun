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

import sys
import time
from multiAsset import multiAsset

def main(uid):
    while 1:
        print(chr(27) + "[2J")
        print uid, ':'
        multiAsset.show(uid)
        time.sleep(3)

if __name__ == '__main__':
    main(sys.argv[1])
