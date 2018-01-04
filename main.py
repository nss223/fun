#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
main
"""

from multiAsset import multiAsset

def main():
    a = multiAsset()

    a.query('a')
    a.query('b')

    a.init('a')
    data = {
            "id": "n1",
            "prop1": 1,
            "prop2": 2
            }
    a.appand('a', data)
    a.query('a')

if __name__ == '__main__':
    main()
