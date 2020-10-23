#!/usr/bin/python3
import math
from math import *
from ev3dev.ev3 import *
from time import *

L = LargeMotor('outA')
R = LargeMotor('outC')



r_coles = 55/2/1000
U = 4
B = 0.15

k_front = 125
k_angle = 150
Kw=10
Vmax=100

alf = 0
Xnow = Ynow = 0
points = [[0.5,0.5], [-0.5,0.5], [-0.5,-0.5],[0.5,-0.5],[0.5, 0.5]]

X_delta = Y_delta = 0
R_pred = L_pred = 0
L_delta = R_delta = 0
l_delta = 0
distance = 0

s1 = 'Results gps sq.txt'
f=open(s1,'w')
f.write('0'+'0'+'\n')

def AngleFiltre(u1):
    if abs(u1)>pi:
        return float(u1-copysign(1, u1)*2*pi)
    else:
        float(u1)

def VektorP(X,Y):
    return sqrt(pow(X,2)+pow(Y,2))

def GetR():
    return R.position

def GetL():
    return L.position

L.reset()
R.reset()

const_time = time()
start_time = time()
TimeNow = time()
for i in range(len(points)):
    X = points[i][0]
    Y = points[i][1]

    while True:
        try:
            current_time = time() - const_time
            delta_time = time() - start_time
            L_now = GetL()
            R_now = GetR()
            L_delta = L_now-L_pred
            R_delta = R_now-R_pred

            distance = VektorP(X-Xnow,Y-Ynow)
            alf=radians((GetL()-GetR())*r_coles/B)
            l_delta=radians((L_delta+R_delta)/2*r_coles)

            Xnow = Xnow + cos(alf)*l_delta
            Ynow = Ynow + sin(alf)*l_delta

            angle = atan2(Y-Ynow, X-Xnow)-alf

            if abs(angle)>pi:
               angle = angle-copysign(1, angle)*2*pi

            print(str(distance))

            BaseSpeed = Vmax * math.tanh(5*distance) * math.cos(angle)
            AngleSpeed = Kw * angle + Vmax * (math.tanh(distance) / distance) * math.sin(angle) * math.cos(angle)

            u_l = BaseSpeed + AngleSpeed
            u_r = BaseSpeed - AngleSpeed

            if (distance<0.03):
                break

            if (abs(u_l) > 100):
                u_l = 100 * copysign(1, u_l)
            if (abs(u_r) > 100):
                u_r = 100 * copysign(1, u_r)

            R.run_direct(duty_cycle_sp=u_r)
            L.run_direct(duty_cycle_sp=u_l)

            L_pred = L_now
            R_pred = R_now
            start_time = time()
            f.write(str(Xnow) + ' ' + str(Ynow) + '\n')

        except (KeyboardInterrupt, SystemExit):
            R.run_direct(duty_cycle_sp=0)
            L.run_direct(duty_cycle_sp=0)
            break

R.run_direct(duty_cycle_sp=0)
L.run_direct(duty_cycle_sp=0)