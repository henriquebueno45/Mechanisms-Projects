import os
import numpy as np
import matplotlib.pyplot as plt

def cicloide(h, beta):
    
    beta_rad = np.deg2rad(beta)
    
    theta_deg = np.linspace(0, beta*2, 1000)
    
    s = np.zeros_like(theta_deg)
    v = np.zeros_like(theta_deg)
    a = np.zeros_like(theta_deg)
    j = np.zeros_like(theta_deg)
    
    # Subida: 0 <= theta < beta
    idx_subida = theta_deg <= beta
    theta_subida = np.deg2rad(theta_deg[idx_subida])
    
    s[idx_subida] = h * (theta_subida / beta_rad - (1/(2*np.pi)) * np.sin(2*np.pi * theta_subida / beta_rad))
    v[idx_subida] = (h / beta_rad) * (1 - np.cos(2*np.pi * theta_subida / beta_rad))
    a[idx_subida] = (2 * np.pi * h) / (beta_rad ** 2) * np.sin(2*np.pi * theta_subida / beta_rad)
    j[idx_subida] = (4 * np.pi ** 2 * h) / (beta_rad ** 3) * np.cos(2*np.pi * theta_subida / beta_rad)
    
    # Descida: beta <= theta < 2*beta
    idx_descida = (theta_deg > beta) & (theta_deg <= 2*beta)
    theta_descida = np.deg2rad(theta_deg[idx_descida]) - beta_rad
    
    s[idx_descida] = h * (1 - (theta_descida / beta_rad - (1/(2*np.pi)) * np.sin(2*np.pi * theta_descida / beta_rad)))
    v[idx_descida] = - (h / beta_rad) * (1 - np.cos(2*np.pi * theta_descida / beta_rad))
    a[idx_descida] = - (2 * np.pi * h) / (beta_rad ** 2) * np.sin(2*np.pi * theta_descida / beta_rad)
    j[idx_descida] = - (4 * np.pi ** 2 * h) / (beta_rad ** 3) * np.cos(2*np.pi * theta_descida / beta_rad)
    
    # Repouso no restante
    s[theta_deg > 2*beta] = 0
    v[theta_deg > 2*beta] = 0
    a[theta_deg > 2*beta] = 0
    j[theta_deg > 2*beta] = 0
    
    geraGraficos(theta_deg, s, v, a, j)

def harmonico(h, beta):

    theta_deg = np.linspace(0, beta*2, 1000)
    beta_rad = np.deg2rad(beta)

    s = np.zeros_like(theta_deg)
    v = np.zeros_like(theta_deg)
    a = np.zeros_like(theta_deg)
    j = np.zeros_like(theta_deg)
    
    # Subida: 0 <= theta < beta
    idx_subida = theta_deg <= beta
    theta_subida = np.deg2rad(theta_deg[idx_subida])
    
    s[idx_subida] = (h / 2) * (1 - np.cos(np.pi * theta_subida / beta_rad))
    v[idx_subida] = (h * np.pi) / (2 * beta_rad) * np.sin(np.pi * theta_subida / beta_rad)
    a[idx_subida] = (h * np.pi ** 2) / (2 * beta_rad ** 2) * np.cos(np.pi * theta_subida / beta_rad)
    j[idx_subida] = - (h * np.pi ** 3) / (2 * beta_rad ** 3) * np.sin(np.pi * theta_subida / beta_rad)
    
    idx_descida = (theta_deg > beta) & (theta_deg <= 2*beta)
    theta_descida = np.deg2rad(theta_deg[idx_descida]) - beta_rad
    
    s[idx_descida] = h - (h / 2) * (1 - np.cos(np.pi * theta_descida / beta_rad))
    v[idx_descida] = - (h * np.pi) / (2 * beta_rad) * np.sin(np.pi * theta_descida / beta_rad)
    a[idx_descida] = - (h * np.pi ** 2) / (2 * beta_rad ** 2) * np.cos(np.pi * theta_descida / beta_rad)
    j[idx_descida] = (h * np.pi ** 3) / (2 * beta_rad ** 3) * np.sin(np.pi * theta_descida / beta_rad)
    
    # Repouso no restante: s = 0
    s[theta_deg > 2*beta] = 0
    v[theta_deg > 2*beta] = 0
    a[theta_deg > 2*beta] = 0
    j[theta_deg > 2*beta] = 0
    
    geraGraficos(theta_deg,s,v,a,j)

