#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nexus7000 FIB inconsistency Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Charles Youssef"
__email__ = "cyoussef@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from time import sleep

print("Checking for inconsistent routes...")

cli("test forwarding inconsistency")
sleep(10)

print("Clearing inconsistent routes in the RIB...")
inconsistent_routes = cli("show forwarding inconsistency | grep prefix | cut -f 4 -d '(' | cut -f 1 -d ')' | sort | uniq").splitlines()
for route in inconsistent_routes:
	cli("clear ip route {}".format(route))
	print("Route {} is cleared".format(route))
	sleep(3)

print("All inconsistent routes have been cleared.")

