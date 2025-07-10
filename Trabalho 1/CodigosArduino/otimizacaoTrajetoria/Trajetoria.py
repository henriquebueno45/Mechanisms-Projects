import numpy as np
distancia = 2.5
angulo_distancia = 33.323*np.pow(distancia,3) - 229.2*np.pow(distancia,2) + 564.95*distancia - 440.2

print(f"Distância: {distancia} - angulo: {int(angulo_distancia)}")