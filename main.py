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

    # 发行资产
    multiAsset.init('a')
    raw_input("初始化 ... 按任意键继续")
    data = {
            "id": 1,
            "value": 1000,
            }
    multiAsset.issue('a', data)
    raw_input("正在发行资产 ... 按任意键继续")
    multiAsset.show('a')
    raw_input("按资产 id 查看余额 ... 按任意键继续")
    print multiAsset.query_value_by_id('a', 1)
    print multiAsset.query_value_by_id('a', 2)

    # 转移资产
    raw_input("转移资产 ... 按任意键继续")
    multiAsset.transmit('a', 'b', 1, 100)
    raw_input("查看账户余额 ... 按任意键继续")
    multiAsset.show('a')
    multiAsset.show('b')

if __name__ == '__main__':
    main()
