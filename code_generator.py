#!/usr/bin/env python
import sys
if not sys.version_info >= (3, 0):
    sys.stdout.write("Sorry requires python 3.x, its not combatible with 2.x\n")
    sys.exit(1)



import the_real_thing
if __name__ == "__main__":
    the_real_thing.main()
