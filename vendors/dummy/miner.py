#!/usr/bin/python

import time
import sys

if __name__ == "__main__":

    try:
        while True:
            time.sleep(1)
            print("[2018-01-23 10:57:17] accepted: 61/62 (98.39%), 572.27 MH/s yay!!!")
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)