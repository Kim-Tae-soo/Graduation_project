#include <ArduinoHub.h>

#define SERIAL_RATE (9600)
#define PULSESENSOR_PORT (0)
#define MOTOR_PORT (7)
#define DIGITAL_OUTPUT (3)

ArduinoHub adHub;

void setup()
{
  adHub.Temp();
  adHub.HeartBeat(PULSESENSOR_PORT);
  adHub.setMotor(MOTOR_PORT);
  adHub.setPin(DIGITAL_OUTPUT);
  Serial.begin(SERIAL_RATE);
}

void loop()
{
  adHub.Start();
}
