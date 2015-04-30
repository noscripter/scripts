#!/usr/bin/env python3
# Download maps from sernix insurgency server
# By Lu Wang

# Usage:
# Download all maps
# insurgency_sernix_downloader.py
# Download all maps whose name has prefix of Test 
# insurgency_sernix_downloader.py Test

import requests
import re
import os
import bz2
import sys

MAPS_URL = 'http://207.173.67.34/insurgency/maps/'
MAP_PATTERN = re.compile('<a href="([^"]+)">')
DOWNLOAD_PATH = os.path.expanduser('~/Library/Application Support/Steam/SteamApps/common/insurgency2/insurgency/maps')

def work():
    for map_name in MAP_PATTERN.findall(requests.get(MAPS_URL).content.decode()):
        if not map_name.endswith('.bz2'):
            continue
        if len(sys.argv) == 2 and not map_name.startswith(sys.argv[1]):
            continue
        local_file_name = os.path.join(DOWNLOAD_PATH, map_name[:-4])
        if os.path.exists(local_file_name):
            print(map_name + ': skipped')
            continue
        print(map_name + ': downloading...', end='', flush = True)
        with open(local_file_name, 'wb') as outf:
            outf.write(bz2.decompress(requests.get(MAPS_URL+map_name).content))
        print('done')


if __name__ == '__main__':
    work()
