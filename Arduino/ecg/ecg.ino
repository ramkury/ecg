#define OFFSET A1
#define ECG    A0
#define GAIN   10

float toVoltage(int input) {
  return 5 * GAIN * (input / 1024.f);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(OFFSET, INPUT);
  pinMode(ECG, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int offset = analogRead(OFFSET);
  int ecg = analogRead(ECG);
  //Serial.println(toVoltage(ecg - offset));
  //Serial.println(toVoltage(offset));
  Serial.print(toVoltage(offset));
  Serial.print(',');
  Serial.println(toVoltage(ecg));
}
