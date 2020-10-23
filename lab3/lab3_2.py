#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math

mC = LargeMotor('A')
mD = LargeMotor('B')
us = UltrasonicSensor('in1')
#us.mode("US-DIST-CM")
dist = us.value()

Kp = -0.5

fh = open('data.txt', 'w')
fh.write('0' + ' 0' + '\n')

start_time = time.time()
mC.position = 0
mD.position = 0

while True :
	current_time = time.time() - start_time
	err=300-us.value()
	if current_time < 10:
		up=Kp*err
		if math.fabs(up) > 100:
			mC.run_direct(duty_cycle_sp = math.copysign(100,up))
			mD.run_direct(duty_cycle_sp = math.copysign(100,up))
			fh.write(str(current_time) + ' ' + str(us.value()) + '\n')
		else:
			mC.run_direct(duty_cycle_sp = int(up))
			mD.run_direct(duty_cycle_sp = int(up))
			fh.write(str(current_time) + ' ' + str(us.value()) + '\n')
	else:
		break

mC.stop(stop_action = 'brake')
mD.stop(stop_action = 'brake')
time.sleep(1)
fh.close()
