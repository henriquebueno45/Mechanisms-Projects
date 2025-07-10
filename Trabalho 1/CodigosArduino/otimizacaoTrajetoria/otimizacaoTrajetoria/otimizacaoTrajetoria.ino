// Constantes físicas
const float g = 9.81; // gravidade em m/s²

// Parâmetros de entrada
float v0 = 5.0;      // Velocidade inicial (m/s)
float h = 0.30;      // Altura inicial (m)
float R = 4.0;       // Distância horizontal (m)

// Função que calcula o alcance horizontal para um dado ângulo
float alcance(float theta, float v0, float h) {
  float sinT = sin(theta);
  float cosT = cos(theta);
  float discriminante = (v0 * sinT) * (v0 * sinT) + 2 * g * h;
  if (discriminante < 0) return -1; // não atinge o solo
  float t = (v0 * sinT + sqrt(discriminante)) / g;
  return v0 * cosT * t;
}

void setup() {
  Serial.begin(9600);
  
  float theta = 0;
  float bestTheta = -1;
  float errorMin = 1e6;
  float degStep = 0.1; // Precisão da busca

  for (float deg = 1.0; deg < 89.0; deg += degStep) {
    theta = radians(deg);
    float x = alcance(theta, v0, h);
    float erro = abs(x - R);

    if (erro < errorMin) {
      errorMin = erro;
      bestTheta = deg;
    }
  }

  if (bestTheta > 0) {
    Serial.print("Melhor angulo (graus): ");
    Serial.println(bestTheta, 2);
    Serial.print("Erro (m): ");
    Serial.println(errorMin, 4);
  } else {
    Serial.println("Nao foi possivel encontrar um angulo valido.");
  }
}

void loop() {
  // Nada no loop
}
