%% Cicloidal

[theta_deg, s_val, v_val, a_val, j_val] = cicloide_symbolic();


function [theta_deg, s_val, v_val, a_val, j_val] = cicloide_symbolic()
    clc; clear;
    fprintf('=== MOVIMENTO CICLOIDAL ===\n');
    
    % Entradas
    h = input('Informe a elevação total do seguidor (mm): ');
    beta = input('Informe o ângulo de levantamento (graus): ');
    
    % Definir variáveis simbólicas
    syms theta beta_sym h_sym
    
    % Converter ângulo em radianos internamente
    theta_rad = deg2rad(theta);
    beta_rad = deg2rad(beta_sym);
    
    % Equação simbólica do deslocamento
    s_sym = h_sym * (theta_rad / beta_rad - (1/(2*pi)) * sin(2*pi * theta_rad / beta_rad));
    
    % Derivadas simbólicas
    v_sym = diff(s_sym, theta); % Velocidade
    a_sym = diff(v_sym, theta); % Aceleração
    j_sym = diff(a_sym, theta); % Jerk
    
    % Mostrar fórmulas:
    disp('Equação de deslocamento:');
    pretty(s_sym)
    disp('Equação de velocidade:');
    pretty(v_sym)
    disp('Equação de aceleração:');
    pretty(a_sym)
    disp('Equação de jerk:');
    pretty(j_sym)
    
    % Vetor de ângulos
    theta_deg = linspace(0, beta, 500);
    
    % Substituir símbolos por valores numéricos
    s_val = zeros(size(theta_deg));
    v_val = zeros(size(theta_deg));
    a_val = zeros(size(theta_deg));
    j_val = zeros(size(theta_deg));
    
    for i = 1:length(theta_deg)
        s_val(i) = double(subs(s_sym, {theta, beta_sym, h_sym}, {theta_deg(i), beta, h}));
        v_val(i) = double(subs(v_sym, {theta, beta_sym, h_sym}, {theta_deg(i), beta, h}));
        a_val(i) = double(subs(a_sym, {theta, beta_sym, h_sym}, {theta_deg(i), beta, h}));
        j_val(i) = double(subs(j_sym, {theta, beta_sym, h_sym}, {theta_deg(i), beta, h}));
    end
    
    % Plots
    figure;
    subplot(4,1,1);
    plot(theta_deg, s_val, 'b', 'LineWidth', 1.5);
    title('Deslocamento (mm)');
    xlabel('Ângulo da came (graus)');
    grid on;
    
    subplot(4,1,2);
    plot(theta_deg, v_val, 'r', 'LineWidth', 1.5);
    title('Velocidade (mm/grau)');
    xlabel('Ângulo da came (graus)');
    grid on;
    
    subplot(4,1,3);
    plot(theta_deg, a_val, 'g', 'LineWidth', 1.5);
    title('Aceleração (mm/grau²)');
    xlabel('Ângulo da came (graus)');
    grid on;
    
    subplot(4,1,4);
    plot(theta_deg, j_val, 'm', 'LineWidth', 1.5);
    title('Jerk (mm/grau³)');
    xlabel('Ângulo da came (graus)');
    grid on;

end
