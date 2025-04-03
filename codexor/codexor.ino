// One-Time Pad XOR Encryption Example

// Keys for XOR encryption (you can change them, but keep them secret)
const char c1 = 0x4F;  // Example XOR key 1
const char c2 = 0xA7;  // Example XOR key 2

// Function to encrypt a message using XOR
String xorEncrypt(String input, char key) {
  String encrypted = "";
  for (int i = 0; i < input.length(); i++) {
    encrypted += (char)(input[i] ^ key);  // XOR each character with the key
  }
  return encrypted;
}

// Function to decrypt a message using XOR (same function as encrypt)
String xorDecrypt(String input, char key) {
  return xorEncrypt(input, key);  // Decryption is the same as encryption for XOR
}

void setup() {
  // Initialize serial communication and pin mode
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);

  // Original message to encrypt
  String originalMessage = "This is a very secret message!";
  Serial.println("Original message: ");
  Serial.println(originalMessage);

  // Encrypt the message with XOR using key c1
  String encryptedMessage = xorEncrypt(originalMessage, c1);
  Serial.println("Encrypted message (c1): ");
  Serial.println(encryptedMessage);

  // Encrypt the message with XOR using key c2
  encryptedMessage = xorEncrypt(encryptedMessage, c2);
  Serial.println("Encrypted message (c2): ");
  Serial.println(encryptedMessage);

  // Decrypt the message back (reverse the process)
  String decryptedMessage = xorDecrypt(encryptedMessage, c2);
  decryptedMessage = xorDecrypt(decryptedMessage, c1);  // Reverse the XOR with key c1

  Serial.println("Decrypted message: ");
  Serial.println(decryptedMessage);
}

void loop() {
  // Blink the LED to indicate the code is running
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on
  delay(2000);                      // wait for 2 seconds
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off
  delay(500);                       // wait for 0.5 seconds
}

