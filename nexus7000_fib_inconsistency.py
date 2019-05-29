#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nexus7000 FIB inconsistency Console Script.

Due to a software defect on N7k, there can be some routes incorrectly programmed in the hardware FIB. 
The workaround is to clear the inconsistent route in the RIB (clear ip route ).

This script is an on-box script. It collects the current list of inconsistent routes and then clears them to recover.

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

