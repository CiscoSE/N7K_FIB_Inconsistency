# Nexus7000 FIB inconsistency

*Detects and recovers inconsistent FIB routes on Nexus 7000 switch*


## Motivation

Due to a software defect on N7k, there can be some routes incorrectly programmed in the hardware FIB. The workaround is to clear the inconsistent route in the RIB (clear ip route <route>).

This script is an on-box script. It collects the current list of inconsistent routes and then clears them to recover. 


**Cisco Products & Services:**

Cisco Nexus 7000 switch running 8.x NX-OS release. It can be applicable to other Nexus platforms and NX-OS releases as well.


## Usage

1. Copy the script to the Nexus switch bootflash:scripts directory
2. Execute the script using the "source" command, or using the "run-script <path>" command


## Installation

Copy the script to the Nexus switch bootflash:scripts directory.


## Authors & Maintainers

- Charles Youssef <cyoussef@cisco.com>

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
# N7K_FIB_Inconsistency
