#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
Multi asset
"""

import json
import logging

from fabricAdapter import fabricAdapter

class multiAsset:
    def __init__(self):
        self.fabric = fabricAdapter()

    def query(self, userid):
        res = self.fabric.get(userid)
        print json.dumps(res, indent = 4)
    
    def init(self, userid):
        self.fabric.set(userid, []) 

    def appand(self, userid, new_data):
        asset = self.fabric.get(userid)
        if filter(lambda x: x['id'] == new_data['id'], asset) == []:
            asset = asset + [new_data]
        else:
            logging.warn(userid + " already has asset " + new_data['id'])
        self.fabric.set(userid, asset)
