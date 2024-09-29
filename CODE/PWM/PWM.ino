int pwm_out = 9; 
int potPin = A1;
int potIn;      // variable to store the value coming from the potentiometer
int pwm_value; // variable to hold the pwm value

void setup() {
  pinMode(pwm_out, OUTPUT);
}

void loop() {
  
  potIn = analogRead(potPin); //reading from potentiometer

  //mapping the Values between 0 to 255
  //long map(long x, long in_min, long in_max, long out_min, long out_max);
  pwm_value = map(potIn, 0, 1023, 0, 255);

  analogWrite(pwm_out, pwm_value);
  delay(1);  //1ms delay
}