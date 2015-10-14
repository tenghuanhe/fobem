a = load('fob-d2.dat');
x = 2.54*a(:,2);
y = 2.54*a(:,3);
z = 2.54*a(:,4);
x = x - x(1);
y = y - y(1);
plot3(x,y,z)
% 
% hold on;
% t = -25:0.01:0;
% yt = -10 * sin(2*pi/25*t);
% plot(t,yt);
