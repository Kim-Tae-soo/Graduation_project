#include <ArduinoHub.h>

#define SERIAL_RATE (9600)
#define PULSESENSOR_PORT (0)
#define COOL_PIN (3)
#define HOT_PIN (5)
#define PET_PIN (7)

ArduinoHub adHub;

void setup()
{
  adHub.Temp();
  adHub.HeartBeat(PULSESENSOR_PORT);
  adHub.setSwitch(COOL_PIN, HOT_PIN, PET_PIN);
  Serial.begin(SERIAL_RATE);
}

void loop()
{
  adHub.Start();
}
