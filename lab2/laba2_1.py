#!/usr/bin/python3
from ev3dev.ev3 import *

mA = LargeMotor('outA')

i=-100

while i<=(-10):
	mA.run_direct(duty_cycle_sp = i)
	time.sleep(3)
	mA.run_direct(duty_cycle_sp = 0)
	time.sleep(2)
	i=i+10