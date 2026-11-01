const int leds[]={8, 9, 10, 11, 12};
const int numberOfLeds=5;

void setup() {
  Serial.begin(9600);
  for (int i=0; i<numberOfLeds; i++){
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  if (Serial.available()>0){
    char command =Serial.read();
    if (command >='0' && command <='5') {
      int fingers = command-'0';
      for (int i=0; i<numberOfLeds; i++) {
        if(i<fingers){
          digitalWrite(leds[i],HIGH);
        }
        else{
          digitalWrite(leds[i],LOW);
        }
      }
    }
  }
}
