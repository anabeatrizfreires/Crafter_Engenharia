#include <Ultrasonic.h>

//----------------------------- Variáveis de funcionamento dos sensores -------------------------------
//sensores de distancia
bool presence_01 = LOW;              // flag de detecção sensor (sensor ultrasonico)
bool presence_02 = LOW;              // flag de detecção sensor (sensor ultrasonico)
bool presence_03 = LOW;              // flag de detecção sensor (sensor ultrasonico)
bool presence_04 = LOW;              // flag de detecção sensor (sensor ultrasonico)
bool presence_05 = LOW;              // flag de detecção sensor (sensor ultrasonico)
bool presence_06 = LOW;              // flag de detecção sensor (sensor ultrasonico)

unsigned long tempo_torneira_01_aberta = 0; // Variavel para armazenar o tempo da torneira 01 aberta
unsigned long tempo_torneira_02_aberta = 0; // Variavel para armazenar o tempo da torneira 02 aberta
unsigned long tempo_torneira_03_aberta = 0; // Variavel para armazenar o tempo da torneira 03 aberta
unsigned long tempo_torneira_04_aberta = 0; // Variavel para armazenar o tempo da torneira 04 aberta
unsigned long tempo_torneira_05_aberta = 0; // Variavel para armazenar o tempo da torneira 05 aberta
unsigned long tempo_torneira_06_aberta = 0; // Variavel para armazenar o tempo da torneira 06 aberta

byte limite_detect = 15;             // limite de detecção em cm (sensor ultrasonico)

//---------------------------------------- CONFIGURAÇÃO DE HARDWARE ---------------------------------------
//sensor de distancia
#define ECHO_PIN_01       2
#define TRIGGER_PIN_01    3

#define ECHO_PIN_02       4
#define TRIGGER_PIN_02    5
  
#define ECHO_PIN_03       6 
#define TRIGGER_PIN_03    7

#define ECHO_PIN_04       8
#define TRIGGER_PIN_04    9

#define ECHO_PIN_05       10
#define TRIGGER_PIN_05    11

#define ECHO_PIN_06       12
#define TRIGGER_PIN_06    13

//relé acionamento
#define RELAY_PIN_01 A0
bool estado_rele_01 = HIGH;         //estado LOW aciona o relé

#define RELAY_PIN_02 A1
bool estado_rele_02 = HIGH;         //estado LOW aciona o relé

#define RELAY_PIN_03 A2
bool estado_rele_03 = HIGH;         //estado LOW aciona o relé

#define RELAY_PIN_04 A3
bool estado_rele_04 = HIGH;         //estado LOW aciona o relé

#define RELAY_PIN_05 A4
bool estado_rele_05 = HIGH;         //estado LOW aciona o relé

#define RELAY_PIN_06 A5
bool estado_rele_06 = HIGH;         //estado LOW aciona o relé

#define TEMPO_ACIONAMENTO 3000     //tempo de acionamento em ms

//---------------------------------------- CONSTRUTORES -------------------------------------------------------
Ultrasonic sensor_dist_01(TRIGGER_PIN_01, ECHO_PIN_01);
Ultrasonic sensor_dist_02(TRIGGER_PIN_02, ECHO_PIN_02);
Ultrasonic sensor_dist_03(TRIGGER_PIN_03, ECHO_PIN_03);
Ultrasonic sensor_dist_04(TRIGGER_PIN_04, ECHO_PIN_04);
Ultrasonic sensor_dist_05(TRIGGER_PIN_05, ECHO_PIN_05);
Ultrasonic sensor_dist_06(TRIGGER_PIN_06, ECHO_PIN_06);

//---------------------------------------- SETUP DO PROGRAMA ----------------------------------------------------
void setup()
{
  Serial.begin(9600);
  pinMode(RELAY_PIN_01, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_01, estado_rele_01);   //Desliga o rele
  
  pinMode(RELAY_PIN_02, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_02, estado_rele_02);   //Desliga o rele
  
  pinMode(RELAY_PIN_03, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_03, estado_rele_03);   //Desliga o rele
  
  pinMode(RELAY_PIN_04, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_04, estado_rele_04);   //Desliga o rele
  
  pinMode(RELAY_PIN_05, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_05, estado_rele_05);   //Desliga o rele

  pinMode(RELAY_PIN_06, OUTPUT);                //Define o pino para o rele como saida
  digitalWrite(RELAY_PIN_06, estado_rele_06);   //Desliga o rele

}

void loop()
{
  //torneira_01();
  torneira_02();
  torneira_03();
  torneira_04();
  torneira_05();
  //torneira_06();

  
  //debug();
  //teste_saidas();
}

//---------------------------------------- FUNÇÕES DO PROGRAMA ----------------------------------------------------

void teste_saidas()
{
  digitalWrite(RELAY_PIN_01, LOW); delay(500);
  digitalWrite(RELAY_PIN_02, LOW); delay(500);
  digitalWrite(RELAY_PIN_03, LOW); delay(500);
  digitalWrite(RELAY_PIN_04, LOW); delay(500);
  digitalWrite(RELAY_PIN_05, LOW); delay(500);
  digitalWrite(RELAY_PIN_06, LOW); delay(500);

  digitalWrite(RELAY_PIN_01, HIGH); digitalWrite(RELAY_PIN_02, HIGH);
  digitalWrite(RELAY_PIN_03, HIGH); digitalWrite(RELAY_PIN_04, HIGH);
  digitalWrite(RELAY_PIN_05, HIGH); digitalWrite(RELAY_PIN_06, HIGH);
  delay(500);
}


