#!/usr/bin/env python3

import sys
import datetime as dt

if len(sys.argv) < 2:
    print('Usage: python3 tw_cancel_snipe.py arrival')
    sys.exit(-1)

# arrival
arrival = dt.datetime.strptime(sys.argv[1], '%H:%M:%S').time()

# cancel time
for m in range(9, -1, -1):
	for s in [30, 0]:
		if m == 0 and s == 0:
			continue
		cancel_delta = dt.timedelta(minutes=m, seconds=s)
		departure = (dt.datetime.combine(dt.date(1,1,10), arrival) - 2*cancel_delta).time()
		cancel_time = (dt.datetime.combine(dt.date(1,1,10), arrival) - cancel_delta).time()
		print('{:02d}:{:02d} before --> send at {}, cancel at {}'.format(m, s, departure, cancel_time))

