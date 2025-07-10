#include <Servo.h>

Servo meuServo_1;
Servo meuServo_2;
const int pinoServo_2 = 6;
const int pinoServo_1 = 7;
String entradaSerial = "";
float distancia = 0;
bool modoAtivo = false;

void setup() {
  Serial.begin(9600);
  meuServo_1.attach(pinoServo_1);
  meuServo_1.write(140);
  delay(150);
  meuServo_2.attach(pinoServo_2);
  meuServo_2.write(140);
  delay(150);
  Serial.println("Digite 0 para iniciar o sistema.");
}

void loop() {
  if (Serial.available()) {
    char caractere = Serial.read();

    if (caractere == '\n') {
      float valorRecebido = entradaSerial.toFloat();

      if (!modoAtivo && valorRecebido == 0) {
        meuServo_1.write(0);
        meuServo_2.write(0);
        Serial.println("Sistema iniciado. Digite a distância desejada (max. 4m):");
        modoAtivo = true;
      } else if(modoAtivo && valorRecebido == 10){
        meuServo_1.write(145);
        meuServo_2.write(145);
        Serial.println("Sistema desativado. digite 0 para iniciar: ");
        modoAtivo = false;
      }else if (modoAtivo) {
        distancia = valorRecebido;

        float angulo_distancia = 33.323 * pow(distancia, 3) - 229.2 * pow(distancia, 2) + 564.95 * distancia - 440.2;
        if (angulo_distancia < 0) {
          angulo_distancia = 0;
        } else if (angulo_distancia > 150) {
          angulo_distancia = 150;
        }
        meuServo_2.write(constrain(angulo_distancia, 0, 180));
        Serial.print("Movendo para ");
        Serial.print(angulo_distancia);
        Serial.println(" graus (ajustado para faixa segura).");
      } else {
        Serial.println("Digite 0 para iniciar.");
      }

      entradaSerial = "";
    } else {
      entradaSerial += caractere; // Constrói a string recebida
    }
  }
}