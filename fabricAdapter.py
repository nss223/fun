#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018  <@fabric>
#
# Distributed under terms of the MIT license.

"""
fabric adapter
"""

import ConfigParser
import json
import logging
import os
import subprocess

class fabricAdapter:

    def __init__(self, debug = False):
        cf = ConfigParser.ConfigParser()
        cf.read('config.ini')

        self.__docker_bin       = '/usr/bin/docker'
        self.__docker_cmd       = 'exec'
        self.__container        = 'cli'
        self.__peer_bin         = 'peer'
        self.__peer_cmd         = 'chaincode'

        self.__chaincode_name   = f.get('fabric', 'chaincode_name')
        self.__channel_id       = f.get('fabric', 'channel_id')
        if not debug:
            self.__err = open(os.devnull, 'w')
        else:
            self.__err = None

    def __cmd_builder(self, cmd, func, ctor):
        """ build cmd string, i.e.
        docker exec cli peer chaincode $cmd -n mycc -c '{"Args":'"$@"'}' -C myc
        """
        return [
                self.__docker_bin,
                self.__docker_cmd,
                self.__container,
                self.__peer_bin,
                self.__peer_cmd,
                cmd,
                '-n',
                self.__chaincode_name,
                '-c',
                '{"Args":["' + func + '", "' + str(ctor) + ']}',
                '-C',
                self.__channel_id
                ]

    def get(self, k, debug = False):
        """ Get value of `k` and return its data, in python's dic form. """
        try:
            p = subprocess.Popen(self.__cmd_builder('query', '', str(k) + '"'), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            out, err = p.communicate()
            r = out.strip().split('Query Result: ')[1]
            ret = json.loads(r)
        except IndexError:
            if err.find('(status: 500, message: Asset not found: ') > -1:
                if debug:
                    logging.warn('Asset not found: ' + k)
            else:
                logging.error(err)
            ret = []
	return ret

    def set(self, k, v):
        """ Set `k` of value `v`, whose form is dic. """
        p = subprocess.Popen(self.__cmd_builder('invoke', 'set', str(k) + '", ' + json.dumps(json.dumps(v))), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = p.communicate()

        if err.find('Error: ') > -1:
            logging.error(err)

    def test(self):
	data = {
                'userid': '7a42f74',
                'asset': [
                    {
                        'assetID': 1111,
                        'Issuer': 'A_bank',
                        'assetvalue': 33,
                        'characteristic': '2018-01-01'
                        },
                    {
                        'assetID': 2222,
                        'Issuer': 'B_bank',
                        'assetvalue': 44,
                        'characteristic': '2017-04-01'
                        }
                    ]
                }
        self.set('a', data)
        print json.dumps(self.get('a'), indent = 4)
