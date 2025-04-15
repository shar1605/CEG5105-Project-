String xorEncryptDecrypt(String data, char key) {
  String result = "";
  for (int i = 0; i < data.length(); i++) {
    result += char(data[i] ^ key);
  }
  return result;
}

void setup() {
  Serial.begin(115200);
  delay(1000);  // Wait for Serial Monitor to catch up
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(3000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);

  // Correctly XOR-encrypted version of: "This is a secret message"
  String encrypted = "\xFE\xC2\xC3\xD9\x8A\xC3\xD9\x8A\xCB\x8A\xD9\xCF\xC9\xD8\xCF\xDE\x8A\xC7\xCF\xD9\xD9\xCB\xCD\xCF";

  String message = xorEncryptDecrypt(encrypted, 0xAA);
  Serial.println(message);  // 
}
