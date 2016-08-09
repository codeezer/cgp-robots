#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <Wire.h> 
#include <HMC5883L.h> 

HMC5883L compass; 

//right
#define aPwm 10
#define aIn1 12
#define aIn2 13

//left
#define bPwm 6
#define bIn1 8
#define bIn2 7

#define L 13.5
#define R 3.3

float integral1,integral2;
float previous_error_left,previous_error_right;

float kp_1=1,
      kd_1=0.5,
      
      kp_2=1,
      kd_2=0.5;

//Right
#define encAClk 3     //Interrupt Pin
#define encADT 5

//Left
#define encBClk 2     //Interrupt Pin
#define encBDT 4

Encoder knobRight(encAClk, encADT);
Encoder knobLeft(encBClk, encBDT);

int previous_encoder_left=0, previous_encoder_right=0;
int current_encoder_left=0, current_encoder_right=0;

int IntThresh=5;

float time=0,prev_time;
void motioncommand(int v, int w);

float measuredleft = 0;
float measuredright = 0;

float drive_left = 0;
float drive_right = 0;


void setup() {
  //*** Motor Driver **
  pinMode(aPwm, OUTPUT);
  pinMode(aIn1, OUTPUT);
  pinMode(aIn2, OUTPUT);
  pinMode(bPwm, OUTPUT);
  pinMode(bIn1, OUTPUT);
  pinMode(bIn2, OUTPUT);
  Wire.begin();
  compass = HMC5883L();
  compass.SetScale(1.3);
  compass.SetMeasurementMode(Measurement_Continuous);
  //*****************
 
  Serial.begin(9600);

}

void loop() { 
  
  doIt();
  Stop();
  delay(5000);
  
}
  

void doIt(){
  for (int i = 0; i<=400; i++)
  {
    current_encoder_left = knobLeft.read();
    current_encoder_right = -knobRight.read();
  
    motioncommand(6*R,0);
  
    measuredleft = current_encoder_left - previous_encoder_left;
    measuredright = current_encoder_right - previous_encoder_right;
    int xDegree = get_angle();
    
    Serial.print(" Compass:");
    Serial.print(xDegree);
    Serial.print("  l: ");
    Serial.print(measuredleft);
    Serial.print(" r: ");
    Serial.println(measuredright);

  
    //  Serial.println(current_encoder_right - previous_encoder_right);
    //  Serial.print(" ");
  
    previous_encoder_left = current_encoder_left;
    previous_encoder_right = current_encoder_right;
  
    time = millis();
    delay(50 - (time-prev_time)); 
    prev_time = millis();
  }
}

void motioncommand(int v, int w)
{ 
  
  float derivative, derivative2, integral2, cmd_vel, v_left, v_right, error = 0, error2 = 0;
  
  
  v_right = (2*v+w*L)/(2*R);
  v_left = (2*v-w*L)/(2*R);
  

  error = v_left - measuredleft;     /*PID*/
  error2 = v_right - measuredright;  /*PID*/ 
  
  if (abs(error) < IntThresh){
      integral2 = integral2 + error;
  }
  else {
      integral2=0;
  }
  
  derivative = error - previous_error_left;
  derivative2 = error2 - previous_error_right;
  
  drive_left += kp_1*error + kd_1*derivative;
  drive_right += kp_2*error2 + kd_2*derivative2;
  
  drive_left = limit(drive_left);
  drive_right = limit(drive_right);
  
  previous_error_left = error;
  previous_error_right = error2;
  
   
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

  if(drive_right<0)
  {
    digitalWrite (aIn1, LOW);
    digitalWrite (aIn2, HIGH);
  }
  else 
  {
    digitalWrite (aIn1, HIGH);
    digitalWrite (aIn2, LOW);
  }
 
  analogWrite(bPwm,(int)(abs(drive_left)));
  analogWrite(aPwm,(int)(abs(drive_right)));
  
  if (abs(error) < IntThresh){
    integral1 = integral1 + error;
  }
  else {
    integral1=0;
  }

}

int limit(int a)
{
  if(a<-255)
    return -255;
  if(a>255)
    return 255;
  return a;
}

void Stop(){
  digitalWrite (bIn1, LOW);
  digitalWrite (bIn2, LOW);
  digitalWrite (bIn1, LOW);
  digitalWrite (bIn2, LOW);
}

int get_angle(){
  MagnetometerRaw raw = compass.ReadRawAxis(); 
  MagnetometerScaled scaled = compass.ReadScaledAxis(); 
  float xHeading = atan2(scaled.YAxis, scaled.XAxis); 
  //float yHeading = atan2(scaled.ZAxis, scaled.XAxis); 
  //float zHeading = atan2(scaled.ZAxis, scaled.YAxis); 
  
  if(xHeading < 0) xHeading += 2*PI;
  if(xHeading > 2*PI) xHeading -= 2*PI;
  //if(yHeading < 0) yHeading += 2*PI;
  //if(yHeading > 2*PI) yHeading -= 2*PI;
  //if(zHeading < 0) zHeading += 2*PI; 
  //if(zHeading > 2*PI) zHeading -= 2*PI;
  float xDegrees = xHeading * 180/M_PI;
  //float yDegrees = yHeading * 180/M_PI;
  //float zDegrees = zHeading * 180/M_PI;
  return xDegrees;
}


