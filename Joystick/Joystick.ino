const int joyX = A0;
const int joyY = A1;
const int joySW = 2;

void setup() {
  Serial.begin(38400);
  pinMode(joySW, INPUT_PULLUP);
  Serial.println("Joystick Test Started");
}

void loop() {
  int x = analogRead(joyX);
  int y = analogRead(joyY);
  int button = digitalRead(joySW);

  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(button);

  delay(300);
}
