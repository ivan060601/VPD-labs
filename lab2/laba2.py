#!/usr/bin/python3
from ev3dev.ev3 import *
import time

mA = LargeMotor('outA')
mA.position = current_time = start_time = 0

start_time = time.time()

i=10

while i<=100:
	try:
		while True:
			current_time = time.time() - start_time
			if current_time > 3:
				break
			else:
				mA.run_direct(duty_cycle_sp = i)
	finally:
		mA.stop(stop_action = 'brake')
		fh.close()

	mA.run_direct(duty_cycle_sp = 0)
	time.sleep(1)
	i=i+10;
break