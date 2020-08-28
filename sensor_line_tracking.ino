const int IN_A0 = A0;
const int IN_D0 = 8;
const int IN_A1 = A1;
const int IN_D1 = 9;
int valor_A0;
bool valor_D0;
int valor_A1;
bool valor_D1;
int LED0 = 7;
int LED1 = 6;


void setup ()
{
  Serial.begin(9600);
  pinMode (IN_A0, INPUT);
  pinMode (IN_D0, INPUT);
  pinMode (IN_A1, INPUT);
  pinMode (IN_D1, INPUT);
  pinMode (LED0, OUTPUT);
  pinMode (LED1, OUTPUT);
}

void loop ()
{
  valor_A0 = analogRead (IN_A0);
  Serial.print ("A0: ");
  Serial.println(valor_A0);
  
  valor_D0 = digitalRead (IN_D0);
  Serial.print ("D0: ");
  Serial.println(valor_D0);
  delay(2000);

  Serial.print("\n");

  valor_A1 = analogRead (IN_A1);
  Serial.print ("A1: ");
  Serial.println(valor_A1);

  valor_D1 = digitalRead (IN_D1);
  Serial.print ("D1: ");
  Serial.println (valor_D1);
  delay(2000);
  Serial.print("\n");

  if (valor_D0 == 0 || valor_A0 <= 200 && valor_D1 == 0 || valor_A1 <= 200)
  {
    digitalWrite(LED0, HIGH);
    digitalWrite(LED1, HIGH);
    delay (1000);
  }
  
  else if (valor_D0 == 0 || valor_A0 <= 200 && valor_D1 == 1 || valor_A1 > 200)
  {
    digitalWrite(LED0, HIGH);
    digitalWrite (LED1, LOW);
    delay (1000);
  }
  
  else if (valor_D1 == 0 || valor_A1 <= 200 && valor_D0 == 1 || valor_A0 > 200 )
  {
    digitalWrite(LED1, HIGH);
    digitalWrite (LED0, LOW);
    delay (1000);
  }
  
  else
  {
    digitalWrite (LED0, LOW);
    digitalWrite (LED1, LOW);
    delay (1000);
  }
}
