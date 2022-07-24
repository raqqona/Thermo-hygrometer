#include "bme280_header.h"
#include "wifi_header.h"

INDOOR_ENV indoorEnv;

void setup() {
  Serial.begin(9600);
  Wire.begin(21,22);
  WifiConnect();
  Bme280Init();
}

void loop() {
  ReadBmeData();
  indoorEnv.temp = GetTemp();
  indoorEnv.hum = GetHum();
  indoorEnv.press = GetPress();

  
  SendRequest(indoorEnv);

  delay(30)
}
