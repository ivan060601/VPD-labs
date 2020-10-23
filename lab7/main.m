k_m = 0.29;
k_e = k_m;
R = 4.7;
m_t = 0.33;
m_k = 0.018;
r = 0.028;
l = 0.111/2;
J = 0.0023;
J_k = 0.000007056;
J_t = 0.00073;
g = 9.8;

Um = 8;
t = 0.5;
t_zvezda = 6.3;
w_0 = t_zvezda/t;

x_1 = m_t*l*r*(m_t*l*r-2*J)-(m_t*l^2+J_t)*(m_t*r^2+2*m_k*r^2+2*J_k+2*J);

a11 = 0; 
a12 = 0; 
a13 = 1;
a21 = (m_t^2*g*r*l^2)/x_1; 
a22 = (2*k_m*k_e*(m_t*l*r + m_t*l^2 + J_t))/(R*x_1); 
a23 = 0;
a31 = (-m_t*g*l*(m_t*r^2 + 2*m_k*r^2 + 2*J_k + 2*J))/x_1; 
a32 = (-2*k_m*k_e*(m_t*l*r + m_t*r^2 + 2*m_k*r^2 + 2*J_k))/(R*x_1); 
a33 = 0;

b1 = 0;
b2 = (-2*k_m*(m_t*l*r + m_t*l^2 + J_t))/(R*x_1);
b3 = (2*k_m*(m_t*l*r + m_t*r^2 + 2*m_k*r^2 + 2*J_k))/(R*x_1);

A = [a11 a12 a13; a21 a22 a23; a31 a32 a33];
B = [b1; b2; b3];

C = A*B;
D = A^2*B;

Y = [B(1,1) C(1,1) D(1,1); B(2,1) C(2,1) D(2,1); B(3,1) C(3,1) D(3,1)];

E = [0 b2 b3; b3 0 a32*b2-a22*b3; a32*b2-a22*b3 a21*b3-a31*b2 0];
W = [3*w_0 + a22; 3*w_0^2 + a31; w_0^3 - a22*a31 + a21*a32];
K = E\W;

k_1 = K(1,1);
k_2 = K(2,1);
k_3 = K(3,1);

disp(Y);
THETA = out.d_psi.data * 180/pi;
THETA_TIME = out.d_psi.time;
plot(THETA_TIME, THETA, 'r');
grid on;
xlabel('{\it t}, c','Fontsize',20);
ylabel('$\dot{\psi}, ^\circ$','interpreter','latex','Fontsize',20)
hold on;