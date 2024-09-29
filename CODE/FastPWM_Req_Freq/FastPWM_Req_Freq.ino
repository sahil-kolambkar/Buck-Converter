#include<PWM.h>

int32_t frequency = 20000; //frequency (in Hz)

void setup()
{
 InitTimersSafe();
bool success = SetPinFrequencySafe(9,frequency);
if(success) {
 pinMode(13, OUTPUT);
 digitalWrite(13, HIGH);
 }
}
void loop()
{
 int sensorValue = analogRead(A0);//Adjust the duty cycle
 pwmWrite(9, sensorValue/4);//sensorValue/4 is to get sensorValue=255 when the input is 1023
 delay(10);
}
