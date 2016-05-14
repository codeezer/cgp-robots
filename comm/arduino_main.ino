#include <SoftwareSerial.h>
//Global Variables Declaration

#define TX 2
#define RX 3
#define BAUD 9600

//***********************
#define aPwm 6
#define aIn1 7
#define aIn2 5

#define bPwm 11
#define bIn1 12
#define bIn2 13
//***********************

SoftwareSerial BT(TX,RX);

String inData;
int x;
int i;

void setup() {
  BT.begin(BAUD);
  BT.println("Hello from Arduino");
  //*****************
  pinMode(aPwm, OUTPUT);
  pinMode(aIn1, OUTPUT);
  pinMode(aIn2, OUTPUT);
  pinMode(bPwm, OUTPUT);
  pinMode(bIn1, OUTPUT);
  pinMode(bIn2, OUTPUT);
  //*****************
}

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
              case 000:
                //BT.println("Read data");
                BT.println("0 received");
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

              case 20:
                dummydata();
              break;
              
              default:
                BT.print("Unknown command");
              break;
            }
            inData = ""; // Clear recieved buffer
        }
    }
}


void dummydata() {
  for(i=0;i<=30;i++)
  {
    BT.print(i);
    BT.print(" ");
    BT.println(i+30);
    delay(5);
  }
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
