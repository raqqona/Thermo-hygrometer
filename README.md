# Thermo-hygrometer

this branch is esp32's code

### 環境
* esp32 DevKit-C
* bme280


### bme280 setup(i2c)
下の表の通りにピンを接続。
| VID | GND | CSB | SDI | SDO | SCK |
| --- | --- | --- | --- | --- | --- |
| 3V3 | GND | 3V3 | 21  | GND | 22  |