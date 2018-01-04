#! /bin/bash
#
# docker_wrapper.sh
# Copyright (C) 2018  <@fabric>
#
# Distributed under terms of the MIT license.
#

cmd=$1
[[ x$cmd = x"invoke" ]] || [[ x$cmd = x"query" ]] || { echo "wrong cmd"; exit 1; }
shift
docker exec cli peer chaincode $cmd -n mycc -c '{"Args":'"$@"'}' -C myc #2>/dev/null

