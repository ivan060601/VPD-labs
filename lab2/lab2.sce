results = read('C:\Users\Ivan\Desktop\data\data_30.txt', -1, 2)
angle = results(:,2)*%pi/180
time = results(:,1)
plot2d(time,angle,2)
plot2d (w.time, w.values,5)
legend('Experiment (30)','Model',2)
