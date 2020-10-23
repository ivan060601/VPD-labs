#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math

mB = LargeMotor('B')
mC = LargeMotor('C')
us1 = UltrasonicSensor('in2')
us2 = UltrasonicSensor('in3')
dist1 = us1.value()/10
dist2 = us2.value()/10

Kp = 0.6
Ki = 0
Kd = 0
aw = 10
h = 22
desired_dist = 20

fh = open('data.txt', 'w')
fh.write('0' + ' 0' + '\n')

start_time = time.time()
old_position = 0.5*h*(dist1+dist2)*math.sqrt(1/(math.pow(h,2)+math.pow((dist1-dist2),2)))
old_time = time.time() - start_time
sum_err = 0

while True :
	current_time = time.time() - start_time
	dist1 = us1.value()/10
	dist2 = us2.value()/10
	d = 0.5*h*(dist1+dist2)*math.sqrt(1/(math.pow(h,2)+math.pow((dist1-dist2),2)))
	err=desired_dist-d

	if current_time < 20:
		up = Kp*err
		ud = Kd*(d - old_position)/(current_time-old_time)
		if math.fabs(err) > aw:
			sum_err = sum_err + 0
		else:
			sum_err = sum_err + err
		ui = Ki*sum_err
		old_position = d
		old_time = current_time

		u=up+ui+ud
		if abs(u) > 50:
			mB.run_direct(duty_cycle_sp = 50-math.copysign(50,u))
			mC.run_direct(duty_cycle_sp = 50+math.copysign(50,u))
			fh.write(str(current_time) + ' ' + str(d) + '\n')
		else:
			mB.run_direct(duty_cycle_sp = 50-u)
			mC.run_direct(duty_cycle_sp = 50+u)
			fh.write(str(current_time) + ' ' + str(d) + '\n')
	else: 
		break

mB.stop(stop_action = 'brake')
mC.stop(stop_action = 'brake')
time.sleep(1)
fh.close()
