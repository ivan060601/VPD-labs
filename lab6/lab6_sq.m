x_m = outCopy1.X_c.data;
y_m = outCopy1.Y_c.data;
plot(0.5*y_m,0.5*x_m,'b--');
hold on;

x_m1 = outCopy.X.data;
y_m1 = outCopy.Y.data;
plot(0.5*x_m1,0.5*y_m1,'b--');
hold on;


legend(['Model'],['Experiment'],'Location','southeast');