/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
*/
#include "otp_cipher.h"

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

const char c0[] = {1,83,252,130,94,45,243,44,206,89,239,158,154,206,182,43,82,150,23,59,118,250,191,74,130,243,14,11,193,197,55,210,102};
const char c1[] = {105,54,144,238,49,13,132,67,188,53,139,190,233,171,196,66,51,250,55,75,25,136,203,106,235,128,46,58,240,240,5,226,86};
char xor2[34];
OTP_Cipher(c0, c1, 33, xor2);
  Serial.println(xor2);
memset(xor2, 0, sizeof(xor2));

  Serial.begin(115200);
  
}

// the loop function runs over and over again forever
void loop() {

  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second

const char c3[] = {194,176,206,129,106,117,175,250,203,134,148};
const char c4[] = {170,213,162,237,5,85,216,149,185,234,240};
char xor5[12];
OTP_Cipher(c3, c4, 11, xor5);
  Serial.println(xor5);
memset(xor5, 0, sizeof(xor5));
const char c6[] = {253,228,127,132,179,189,16};
const char c7[] = {144,157,95,234,210,208,117};
char xor8[8];
OTP_Cipher(c6, c7, 7, xor8);
  Serial.println(xor8);
memset(xor8, 0, sizeof(xor8));
}

