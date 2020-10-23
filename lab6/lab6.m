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

plot(0.5*to_11.Y,0.5*to_11.X, 'b');
hold on;
plot(to_n11.Y,to_n11.X, 'y');
hold on;
plot(to_1n1.Y,to_1n1.X, 'r');
hold on;
plot(-to_n11.Y,to_n11.X, 'g');
hold on;

x_m1 = out.X1.data;
y_m1 = out.Y1.data;
plot(y_m1,x_m1,'b--');
hold on;

x_m2 = out.X2.data;
y_m2 = out.Y2.data;
plot(y_m2,x_m2,'y--');
hold on;

x_m3 = out.X3.data;
y_m3 = out.Y3.data;
plot(y_m3,x_m3,'r--');
hold on;

x_m4 = out.X4.data;
y_m4 = out.Y4.data;
plot(y_m4,x_m4,'g--');
hold on;
grid on;
xlabel('X');
ylabel('Y');

legend(['Experiment to [0.5;0.5]'],['Experiment to [0.5;-0.5]'],['Experiment to [-0.5;0.5]'],['Experiment to [-0.5;-0.5]'],['Model to [0.5;0.5]'],['Model to [0.5;-0.5]'],['Model to [-0.5;0.5]'],['Model to [-0.5;-0.5]'],'Location','east');
