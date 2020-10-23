plot(0.5*to_11.Y,0.5*to_11.X, 'b');
hold on;
plot(to_n11.Y,to_n11.X, 'y');
hold on;
plot(to_1n1.Y,to_1n1.X, 'r');
hold on;
plot(-to_n11.Y,to_n11.X, 'g');
hold on;

grid on;
xlabel('X');
ylabel('Y');