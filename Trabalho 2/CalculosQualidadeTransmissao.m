clear;
clc;
close all;

%% Caça - 2PFS

a = 51.95;
b = 29.46;
c = 29.69;
d = 4.47;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = 92.36:142.8;
u = acosd(A + B * cosd(theta));

pivot = 90:150;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

% figure();
% plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
% legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
% grid on;
% title("Mecanismo principal - 2PFS");
% xlabel("Ângulo de entrada [graus]");
% ylabel("Ângulo de saída [graus]");

%% Caça - 3PFS

a = 70.42;
b = 30.63;
c = 54.87;
d = 10.45;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = 147.26:211.32;
u = acosd(A + B * cosd(theta));

pivot = 140:220;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

% figure();
% plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
% legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
% grid on;
% title("Mecanismo principal - 3PFS");
% xlabel("Ângulo de entrada [graus]");
% ylabel("Ângulo de saída [graus]");


%% Caixa - pá - 2PFS

a = 200.96;
b = 55.81;
c = 187.39;
d = 54.5;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = 17.5:118.02;
u = acosd(A + B * cosd(theta));

pivot = 0:140;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

% figure();
% plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
% legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
% grid on;
% title("Mecanismo principal - 2PFS");
% xlabel("Ângulo de entrada [graus]");
% ylabel("Ângulo de saída [graus]");

%% Caixa - tampa - 2PFS

a = 85.49;
b = 119.2;
c = 88.03;
d = 17.7;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = 62.89:163.1;
u = acosd(A + B * cosd(theta));

pivot = 0:180;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

% figure();
% plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
% legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
% grid on;
% title("Mecanismo principal - 2PFS");
% xlabel("Ângulo de entrada [graus]");
% ylabel("Ângulo de saída [graus]");

%% Caixa - Pá - 3PFS

a = 268;
b = 83.96;
c = 227.18;
d = 96.54;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = 12.27:83.39;
u = acosd(A + B * cosd(theta));

pivot = 0:100;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

figure();
plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
grid on;
title("Mecanismo principal - 3PFS");
xlabel("Ângulo de entrada [graus]");
ylabel("Ângulo de saída [graus]");

%% Caixa - Tampa - 3PFS

a = 143.61;
b = 69.68;
c = 95.06;
d = 54.64;

A = (b^2 + c^2 - a^2 - d^2)/(2*b*c);
B = a*d/b/c;

theta = -15.7:91.45;
u = acosd(A + B * cosd(theta));

pivot = -20:100;

limMax = ones(1, numel(pivot)) * 140;
limMin = ones(1, numel(pivot)) * 40;

figure();
plot(theta,u, pivot, limMin, pivot, limMax, 'LineWidth', 2);
legend("Curva de qualidade de transmissão", "Limite inferior", "Limite superior");
grid on;
title("Mecanismo principal - 3PFS");
xlabel("Ângulo de entrada [graus]");
ylabel("Ângulo de saída [graus]");