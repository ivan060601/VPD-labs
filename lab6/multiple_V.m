L = 0.0047;
J = 0.0023;
Km = 0.29;
Ke = Km;
R = 4.7;
Ks = 150;
Kr = 100;
Um = 3.5;
Rad = 0.0275;
Brad = 0.17;

x_m1 = out.V3.data;
y_m1 = out.V3.time;
plot(y_m1,x_m1,'b-');
hold on;

x_m2 = out.V4.data;
y_m2 = out.V4.time;
plot(y_m2,x_m2,'y--');
hold on;

x_m3 = out.V3.data;
y_m3 = out.V3.time;
plot(y_m3,x_m3,'r-');
hold on;

x_m4 = out.V4.data;
y_m4 = out.V4.time;
plot(y_m4,x_m4,'g--');
hold on;

grid on;
xlabel('Time');
ylabel('V');

legend(['Model V(t) to [-1;-1] Lab6'],['Model V(t) to [-1;1] Lab6'],['Model V(t) to [-1;-1] Lab5'],['Model V(t) to [-1;1] Lab5'],'Location','northeast');
