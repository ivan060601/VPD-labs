/*results = read('C:\Users\Ivan\Desktop\data\data_sinus_1.txt', -1, 2)
angle = results(:,2)*%pi/180
time = results(:,1)
plot2d(time,angle,2)
results = read('C:\Users\Ivan\Desktop\data\data_sinus_2.txt', -1, 2)
angle = results(:,2)*%pi/180
time = results(:,1)
plot2d(time,angle,2)*/
results = read('C:\Users\Ivan\Desktop\data\data_sinus_3.txt', -1, 2)
angle = results(:,2)*%pi/180
time = results(:,1)
plot2d(time,angle,2)
t1 = 0.2:0.01:3;
a1 = 1.25*sin(9.42*t1-2.05)+1.35

t2 = 0.05:.01:0.2;
a2 = 1.25*sin(9.42*t2-2)+1.3
plot2d(t1,a1,5)
plot2d(t2,a2,5)
legend('Experiment [3pi]','Model',2)

