#include <SoftwareSerial.h>
SoftwareSerial bluetooth(0, 1); // RX, TX
const int lm35_pin = A0; // Analog pin for thermistor
int led = 13;
int sensorValue = 0;
double temperature;
char command;
char data = 0;

void setup() {
 Serial.begin(9600);
 Serial.println("Bluetooth is ready!");
 bluetooth.begin(9600);
 pinMode(13, OUTPUT);
}

void loop() {
  if(Serial.available() > 0){
   command = Serial.read();
   Serial.println(command);

  }
  if(command == 'A' && temperature >= 30)
  {
    digitalWrite(13, HIGH);
    Serial.println("The LED ON");
  }
  if(command == 'B' )
  {
    digitalWrite(13, LOW);
    Serial.println("The LED OFF");
  }

  while (bluetooth.available() > 0) {
  char data = bluetooth.read();
  Serial.print(data);
  }
  sensorValue = analogRead(lm35_pin);
  temperature = (sensorValue * 4.88) / 10 ;
  Serial.print(temperature);
  Serial.println(" degrees C");

  delay(1000);
}
