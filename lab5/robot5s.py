from ev3dev.ev3 import *
#from motor import LargeMotor
from time import *
from math import *

# List of points (x, y)
PATH = [
  [0.5, 0.5],
  [-0.5, 0.5],
  [-0.5, -0.5],
  [0.5, -0.5],
  [0.5, 0.5]
]
END_DIST = 0.05
Ks = 250
Kr = 70

r = 0.0275
B = 0.17
DT = 0.05

x, y, angle = 0, 0, 0
start_time, cur_time = 0, 0

prev_left_position = 0
prev_right_position = 0

left_motor = LargeMotor('outC')
right_motor = LargeMotor('outD')

left_motor.position = 0
right_motor.position = 0

stream = open('data.txt', 'w')

def limit(num, lim=100):
  return max(min(num, lim), -lim)

def calc_p(point):
  return sqrt((point[0] - x) ** 2 + (point[1] - y) ** 2)

def calc_a(point):
  global x, y
  #if point[0] == 0:
  #  return pi/2
  #psi_tan = (point[1] - y) / (point[0] - x)
  #res = atan(psi_tan) - angle
  res = atan2(point[1] - y, point[0] - x) - angle
  if (abs(res) > pi):
    res -= copysign(2*pi, res)
  return res

def calc_dpsi():
  global prev_left_position, prev_right_position
  dleft = left_motor.position - prev_left_position
  dright = right_motor.position - prev_right_position
  return dleft / 180 * pi, dright / 180 * pi

def calc_dtheta(lpsi, rpsi):
  return (rpsi - lpsi) * r / B

def run_to(point):
  global x, y, angle, prev_left_position, prev_right_position

  start_time = time()
  print('Start run to point (%.1f, %.1f).' % (point[0], point[1]))
  print(calc_p(point), calc_p(point) >= END_DIST)
  while calc_p(point) >= END_DIST:
    cur_time = time()
    lpsi, rpsi = calc_dpsi()
    dtheta = calc_dtheta(lpsi, rpsi)
  
    x += cos(angle) * (lpsi + rpsi) / 2 * r 
    y += sin(angle) * (lpsi + rpsi) / 2 * r
    angle += dtheta

    Us = Ks * calc_p(point)
    Ur = Kr * calc_a(point)

    prev_left_position = left_motor.position
    prev_right_position = right_motor.position

    left_motor.run_direct(duty_cycle_sp = limit(limit(Us, 80) - limit(Ur, 20)))
    right_motor.run_direct(duty_cycle_sp = limit(limit(Us, 80) + limit(Ur, 20)))

    print(calc_a(point) * 180 / pi, angle * 180 / pi, end = ' | ')

    print('%.2f, %.2f, %.2f' % (lpsi*180 / pi, rpsi*180/pi, dtheta))
    stream.write('%f %f %f %f\n' % (cur_time - start_time, x, y, angle))
    print('%4.2f: x = %.3f | y = %.3f | angle = %.3f || %.2f %.2f' % (cur_time - start_time, x, y, angle * 180 / pi, Us, Ur))
    if time() - cur_time < DT:
      sleep(DT)
  print('End run.')

try:
  for point in PATH:
    run_to(point)

  left_motor.run_direct(duty_cycle_sp = 0)
  right_motor.run_direct(duty_cycle_sp = 0)
except:
  left_motor.stop(stop_action='brake')
  right_motor.stop(stop_action='brake')
  stream.close()
finally:
  left_motor.stop(stop_action='brake')
  right_motor.stop(stop_action='brake')
  stream.close()