void torneira_01()
{
  // checando sensor de distancia 01
  float dist_cm_01; long microsec_01 = sensor_dist_01.timing();
  dist_cm_01 = sensor_dist_01.convert(microsec_01, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_01 < limite_detect && presence_01 == LOW)
  {
      digitalWrite(RELAY_PIN_01, !estado_rele_01);   //Liga o rele
      tempo_torneira_01_aberta = millis();
      presence_01 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_01 && (millis() - tempo_torneira_01_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_01, estado_rele_01);   //Desliga o rele
      tempo_torneira_01_aberta = millis();
      presence_01 = LOW;
  }
}

void torneira_02()
{
  // checando sensor de distancia 01
  float dist_cm_02; long microsec_02 = sensor_dist_02.timing();
  dist_cm_02 = sensor_dist_02.convert(microsec_02, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_02 < limite_detect && presence_02 == LOW)
  {
      digitalWrite(RELAY_PIN_02, !estado_rele_02);   //Liga o rele
      tempo_torneira_02_aberta = millis();
      presence_02 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_02 && (millis() - tempo_torneira_02_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_02, estado_rele_02);   //Desliga o rele
      tempo_torneira_02_aberta = millis();
      presence_02 = LOW;
  }
}

void torneira_03()
{
  // checando sensor de distancia 03
  float dist_cm_03; long microsec_03 = sensor_dist_03.timing();
  dist_cm_03 = sensor_dist_03.convert(microsec_03, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_03 < limite_detect && presence_03 == LOW)
  {
      digitalWrite(RELAY_PIN_03, !estado_rele_03);   //Liga o rele
      tempo_torneira_03_aberta = millis();
      presence_03 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_03 && (millis() - tempo_torneira_03_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_03, estado_rele_03);   //Desliga o rele
      tempo_torneira_03_aberta = millis();
      presence_03 = LOW;
  }
}

void torneira_04()
{
  // checando sensor de distancia 4
  float dist_cm_04; long microsec_04 = sensor_dist_04.timing();
  dist_cm_04 = sensor_dist_04.convert(microsec_04, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_04 < limite_detect && presence_04 == LOW)
  {
      digitalWrite(RELAY_PIN_04, !estado_rele_04);   //Liga o rele
      tempo_torneira_04_aberta = millis();
      presence_04 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_04 && (millis() - tempo_torneira_04_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_04, estado_rele_04);   //Desliga o rele
      tempo_torneira_04_aberta = millis();
      presence_04 = LOW;
  }
}

void torneira_05()
{
  // checando sensor de distancia 05
  float dist_cm_05; long microsec_05 = sensor_dist_05.timing();
  dist_cm_05 = sensor_dist_05.convert(microsec_05, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_05 < limite_detect && presence_05 == LOW)
  {
      digitalWrite(RELAY_PIN_05, !estado_rele_05);   //Liga o rele
      tempo_torneira_05_aberta = millis();
      presence_05 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_05 && (millis() - tempo_torneira_05_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_05, estado_rele_05);   //Desliga o rele
      tempo_torneira_05_aberta = millis();
      presence_05 = LOW;
  }
}

void torneira_06()
{
  // checando sensor de distancia 06
  float dist_cm_06; long microsec_06 = sensor_dist_06.timing();
  dist_cm_06 = sensor_dist_06.convert(microsec_06, Ultrasonic::CM);
  
  //Verifica se há presença e aciona o relé em caso positivo
  if (dist_cm_06 < limite_detect && presence_06 == LOW)
  {
      digitalWrite(RELAY_PIN_06, !estado_rele_06);   //Liga o rele
      tempo_torneira_06_aberta = millis();
      presence_06 = HIGH;      
  }
  
  //Mantém o relé acionado pelo tempo determinado e depois desliga o relé
  if (presence_06 && (millis() - tempo_torneira_06_aberta >= TEMPO_ACIONAMENTO))
  {
      digitalWrite(RELAY_PIN_06, estado_rele_06);   //Desliga o rele
      tempo_torneira_06_aberta = millis();
      presence_06 = LOW;
  }
}

void debug()
{
  Serial.print("Presenca sensor 1: ");Serial.println(presence_01);
  if (presence_01) Serial.println("Torneira 01 Aberta! 1111111111111111111111111111111111111111");
  
  Serial.print("Presenca sensor 2: ");Serial.println(presence_02);
  if (presence_02) Serial.println("Torneira 02 Aberta! 2222222222222222222222222222222222222222");
  
  Serial.print("Presenca sensor 3: ");Serial.println(presence_03);
  if (presence_01) Serial.println("Torneira 03 Aberta! 3333333333333333333333333333333333333333");
  
  Serial.print("Presenca sensor 4: ");Serial.println(presence_04);
  if (presence_04) Serial.println("Torneira 04 Aberta! 4444444444444444444444444444444444444444");
  
  Serial.print("Presenca sensor 5: ");Serial.println(presence_05);
  if (presence_05) Serial.println("Torneira 05 Aberta! 5555555555555555555555555555555555555555");
  
  Serial.print("Presenca sensor 6: ");Serial.println(presence_06);
  if (presence_06) Serial.println("Torneira 06 Aberta! 6666666666666666666666666666666666666666");

}

