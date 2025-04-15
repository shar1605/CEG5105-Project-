#include <AESLib.h>

AESLib aesLib;

byte aesKey[] = {
  0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe,
  0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81
};

// AESLib still expects this IV even in ECB mode
byte aesIV[16]; // zero-initialized globally is fine too

byte encrypted_msg[] = {
  0xb6, 0xa9, 0x99, 0x7f, 0x41, 0x46, 0x32, 0x8d,
  0x0b, 0xd2, 0xef, 0x7a, 0x96, 0xe4, 0x80, 0xd9
};

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  delay(1000);
  Serial.println("AES decryption starting...");
}

void loop() {
  memset(aesIV, 0, 16);  // 🔑 reset IV before each decrypt

  byte decrypted[16];
  aesLib.decrypt(encrypted_msg, sizeof(encrypted_msg), decrypted, aesKey, 128, aesIV);

  char decryptedText[16];              // 15 + null terminator
  memcpy(decryptedText, decrypted, 15);
  decryptedText[15] = '\0';

  Serial.println("Decrypted message:");
  Serial.println(decryptedText);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
