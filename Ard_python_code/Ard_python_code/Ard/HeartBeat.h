#pragma once

#define Threshold 540
#define AVG 20

class Heartbeat
{
    public:
    Heartbeat() {}
    
    void SetPort(int PurplePin) //포트 설정
    {
        PulseSensorPurplePin = PurplePin;
    }

    int BPM()   // Threshold값을 통해 평균화를 통한 BPM 계산
    {
        int sensorValue = analogRead(PulseSensorPurplePin);

        if (sensorValue > Threshold)
        {
            pulse = true;
        }

        if (pulse == true)
        {
            pulse = false;

            for (int i = 1; i < AVG; i++)
            {
                heartbit_tick[i - 1] = heartbit_tick[i];
            }

            heartbit_tick[AVG - 1] = millis();

            if (heartbit_tick[0] != 0 && heartbit_tick[AVG - 1] != 0)
            {
                float timedur = (float)heartbit_tick[AVG - 1] - (float)heartbit_tick[0];
                bpm = (((AVG-1) * 1000) / timedur) * 60;
            }
        }
        
        return int(bpm);
    }

    int Beat()  // 센서값 평균화를 통한 평탄화
    {
        for (int i = 0; i < AVG; i++)
        {
            sensorValues[i] = sensorValues[i+1];
        }
        
        sensorValues[AVG - 1] = analogRead(PulseSensorPurplePin);
        
        for (int i = 0; i < AVG; i++)
        {
            filteredValue += sensorValues[i];
        }
        
        filteredValue /= AVG;
        
        return int(filteredValue);
    }

protected:
    float sensorValues[AVG];
    float filteredValue = 0.0;
    float bpm = -1.0;
    int PulseSensorPurplePin = 0;
    bool pulse = false;
    unsigned long heartbit_tick[AVG];
};