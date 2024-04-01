#pragma once

#include <Temp.h>
#include <HeartBeat.h>
#include <Motor.h>
#include <StringTok.h>

class ArduinoHub
{
    public:
    ArduinoHub() {}

    void HeartBeat(int nPurplePin)  // 심박센서 핀 입력 
    {
        hb.SetPort(nPurplePin);
    }

    void setMotor(int nMotorPort)   // 서보모터 핀 입력
    {
        motor.setPort(nMotorPort);
    }

    void Temp() // 온도센서 입력
    {
        tp.Ready();
    }

    void setPin(int pinnum) // Relay 스위치 출력
    {   
        pin = pinnum;
        pinMode(pin, OUTPUT);
    }

    void Start()
    {
        while(true)
        {
            long time = millis();

            while (time + 100 > millis())   // 0.1초가 되기 전
            {
                    if (Serial.available() > 0 )    // 입력이 있을 시
                    {
                        stCmd.appendString(getSerialInput());   
                        String sToken = parseCmd(); // 입력구문분석
                        exeCmd(sToken);
                    }
            }
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
    }

    protected:
    Temperature tp;
    Heartbeat hb;    
    Motor motor;
    StringTok stCmd;

    int pin = 3;
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
        if (sToken == "move") { exeMove(); }
        else if (sToken == "push") { exePin(); }
        else if (sToken == "read") { exeRead(); }
        else { Serial.println("Error!"); }
    }
    
    void exeMove()  // 모터 각도조정
    {
        String sToken = parseCmd();
        int ang = sToken.toInt();
        motor.move(ang);
        
        Serial.print("Move ");
        Serial.println(ang);
    }

    void exeRead()  // 모터 각도읽기
    {
        int ang = motor.getServo();
        
        Serial.print("Angle ");
        Serial.println(ang);
    }

    void exePin()   // Relay 스위치 ON/OFF
    {
        if (digitalRead(pin) == LOW)
        {
            digitalWrite(pin, HIGH);
            Serial.println("ON");
        }

        else 
        {
            digitalWrite(pin, LOW);
            Serial.println("OFF");
        }
    }
};