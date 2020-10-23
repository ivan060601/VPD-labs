#!/usr/bin/python3
from ev3dev.ev3 import *
import time

mA = LargeMotor('outB')
mA.position = current_time = start_time = 0

fh = open('data.txt', 'w')
fh.write('0' + '0' + '\n')

start_time = time.time()

try:
	while True:
		current_time = time.time() - start_time
		if current_time > 1:
			break
		else:
			mA.run_direct(duty_cycle_sp = 100)
			fh.write(str(current_time) + '' + str(mA.position) + '\n')
finally:
	mA.stop(stop_action = 'brake')
	fh.close()