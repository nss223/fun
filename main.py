#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
多资产管理平台演示
"""

from multiAsset import multiAsset as ma

def main():
    ma.show('a')

def test():

    # 发行资产
    ma.init('a')

    data = {
            "id": 2,
            "value": 1000,
            }
    ma.issue('a', data)


    ma.show('a')

    print ma.query_value_by_id('a', 1)
    print ma.query_value_by_id('a', 2)

    # 转移资产

    ma.transmit('a', 'b', 1, 100)

    ma.show('a')
    ma.show('b')

if __name__ == '__main__':
    main()
