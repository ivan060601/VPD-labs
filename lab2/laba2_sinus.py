#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math
mA = LargeMotor('outA')

for i in range(1,4):
	s='data_sinus_'+str(i)+'.txt'
	fh = open(s, 'w')
	fh.write('0' + ' 0' + '\n')
	mA.position = current_time = start_time = 0
	start_time = time.time()

	while True:
			current_time = time.time() - start_time
			if current_time > 3:
				break
			else:
				s = 100*math.sin(current_time*math.pi*i)
				mA.run_direct(duty_cycle_sp = int(s))
				fh.write(str(current_time) + ' ' + str(mA.position) + '\n')
		
	mA.stop(stop_action = 'brake')
	time.sleep(1)
	fh.close()