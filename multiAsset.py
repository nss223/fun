#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
Multi asset implement
"""

import json
import logging

from fabricAdapter import fabricAdapter

class multiAsset:
    __fabric = fabricAdapter()

    @staticmethod
    def show(userid):
        """get values of `userid` and print in a nice form"""
        print json.dumps(multiAsset.__fabric.get(userid), indent = 4)

    @staticmethod
    def query(userid):
        """get values of `userid`"""
        return multiAsset.__fabric.get(userid)

    @staticmethod
    def query_by_id(userid, aid):
        """get values of `userid`, and filtered by `aid`"""
        return filter(lambda x: x['id'] == aid, multiAsset.query(userid))
    
    @staticmethod
    def query_value_by_id(userid, aid):
        """get value of `aid` of `userid`"""
        v = multiAsset.query_by_id(userid, aid)
        if v == []:
            return 0
        else:
            return v[0]['value']

    @staticmethod
    def update_value_by_id(userid, aid, value, debug = True):
        """set value to `value` of `aid` of `userid`"""
        try:
            vs = multiAsset.__fabric.get(userid)
            pos = (i for i,v in enumerate(vs) if v['id'] == aid).next()
            vs[pos]['value'] = value
            multiAsset.__fabric.set(userid, vs)
        except StopIteration:
            if debug:
                logging.warn("User " + userid + " does not has asset of " + str(aid))
            data = {
                    "id": aid,
                    "value": value,
                    }
            multiAsset.issue(userid, data)
    
    @staticmethod
    def init(userid):
        """reset values of `userid`"""
        multiAsset.__fabric.set(userid, []) 

    @staticmethod
    def issue(userid, new_data):
        """add `new_data` to `userid`"""
        vs = multiAsset.__fabric.get(userid)
        if filter(lambda x: x['id'] == new_data['id'], vs) == []:
            vs = vs + [new_data]
        else:
            logging.error("User " + userid + " already has asset " + str(new_data['id']))
        multiAsset.__fabric.set(userid, vs)

    @staticmethod
    def remove_value_by_id(userid, aid, value):
        """remove `value` of `aid` of `userid`
        fail if `value` > current value
        """
        try:
            vs = multiAsset.__fabric.get(userid)
            pos = (i for i,v in enumerate(vs) if v['id'] == aid).next()
            cvalue = vs[pos]['value']
            if cvalue < value:
                logging.error("User " + userid + " does not have enough asset " + str(aid))
                return

            if cvalue == value:
                del vs[pos]
            else:
                vs[pos]['value'] = cvalue - value
            
            multiAsset.__fabric.set(userid, vs)
        except StopIteration:
            logging.error("User " + userid + " does not has asset of " + str(aid))

    @staticmethod
    def transmit(src, dst, aid, value):
        """remove `value` from `src` of `aid`, add them to `dst`"""
        if multiAsset.__fabric.get(dst) == {}:
            multiAsset.init(dst)
        multiAsset.remove_value_by_id(src, aid, value)
        multiAsset.update_value_by_id(dst, aid, value)

