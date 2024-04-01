#pragma once

#include <Servo.h>

#define DELAY_TIME (1000)
#define SERVO_SPEED (180. / 1500.)

class Motor
{
public:
    Motor(void) {}

    void setPort(int nPort) //포트 설정
    {
        nPort = nMotorPort;
    }

    int getServo()  // 모터 연결 후 각도 읽기
    {
        m_servo.attach(nMotorPort);

        int motorAng = m_servo.read();
        
        m_servo.detach();

        return motorAng;
    }

    void move(int ang)  // 모터 연결 후 회전명령 수행
    {
        m_servo.attach(nMotorPort);
        
        int nSpeed = int(abs((ang - getServo()) / SERVO_SPEED));
        m_servo.write(ang);
        delay(nSpeed);

        m_servo.detach();
    }

protected:
Servo m_servo; 
int nMotorPort; //포트값 저장
};