def polinomio_8(h, beta):

    # Ângulo total 0° a 360°
    theta_deg = np.linspace(0, beta*2, 1000)
    theta = theta_deg  # Graus, pois y usa graus
    
    s = np.zeros_like(theta)
    v = np.zeros_like(theta)
    a = np.zeros_like(theta)
    j = np.zeros_like(theta)
    
    # Subida: 0 <= theta < beta
    idx_subida = theta <= beta
    y_subida = theta[idx_subida] / beta
    
    s[idx_subida] = h * (35 * y_subida**4 - 84 * y_subida**5 + 70 * y_subida**6 - 20 * y_subida**7)
    v[idx_subida] = h * (140 * y_subida**3 - 420 * y_subida**4 + 420 * y_subida**5 - 140 * y_subida**6) / beta
    a[idx_subida] = h * (420 * y_subida**2 - 1680 * y_subida**3 + 2100 * y_subida**4 - 840 * y_subida**5) / beta**2
    j[idx_subida] = h * (840 * y_subida - 5040 * y_subida**2 + 8400 * y_subida**3 - 4200 * y_subida**4) / beta**3
    
    # Descida: beta <= theta < 2*beta
    idx_descida = (theta > beta) & (theta <= 2*beta)
    y_descida = (theta[idx_descida] - beta) / beta  # normaliza de 0 a 1
    
    s[idx_descida] = h * (1 - (35 * y_descida**4 - 84 * y_descida**5 + 70 * y_descida**6 - 20 * y_descida**7))
    v[idx_descida] = - h * (140 * y_descida**3 - 420 * y_descida**4 + 420 * y_descida**5 - 140 * y_descida**6) / beta
    a[idx_descida] = - h * (420 * y_descida**2 - 1680 * y_descida**3 + 2100 * y_descida**4 - 840 * y_descida**5) / beta**2
    j[idx_descida] = - h * (840 * y_descida - 5040 * y_descida**2 + 8400 * y_descida**3 - 4200 * y_descida**4) / beta**3
    
    # Repouso: 2*beta até 360°
    s[theta > 2*beta] = 0
    v[theta > 2*beta] = 0
    a[theta > 2*beta] = 0
    j[theta > 2*beta] = 0
    
    geraGraficos(theta_deg,s,v,a,j)


def geraGraficos(theta_deg, s, v, a, j):
    # Plot 2x2
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    
    axs[0, 0].plot(theta_deg, s, 'b', linewidth=1.5)
    axs[0, 0].set_title('Deslocamento (mm)')
    axs[0, 0].set_xlabel('Ângulo da came (graus)')
    axs[0, 0].grid(True)
    
    axs[0, 1].plot(theta_deg, v, 'r', linewidth=1.5)
    axs[0, 1].set_title('Velocidade (mm/grau)')
    axs[0, 1].set_xlabel('Ângulo da came (graus)')
    axs[0, 1].grid(True)
    
    axs[1, 0].plot(theta_deg, a, 'g', linewidth=1.5)
    axs[1, 0].set_title('Aceleração (mm/grau²)')
    axs[1, 0].set_xlabel('Ângulo da came (graus)')
    axs[1, 0].grid(True)
    
    axs[1, 1].plot(theta_deg, j, 'm', linewidth=1.5)
    axs[1, 1].set_title('Jerk (mm/grau³)')
    axs[1, 1].set_xlabel('Ângulo da came (graus)')
    axs[1, 1].grid(True)
    
    plt.tight_layout()
    plt.show()


option  = 0

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("++++++++++++++++++ Opções de Elevação de seguidor ++++++++++++++++")
    print("[1] - Cicloide")
    print("[2] - Harmônico")
    print("[3] - Polinômio de oitavo grau")
    print("[4] - Meia-cicloide + Meia-harmônico")
    print("[5] - Para Meia-harmônico + Meia-cicloide")
    print("[6] - Para Meia-cicloide + velocidade constante + Meia-cicloide")
    print("[7] - Para Meia-cicloide + velocidade constante + Meia-harmônico")
    print("[8] - Para Meia-harmônico  + velocidade constante + Meia-harmônico")
    print("[9] - Para Meia-harmônico + velocidade constante + Meia-cicloide")
    try:
        option = int(input("Digite a opção desejada: "))
        h = float(input("Informe a elevação total do seguidor (mm): "))
        beta = float(input("Informe o ângulo de subida/descida (graus): "))
    except:
        option = 0
    print(option)
    if(option == 1):
        cicloide(h, beta)
        break
    elif(option == 2):
        harmonico(h, beta)
        break
    elif(option == 3):
        polinomio_8(h, beta)
        break
