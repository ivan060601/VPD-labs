#!/usr/bin/python3
from ev3dev.ev3 import *
from array import *
import time
import math

mLeft = LargeMotor('outC')
mRight = LargeMotor('outD')

coord_x = [1,1,-1,-1,1]
coord_y = [1,-1,-1,1,1]

err_d = 0.005
Rad = 0.0275
Brad = 0.17
x = 0
y = 0
angle = 0
start_time = 0
cur_time = 0
prev_left_position = 0
prev_right_position = 0
to_rad = 3.14/180
to_grad = 180/3.14
Ks = 250
Kr = 70
i = 0
control = 0
baseSpeed = 0
k = 20
length = 0


fh = open('data.txt', 'w')
fh.write('0' + ' 0' + '\n')

def run_motors(x1, y1):
  global x, y, angle, prev_left_position, prev_right_position

  start_time = time()

  while math.sqrt(math.pow((x1 - x),2) + math.pow((y1 - y),2)) > END_DIST:
    cur_time = time()
    lpsi = (prev_left_position - mLeft)*to_rad
    rpsi = (prev_right_position - mRight)*to_rad
    theta = (lpsi - rpsi)*Rad/Brad
  
    x = x + cos(angle) * (lpsi + rpsi) / 2 * Rad
    y = y + sin(angle) * (lpsi + rpsi) / 2 * Rad
    angle = angle + theta

    Us = Ks * math.sqrt(math.pow((x1 - x),2) + math.pow((y1 - y),2))

    u = math.atan2(y1 - y, x1 - x) - angle
    if (math.fabs(u) > pi):
    	u -= copysign(2*pi, u)
    #Ur = Kr * u

    length =  math.sqrt(math.pow((x1 - x),2) + math.pow((y1 - y),2))
    baseSpeed = 100*math.tanh(length)*cos(u)
    if (math.fabs(baseSpeed) > 80): baseSpeed = math.copysign(baseSpeed,80)
    control = k*u+sin(u)*baseSpeed/length
    if (math.fabs(control) > 20): control = math.copysign(control,20)

    prev_left_position = mLeft.position
    prev_right_position = mRight.position

    #if math.fabs(Ur)>20: Ur = copysign(Ur,20)
    #if math.fabs(Us)>80: Ur = copysign(Us,80)

    #mRight.run_direct(duty_cycle_sp = Us+Ur)
    #mLeft.run_direct(duty_cycle_sp = Us-Ur)
    
    mRight.run_direct(duty_cycle_sp = baseSpeed+control)
    mLeft.run_direct(duty_cycle_sp = baseSpeed-control)


#for i in range(0, len(coord_x)-1):
#	run_motors(coord_x[i], coord_y[i])

run_motors(1,1)
mRight.stop(stop_action = 'brake')
mLeft.stop(stop_action = 'brake')
time.sleep(1)
fh.close()