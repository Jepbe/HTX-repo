#include <iostream>
using namespace std;

class lights {
  public:
    int led;
};

void setup() {
  lights led_1;
  led_1.led = 11;

  lights led_2;
  led_2.led = 12;

  lights led_3;
  led_3.led = 13;

  //pinMode(led_1.led, OUTPUT);  
  //pinMode(led_2.led, OUTPUT);
  //pinMode(led_3.led, OUTPUT);
}


void loop() {
  // put your main code here, to run repeatedly:
  // digitalWrite(led_1.led, HIGH);   // turn the LED on (HIGH is the voltage level)
  // delay(400);                       // wait for a second
  // digitalWrite(led_1.led, LOW);    // turn the LED off by making the voltage LOW
  // delay(400);  
  // digitalWrite(led_2.led, HIGH);    // turn the LED off by making the voltage LOW
  // delay(400); 
  // digitalWrite(led_2.led, LOW);    // turn the LED off by making the voltage LOW
  // delay(400); 
  // digitalWrite(led_3.led, HIGH);    // turn the LED off by making the voltage LOW
  // delay(400); 
  // digitalWrite(led_3.led, LOW);    // turn the LED off by making the voltage LOW
  // delay(400);  
}
