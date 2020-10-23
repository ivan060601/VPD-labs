x_m1 = out.X1.data;
y_m1 = out.Y1.data;
plot(y_m1,x_m1,'b');
hold on;

x_m1 = out6.X1.data;
y_m1 = out6.Y1.data;
plot(y_m1,x_m1,'b--');
hold on;

x_m2 = out.X2.data;
y_m2 = out.Y2.data;
plot(y_m2,x_m2,'y');
hold on;

x_m3 = out.X3.data;
y_m3 = out.Y3.data;
plot(y_m3,x_m3,'r');
hold on;

x_m4 = out.X4.data;
y_m4 = out.Y4.data;
plot(y_m4,x_m4,'g');

x_m2 = out6.X2.data;
y_m2 = out6.Y2.data;
plot(y_m2,x_m2,'y--');
hold on;

x_m3 = out6.X3.data;
y_m3 = out6.Y3.data;
plot(y_m3,x_m3,'r--');
hold on;

x_m4 = out6.X4.data;
y_m4 = out6.Y4.data;
plot(y_m4,x_m4,'g--');
hold on;
grid on;
xlabel('X');
ylabel('Y');

legend(['Model Lab5 to [1;1]'],['Model Lab6 to [1;1]'],'Location','southeast');



