"""
Given  a string you need to remove all adjuscent characters that are same.
Until there are no moore adjacent characters that are same.

ex1. 

    a,b,b,d => a,d
    a,b,c,c,b,d,e => a,b,b,d,e => a,d,e
    a,d,e,b,b,e,c,a,a,c,d,e => a,e

    We can solve using this by stack
"""

import os
import sys
sys.path.append(os.getcwd())

from advance.live.day_86.q1 import Stack

