// #include "CPPCode.h"
#include <Arduino.h>

int ball = 4;
int points = 1;
bool dir = HIGH;
 
void setup() {
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(ball, HIGH);
  delay(300);
  digitalWrite(ball, LOW);


  if (digitalRead(2) == HIGH) {
    if (ball == 8) {
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      delay(500);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
    }
    else {
      delay(1000);
    }
    if (ball == 8) {
      //points = points + 1;
      Serial.print("Sut sebber. \n");
    }
  }

  if (dir == HIGH) {
    ball = ball + 1;
  }
  else {
    ball = ball - 1;
  }

  if (ball == 12) {
    dir = LOW;
  }
  else if (ball == 4){
    dir = HIGH;
  }

  if (ball > 12) {
    ball = 4;
  }
}