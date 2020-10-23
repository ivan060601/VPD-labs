Um = 3.5;
Kp = 3;
Ki = 0.05;
Kd = 0.03;
Kb = 5;
L = 0.0047;
J = 0.0023;
Km = 0.29;
Ke = Km;
R = 4.7;
angle_1 = 3.14;
state_angle = 180;

time_m = out.simout.time;
angle_m = out.simout.data;
plot(time_m,angle_m,'r');
hold on;

plot(data.VarName1,data.VarName2,'b');
hold on;

x = [0,0,10,10];
y = [state_angle*0.95,state_angle*1.05,state_angle*1.05,state_angle*0.95];
h = fill(x,y,'y','edgecolor','none');
set(h,'facealpha',.2)
hold on;

yline(state_angle*0.95,'--k');
hold on;
yline(state_angle*1.05,'--k');
grid on;

legend(['Model K_{\itp} = ',num2str(Kp),'; K_{\iti} = ',num2str(Ki),'; K_{\itd} = ', num2str(Kd),'; anti-windup = ',num2str(Kb)],['Experiment K_{\itp} = ',num2str(Kp),'; K_{\iti} = ',num2str(Ki),'; K_{\itd} = ', num2str(Kd),'; anti-windup = ',num2str(Kb)],'Confidence interval','Location','southeast');
xlabel('Time [sec]');
ylabel('Angle [grad]');