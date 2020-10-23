path = r"‪D:\Учеба\\1 курс\ВПД\lab4\data_2\PI_aw\data aw 10.txt"
f = open(path,'r')
new_line = ''
time_array = []
time = 0.0
i,j=0,0
angle = 0
max_angle = 0
state_angle = 0
state_time = 10.0

for line in f:
	i=i+1
	new_line = f.readline()	
	try:
		time, angle = float(new_line.split()[0]), int(new_line.split()[1])
	except:
		pass
	if angle>max_angle: max_angle = angle
	state_angle = angle

f.close()
f = open(path,'r')
time_array = f.readlines()

for j in range(i,0,-1):
	try:
		if (int(time_array[j].split()[1]) > 0.95*state_angle) and (int(time_array[j].split()[1]) < 1.05*state_angle):
			state_time = float(time_array[j].split()[0])
		else:
			break
	except: 
		pass

f.close()

e = abs(180 - state_angle)
overreg = (max_angle - state_angle)*100/state_angle
print('Уст. угол = ' + str(state_angle))
print('Уст. ошибка = ' + str(e))
print('Пререгулирование = ' + str(overreg)[0:6] + ' %')
print('Время переходного процесса = ' + str(state_time)[0:6])