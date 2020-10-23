x_m1 = out.X1.data;
y_m1 = out.Y1.data;
plot(0.5*y_m1,0.5*x_m1,'b--');
hold on;

x_m2 = outLab6.X.data;
y_m2 = outLab6.Y.data;
plot(0.5*y_m2,0.5*x_m2,'b');
hold on;

grid on;
xlabel('X');
ylabel('Y');

legend(['Model Lab5'],['Model Lab6'],'Location','southeast');