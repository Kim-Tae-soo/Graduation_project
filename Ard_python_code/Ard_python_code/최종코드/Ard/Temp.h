#pragma once

#include <Wire.h>
#include <Adafruit_MLX90614.h>

class Temperature
{
  public:
  Temperature() {}

  void Ready()  // 센서 입력
  {
    mlx.begin();
  }

  float ReadTemp()
  {
    if (isnan(mlx.readObjectTempC())) // Nan값 출력시 
    {
      return temp;
    }

    else
    {
      temp = mlx.readObjectTempC();
    } 
    return temp;
  }

  protected:
  Adafruit_MLX90614 mlx = Adafruit_MLX90614();
  float temp = -1.0;
};