#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math

mC = LargeMotor('C')

Kp = 3
Ki = 0.08
Kd = 0.03

fh = open('data.txt', 'w')
fh.write('0' + ' 0' + '\n')

start_time = time.time()
mC.position = 0
old_position = mC.position
old_time = time.time() - start_time
sum_err = 0

while True :
	current_time = time.time() - start_time
	err=180-mC.position
	if current_time < 10:
		up = Kp*err
		ud = Kd*(mC.position - old_position)/(current_time-old_time)
		sum_err = sum_err + err
		ui = Ki*sum_err
		old_position = mC.position
		old_time = current_time
		u=up+ui+ud
		if abs(u) > 100:
			mC.run_direct(duty_cycle_sp = math.copysign(100,u))
			fh.write(str(current_time) + ' ' + str(mC.position) + '\n')
		else:
			mC.run_direct(duty_cycle_sp = int(u))
			fh.write(str(current_time) + ' ' + str(mC.position) + '\n')
	else: 
		break

mC.stop(stop_action = 'brake')
time.sleep(1)
fh.close()
