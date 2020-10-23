#!/usr/bin/python3
from ev3dev.ev3 import *
import time
import math

mLeft = LargeMotor('A')
mRight = LargeMotor('D')

int err_t = 0.005
float k_p_angle = 3
float k_p_velocity = 4
int max_p = 50

int i_radius = 0.027	
int o_radius = 0.192

float x,y,last_x,last_ygoal_dist, goal_orientation, avg_rot,
      current_orientation, dist_rolled, l,last_l,
      dist_traveled, orientation_diff, dist_left = 0;
float goal_x, goal_y = 1, 1

def pi_mod(angle):
	if abs(angle) > math.PI:
		return (angle-math.copysign(angle,2*math.PI))
	else:
		return angle

def run_motors(orientation_diff, goal_dist):
	float u1, u2
	int pwrLeft, pwrRight
	u1 = k_p_angle*orientation_diff
	u2 = k_p_velocity*goal_dist*math.cos(orientation_diff)

	if abs(u1) > max_p:
		u1 = math.copysign(u1, max_p)
	if abs(u2) > max_p:
		u2 = math.copysign(u2, max_p)

	pwrLeft = u1+u2
	pwrRight = u1-u2

	if pwrRight > 100:
		pwrRight = math.copysign(pwrRight, 100)
	if pwrLeft > 100:
		pwrLeft = math.copysign(pwrLeft, 100)

	mLeft.run_direct(duty_cycle_sp = pwrLeft)	
	mRight.run_direct(duty_cycle_sp = pwrRight)	

goal_dist = dist_left = math.sqrt(math.pow(goal_x,2)+math.pow(goal_y,2))
goal_orientation = pi_mod(atan2(goal_y,goal_x))

while dist_left>err_t:
	avg_rot = (mLeft.position+mRight.position)*(math.PI/180)/2
	current_orientation = (math.PI/180)*((mLeft.position-mRight.position)*i_radius/o_radius)
	dist_rolled = avg_rot*i_radius
	l = dist_rolled - last_l

	x = l*math.cos(current_orientation) + x
	y = l*math.sin(current_orientation) + y

	dist_traveled = math.sqrt(math.pow(x,2)+math.pow(y,2))
	last_l = dist_rolled

	orientation_diff = pi_mod(goal_orientation - current_orientation)
	dist_left = goal_dist - dist_traveled
	run_motors(orientation_diff,goal_dist)
	