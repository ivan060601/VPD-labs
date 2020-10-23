L = 0.0047;
J = 0.0023;
Km = 0.29;
Ke = Km;
R = 4.7;
Ks = 250;
Kr = 70;
Um = 3.5;
Rad = 0.0275;
Brad = 0.17;
    
x_m1 = out.X1.data;
y_m1 = out.Y1.data;
plot(y_m1,x_m1,'r');
hold on;
plot(kvadrat.VarName3,kvadrat.VarName2,'b','LineWidth',1);
grid on;

legend(['Model'],['Experiment'],'Location','southeast');

xlabel('X');
ylabel('Y');