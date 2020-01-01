#!/usr/bin/env python3

import sys
import datetime as dt

if len(sys.argv) < 3:
    print('Usage: python3 tw_departure.py arrival duration')
    sys.exit(-1)

# arrival
arrival = dt.datetime.strptime(sys.argv[1], '%H:%M:%S').time()

# duration
duration = sys.argv[2].split(':')
h = int(duration[0])
m = int(duration[1])
s = int(duration[2])
duration = dt.timedelta(hours=h, minutes=m, seconds=s)

# departure
departure = (dt.datetime.combine(dt.date(1,1,10), arrival) - duration).time()
print(departure)
