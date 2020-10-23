results = read('D:\Programs\scilab-6.0.2\data\lab1\data100.txt', -1, 2)
angle = results(:,2)*%pi/180
time = results(:,1)
plot2d(time,angle,2)
aim = [time,angle]
aim = aim'
deff ("e=func(k,z)","e=z(2)-k(1)*(z(1)-k(2)*(1-exp(-z(1)/k(2))))")
att = [15;0.06]
[koeffs,errs] = datafit(func,aim,att)
Wnls = koeffs(1)
Tm = koeffs(2)
model = Wnls*(time-Tm*(1-exp(-time/Tm)))
plot2d(time,model,3)
plot2d (w.time, w.values,5)
legend('Experiment 1','$\theta(t)=\omega_{nls}t-\omega_{nls}T_m+\omega_{nls}T_m\,exp\bigl(-\frac{t}{T_m}\bigr)$','Model',2)
