const int IN_A0 = A0;
const int IN_D0 = 8;
int valor_A0;
bool valor_D0;


void setup ()
{
  Serial.begin(9600);
  pinMode (IN_A0, INPUT);
  pinMode (IN_D0, INPUT);
  pinMode (LED_BUILTIN, OUTPUT);
}

void loop ()
{
  valor_A0 = analogRead (IN_A0);
  Serial.print ("Analogico: ");
  Serial.println(valor_A0);
  
  valor_D0 = digitalRead (IN_D0);
  Serial.print ("Digital: ");
  Serial.println(valor_D0);
  delay(1000);

  
  if (valor_D0 == 0 || valor_A0 < 200)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  
  else
  {
    Serial.println ("Tem ninguem nao");
    digitalWrite (LED_BUILTIN, LOW);
  }
}
