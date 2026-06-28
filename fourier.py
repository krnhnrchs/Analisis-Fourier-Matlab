% ==========================================================
% ANALISIS DE SEÑALES Y TRANSFORMADA DE FOURIER
% Autor: Karen Heinrichs
% ==========================================================

clc;
clear;
close all;

%% =========================================================
% DEFINICION DE LA SEÑAL EN EL DOMINIO DEL TIEMPO
% ==========================================================

Fs = 1000;          % Frecuencia de muestreo (Hz)
T = 1;              % Duración de la señal (s)
t = 0:1/Fs:T-1/Fs;  % Vector de tiempo

%% =========================================================
% 1. SEÑAL SENOIDAL
% ==========================================================

f = 50; % Frecuencia de la señal (Hz)

senal_senoidal = sin(2*pi*f*t);

% Gráfica en el dominio del tiempo
figure;
plot(t, senal_senoidal,'LineWidth',1.5);
title('Señal Senoidal - Dominio del Tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;

%% =========================================================
% CALCULO DE LA TRANSFORMADA DE FOURIER
% ==========================================================

FFT_senoidal = fft(senal_senoidal);

N = length(FFT_senoidal);
frecuencia = (0:N-1)*(Fs/N);

%% =========================================================
% VISUALIZACION DE LA MAGNITUD
% ==========================================================

figure;
plot(frecuencia(1:N/2),abs(FFT_senoidal(1:N/2)),'LineWidth',1.5);
title('Espectro de Magnitud - Señal Senoidal');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');
grid on;

%% =========================================================
% VISUALIZACION DE LA FASE
% ==========================================================

figure;
plot(frecuencia(1:N/2),angle(FFT_senoidal(1:N/2)),'LineWidth',1.5);
title('Espectro de Fase - Señal Senoidal');
xlabel('Frecuencia (Hz)');
ylabel('Fase (rad)');
grid on;

%% =========================================================
% 2. PULSO RECTANGULAR
% ==========================================================

pulso = double((t >= 0.3) & (t <= 0.7));

figure;
plot(t,pulso,'LineWidth',1.5);
title('Pulso Rectangular');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;

FFT_pulso = fft(pulso);

figure;
plot(frecuencia(1:N/2),abs(FFT_pulso(1:N/2)),'LineWidth',1.5);
title('Espectro de Magnitud del Pulso Rectangular');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');
grid on;

%% =========================================================
% 3. FUNCION ESCALON
% ==========================================================

escalon = double(t >= 0.5);

figure;
plot(t,escalon,'LineWidth',1.5);
title('Funcion Escalon');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;

FFT_escalon = fft(escalon);

figure;
plot(frecuencia(1:N/2),abs(FFT_escalon(1:N/2)),'LineWidth',1.5);
title('Espectro de Magnitud de la Funcion Escalon');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');
grid on;

%% =========================================================
% PROPIEDAD DE LINEALIDAD
% ==========================================================

senal2 = sin(2*pi*100*t);

senal_suma = senal_senoidal + senal2;

FFT_suma = fft(senal_suma);

figure;
plot(frecuencia(1:N/2),abs(FFT_suma(1:N/2)),'LineWidth',1.5);
title('Propiedad de Linealidad');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');
grid on;

%% =========================================================
% PROPIEDAD DE DESPLAZAMIENTO TEMPORAL
% ==========================================================

senal_desplazada = sin(2*pi*f*(t-0.1));

FFT_desplazada = fft(senal_desplazada);

figure;
plot(frecuencia(1:N/2),angle(FFT_desplazada(1:N/2)),'LineWidth',1.5);
title('Cambio de Fase por Desplazamiento Temporal');
xlabel('Frecuencia (Hz)');
ylabel('Fase (rad)');
grid on;

%% =========================================================
% PROPIEDAD DE ESCALAMIENTO
% ==========================================================

senal_escalada = sin(2*pi*(2*f)*t);

FFT_escalada = fft(senal_escalada);

figure;
plot(frecuencia(1:N/2),abs(FFT_escalada(1:N/2)),'LineWidth',1.5);
title('Escalamiento en Frecuencia');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');
grid on;

%% =========================================================
% CONCLUSIONES DEL ANALISIS
% ==========================================================

disp('ANALISIS FINAL');
disp('1. La señal senoidal presenta un pico dominante en 50 Hz.');
disp('2. El pulso rectangular contiene multiples componentes frecuenciales.');
disp('3. La funcion escalon concentra energia en bajas frecuencias.');
disp('4. La linealidad permite sumar señales y observar ambas frecuencias.');
disp('5. El desplazamiento temporal modifica la fase.');
disp('6. El escalamiento cambia la posicion de las componentes espectrales.');