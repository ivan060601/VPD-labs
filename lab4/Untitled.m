%time_m = out.simout.time;
%angle_m = out.simout.data;
%plot(time_m,angle_m,'r');
%hold on;

plot(data.VarName3,data.VarName2,'b','LineWidth',2);
hold on;
plot(data2.VarName3,data2.VarName2,'r','LineWidth',2);
hold on;
plot(data3.VarName3,data3.VarName2,'g','LineWidth',2);
hold on;
plot(data4.VarName3,data4.VarName2,'k','LineWidth',2);
hold on;
grid on;