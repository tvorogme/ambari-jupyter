#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import hashlib
from resource_management import *
import random

def cast_bytes(s):
    if not isinstance(s, bytes):
        return s.encode('ascii', "replace")
    return s

def hashText(text):
    h = hashlib.new('sha1')
    salt_len = 12
    salt = ('%0' + str(salt_len) + 'x') % random.getrandbits(4 * salt_len)
    h.update(text.encode() + salt.encode())

    return ':'.join(('sha1', salt, h.hexdigest()))

config = Script.get_config()

config_dir = "/opt/jupyter/"
jupyter_port = config['configurations']['jupyter-hl-env']['jupyter_port']
jupyter_host = config['configurations']['jupyter-hl-env']['jupyter_host']

jupyter_password = config['configurations']['jupyter-hl-env']['jupyter_password']
jupyter_root_dir = config['configurations']['jupyter-hl-env']['jupyter_root_dir']

anaconda_user = 'root'
anaconda_group = 'root'

client_port = config['configurations']['port-jupyter-forward-env']['port_forward']
