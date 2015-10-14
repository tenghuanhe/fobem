a = load('fob.dat');
x = 2.54*a(:,2);
y = 2.54*a(:,3);

x = x - x(1);
y = y - y(1);
plot(x,y)
% 
% hold on;
% t = -25:0.01:0;
% yt = -10 * sin(2*pi/25*t);
% plot(t,yt);