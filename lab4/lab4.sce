Um = 3.5;
Kp = 2;
Ki = 0.05;
Kd = 0.03;
Kb = 0;
L = 0.0047;
J = 0.0023;
Km = 0.29;
Ke = Km;
R = 4.64;
angle_1 = 3.14;
state_angle = 180;

results = read('C:\Users\Ivan\Desktop\lab4\data_2\PID\data 2 005 003.txt', -1, 2)
time = results(:,1)
angle = results(:,2)/180*3.14
plot2d(time,angle,1)

plot2d(t.time,t.values,5)
