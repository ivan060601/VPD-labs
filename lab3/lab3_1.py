#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math

mA = LargeMotor('A')

Kp = 3

fh = open('data.txt', 'w')
fh.write('0' + ' 0' + '\n')

start_time = time.time()
mA.position = 0


while True :
	current_time = time.time() - start_time
	err=180-mA.position
if current_time < 10:
	up=Kp*err
	if math.fabs(up) > 100:
		mA.run_direct(duty_cycle_sp = math.copysign(100,up))
		fh.write(str(current_time) + ' ' + str(mA.position) + '\n')
	else:
		mA.run_direct(duty_cycle_sp = int(up))
		fh.write(str(current_time) + ' ' + str(mA.position) + '\n')
else:
	break

mA.stop(stop_action = 'brake')
time.sleep(1)
fh.close()