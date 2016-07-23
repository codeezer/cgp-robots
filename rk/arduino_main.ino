/* Encoder Library - TwoKnobs Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 *
 * This example code is in the public domain.
 */
#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <SoftwareSerial.h>
#include <PID_v1.h>

//*** Bluetooth ********
#define TX A0
#define RX A1
#define BAUD 9600

//*** Encoder *********
#define encAClk 2     //Interrupt Pin
#define encADT 4
#define encBClk 3     //Interrupt Pin
#define encBDT 5

//*** Motor Driver ******
#define aPwm 6
#define aIn1 7
#define aIn2 8

#define bPwm 10
#define bIn1 12
#define bIn2 13
//***********************

// Change these pin numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability

String inData;
int x;
int i;
SoftwareSerial BT(TX,RX);
Encoder knobRight(encAClk, encADT);
Encoder knobLeft(encBClk, encBDT);
//   avoid using pins with LEDs attached
long right, left;
double Setpoint, Input, Output
PID myPID(&Input, &Output, &Setpoint, 2, 5, 1, DIRECT);

void setup() {
  
      //*** Bluetooth *****

    BT.begin(BAUD);
    BT.println("Hello from Arduino");

    //*** Motor Driver **
    pinMode(aPwm, OUTPUT);
    pinMode(aIn1, OUTPUT);
    pinMode(aIn2, OUTPUT);
    pinMode(bPwm, OUTPUT);
    pinMode(bIn1, OUTPUT);
    pinMode(bIn2, OUTPUT);
    //*****************
  
  Serial.begin(BAUD);
  Serial.println("TwoKnobs Encoder Test:");
}

long positionLeft  = -999;
long positionRight = -999;

void loop() {
    while (BT.available())
    {
        char recieved = BT.read();
        inData += recieved; 

        // Process message when # character is recieved
        if (recieved == '#')
        {
            x=inData.toInt();
            //BT.print("Arduino Received: ");
            //BT.println(x);
            switch (x)
            {
              case 00:
                Stop();
                break;
                
              case 30:
                Enc();
                break;
              
              case 31:
                Reset();
                break;
                
              case 32:
                encoderData();
                break;
              
              case 10:
                BT.println("Move forward");
                mov(LOW, HIGH, LOW, HIGH);
              break;

              case 11:
                BT.println("Move back");
                mov(HIGH, LOW, HIGH, LOW);
                break;

              case 12:
                BT.println("Turn left");
                mov(LOW, HIGH, HIGH, LOW);
                break;

              case 13:
                BT.println("Turn right");
                mov(HIGH, LOW, LOW, HIGH);
                break;
                
              case 33:
                BT.println("Controlled Move");
                controlledMove();
                break;
              
              default:
                BT.println("Unknown command");
                break;
            }
            inData = ""; // Clear recieved buffer
        }
    }
  // if a character is sent from the serial monitor,
  // reset both back to zero.
}

void Enc() { 
  long newLeft, newRight;
  newLeft = knobLeft.read();
  newRight = knobRight.read();
  if (newLeft != positionLeft || newRight != positionRight) {
    BT.print("Left = ");
    BT.print(newLeft);
    BT.print(", Right = ");
    BT.print(newRight);
    BT.println();
    positionLeft = newLeft;
    positionRight = newRight;
  }
}

void Reset() {
    BT.println("Reset both knobs to zero");
    knobLeft.write(0);
    knobRight.write(0);
}

//***********************************

void mov(boolean a1, boolean a2, boolean b1, boolean b2)
{
  digitalWrite(aIn1, a1);
  digitalWrite(aIn2, a2);
  analogWrite(aPwm, 150);  //Duty Cycle value range 0~255

  digitalWrite(bIn1, b1);
  digitalWrite(bIn2, b2);
  analogWrite(bPwm, 150);
  delay(1000);
  Stop();
}

void Stop()
{
  digitalWrite(aIn1, LOW);
  digitalWrite(aIn2, LOW);  
  digitalWrite(bIn1, LOW);
  digitalWrite(bIn2, LOW);
}

//***************************************

void encoderData() {
  right = knobRight.read();
  BT.print("Right enc data   ");
  BT.print(right+"    ");
  
  left = knobLeft.read();
  BT.print("Left enc data   ");
  BT.println(left);
}

void controlledMove() {
  Reset();
  right = knobRight.read();
    digitalWrite(aIn1, LOW);
    digitalWrite(aIn2, HIGH);
    analogWrite(aPwm, 100);  //Duty Cycle value range 0~255

    digitalWrite(bIn1, HIGH);
    digitalWrite(bIn2, LOW);
    analogWrite(bPwm, 100);
    while(1) {
      if ( abs(knobRight.read()) >= 60) {
        Stop();
        break;
      }
    }
}
