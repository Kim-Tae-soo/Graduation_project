#pragma once

#include <StringTok.h>
#include <Temp.h>
#include <HeartBeat.h>

class ArduinoHub
{
    public:
    ArduinoHub() {}

    void HeartBeat(int nPurplePin)  // 심박센서 핀 입력 
    {
        hb.SetPort(nPurplePin);
    }

    void Temp() // 온도센서 입력
    {
        tp.Ready();
    }

    void setSwitch(int coolPin, int hotPin, int PETPin) // Relay 스위치 출력
    {   
        coolSwitch = coolPin;
        hotSwitch = hotPin;
        PETSwitch = PETPin;

        pinMode(coolSwitch, OUTPUT);
        pinMode(hotSwitch, OUTPUT);
        pinMode(PETSwitch, OUTPUT);
    }

    void Start()
    {
        while(true)
        {
            long time = millis();

            while (time + 20 > millis())   // 0.01초가 되기 전
            {
                if (Serial.available() > 0 )    // 입력이 있을 시
                {
                    stCmd.appendString(getSerialInput());   
                    String sToken = parseCmd(); // 입력구문분석
                    exeCmd(sToken);
                }
            }
        }
    }

    protected:
    Temperature tp;
    Heartbeat hb;
    StringTok stCmd;

    int coolSwitch;
    int hotSwitch;
    int PETSwitch;
    float temp = 0.0;
    int beat = 0;
    int BPM = 0;

    String getSerialInput()
    {
        StringTok stInput;

        if (Serial.available() > 0)
        {
            //stInput.appendSerial();
            scans(stInput);

            if (!stInput.isEmpty())
            {
                int nCheckLine = 0;

                while (!stInput.hasLine())
                {
                    stInput.appendSerial();
                    nCheckLine++;
                    if (nCheckLine > 5) { break; }
                }
            }
        }

    return stInput.toString();
    }

    String parseCmd(void)
    {
        return stCmd.cutToken().toString();
    }

    void exeCmd(String sToken)
    {
        if (sToken == "push") { exeSwitch(); }
        else if (sToken == "scan") { exeScan(); }
        else { Serial.println("Error!"); }
    }
    
    void exeScan()
    {
        // 센서값 읽어오는 구문
        temp = tp.ReadTemp();
        beat = hb.Beat();
        BPM = hb.BPM();

        Serial.print(temp);
        Serial.print(" ");
        Serial.print(beat);
        Serial.print(" ");
        Serial.println(BPM);
    }

    void exeSwitch()   // Relay 스위치 ON/OFF
    {
        String sToken = parseCmd();

        if (sToken == "cool")
        {
            if (digitalRead(coolSwitch) == LOW)
            {
                digitalWrite(coolSwitch, HIGH);
                Serial.println("Cool ON");
            }

            else 
            {
                digitalWrite(coolSwitch, LOW);
                Serial.println("Cool OFF");
            }
        }
        
        if (sToken == "hot")
        {
            if (digitalRead(hotSwitch) == LOW)
            {
                digitalWrite(hotSwitch, HIGH);
                Serial.println("Hot ON");
            }

            else 
            {
                digitalWrite(hotSwitch, LOW);
                Serial.println("Hot OFF");
            }
        }
        if (sToken == "pet")
        {
            if (digitalRead(PETSwitch) == LOW)
            {
                digitalWrite(PETSwitch, HIGH);
                Serial.println("PET ON");
            }

            else 
            {
                digitalWrite(PETSwitch, LOW);
                Serial.println("PET OFF");
            }
        }
    }
};