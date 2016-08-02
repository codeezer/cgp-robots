#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>


//right
#define aPwm 6 
#define aIn1 7
#define aIn2 8

//left
#define bPwm 10
#define bIn1 13
#define bIn2 12

float integral1,integral2;
float previous_error_left,previous_error_right;
float kp_1=1,
      kd_1=0,
      ki_1=0,
      
      kp_2=1,
      kd_2=0.5;

//Right
#define encAClk 2     //Interrupt Pin
#define encADT 4

//Left
#define encBClk 3     //Interrupt Pin
#define encBDT 5 

Encoder knobRight(encAClk, encADT);
Encoder knobLeft(encBClk, encBDT);

int previous_encoder_left=0,previous_encoder_right=0;
int current_encoder_left=0,current_encoder_right=0;
int IntThresh=5;

float time=0,prev_time;
void motioncommand(int v, int w);
float measuredleft = 0;
float drive_left =0;
void setup() {
    //*** Motor Driver **
    pinMode(aPwm, OUTPUT);
    pinMode(aIn1, OUTPUT);
    pinMode(aIn2, OUTPUT);
    pinMode(bPwm, OUTPUT);
    pinMode(bIn1, OUTPUT);
    pinMode(bIn2, OUTPUT);
    //*****************
    //
    Serial.begin(9600);

}

void loop() { 
  
  current_encoder_left = knobLeft.read();
  current_encoder_right = knobRight.read();
  motioncommand(6,0);
  measuredleft = current_encoder_left - previous_encoder_left;
  Serial.println(measuredleft);
  Serial.print(" ");
  
//  Serial.println(current_encoder_right - previous_encoder_right);
//  Serial.print(" ");
  
  previous_encoder_left = current_encoder_left;
  previous_encoder_right = current_encoder_right;
  time = millis();
  delay(50 - (time-prev_time)); 
  prev_time = millis();
  
  
 }


void motioncommand(int v, int w)
{ 
  
  float measuredright,derivative,integral2,drive_right,cmd_vel,v_left,v_right,error=0;
  v_left = 8;
  v_right = 0;
  

  error = v_left - measuredleft;   /*PID*/
  if (abs(error) < IntThresh){
      integral2 = integral2 + error;
  }
  else {
      integral2=0;
  }
  derivative = error - previous_error_left;
  drive_left += kp_2*error + kd_2*derivative;
  drive_left = limit(drive_left);
  previous_error_left = error;
  
   
  if(drive_left<0)
  {
    digitalWrite (bIn1, LOW);
    digitalWrite (bIn2, HIGH);
  }
  else 
  {
    digitalWrite (bIn1, HIGH);
    digitalWrite (bIn2, LOW);
  }
 
  analogWrite(bPwm,(int)(abs(drive_left)));
  
//  error = v_right - measuredright ;  /*PID*/
  if (abs(error) < IntThresh){
      integral1 = integral1 + error;
  }
  else {
      integral1=0;
  }
//  integral1 = integral1 + error;                  
//  derivative = error - previous_error_right;
//  drive_right = kp_1*error + kd_1*derivative + ki_1*integral1;
//  previous_error_right = error;;

//  if(drive_right<0)
//  {
//    digitalWrite (aIn1, LOW);
//    digitalWrite (aIn2, HIGH);
//  }
//  else 
//  {
//    digitalWrite (aIn1, HIGH);
//    digitalWrite (aIn2, LOW);
//  }
//  analogWrite(bPwm,255/12*abs(drive_right));
    
}

int limit(int a)
{
  if(a<-255)
    return -255;
  if(a>255)
    return 255;
  return a;
}
