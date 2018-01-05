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

from multiAsset import multiAsset

def main():
    multiAsset.show('a')

def test():

    # 发行资产
    multiAsset.init('a')

    data = {
            "id": 2,
            "value": 1000,
            }
    multiAsset.issue('a', data)


    multiAsset.show('a')

    print multiAsset.query_value_by_id('a', 1)
    print multiAsset.query_value_by_id('a', 2)

    # 转移资产

    multiAsset.transmit('a', 'b', 1, 100)

    multiAsset.show('a')
    multiAsset.show('b')

if __name__ == '__main__':
    main()
